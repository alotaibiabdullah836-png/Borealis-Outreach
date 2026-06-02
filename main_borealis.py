import os
import logging
import time
from datetime import datetime
from lead_discovery import search_prospects, enrich_prospect
from email_generator import generate_personalized_email
from email_sender import send_email
from database_manager import DatabaseManager

# Initialize logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
log = logging.getLogger(__name__)

def run_borealis_outreach(limit=100):
    log.info(f"Starting Borealis Automated Outreach System (Limit: {limit})...")
    db = DatabaseManager()
    
    # 1. Discover Leads
    target_queries = [
        "Data center operators Singapore", 
        "AI infrastructure founders USA", 
        "Hyperscale data center executives",
        "Semiconductor fabrication facility managers",
        "HPC facility operators",
        "Colocation provider decision makers"
    ]
    
    all_new_prospects = []
    for query in target_queries:
        prospects = search_prospects(query)
        all_new_prospects.extend(prospects)
    
    # 2. Process Leads
    sent_count = 0
    for prospect in all_new_prospects:
        if sent_count >= limit:
            log.info(f"Reached daily limit of {limit} emails. Stopping.")
            break
            
        email = f"{prospect['name'].lower().replace(' ', '.')}@{prospect['company'].lower().replace(' ', '')}.com" # Simulated email
        prospect['Email'] = email
        
        # Check if already contacted
        if db.is_contacted(email):
            log.info(f"Skipping {prospect['name']} - already in database.")
            continue
        
        # 3. Enrich and Personalize
        enriched_prospect = enrich_prospect(prospect)
        email_content = generate_personalized_email(enriched_prospect)
        
        # Split subject and body (assuming the LLM returns both)
        lines = email_content.split('\n', 1)
        subject = lines[0].replace('Subject:', '').strip()
        body = lines[1].strip() if len(lines) > 1 else email_content
        
        # 4. Send Email
        log.info(f"Preparing to send email to {prospect['name']} ({email})")
        try:
            send_email(email, subject, body)
            sent_count += 1
        except Exception as e:
            log.error(f"Failed to send email to {email}: {e}")
            continue
        
        # 5. Update Database
        db.add_lead({
            "Name": prospect['name'],
            "Company": prospect['company'],
            "Title": prospect['title'],
            "Email": email,
            "Industry": prospect['industry'],
            "Location": prospect['location'],
            "Email Sent": "Yes",
            "Date Contacted": datetime.now().strftime("%Y-%m-%d"),
            "Notes": f"Personalized email generated. Subject: {subject}"
        })
        
        # Respectful delay between sends
        time.sleep(5)

    log.info(f"Borealis Outreach Run Completed. Total sent: {sent_count}")

if __name__ == "__main__":
    # Daily limit of 100 emails as requested
    run_borealis_outreach(limit=100)
