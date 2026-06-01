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

def run_borealis_outreach():
    log.info("Starting Borealis Automated Outreach System...")
    db = DatabaseManager()
    
    # 1. Discover Leads
    # In a production environment, this would loop through various target queries
    target_queries = ["Data center operators Singapore", "AI infrastructure founders USA", "Hyperscale data center executives"]
    
    all_new_prospects = []
    for query in target_queries:
        prospects = search_prospects(query)
        all_new_prospects.extend(prospects)
    
    # 2. Process Leads
    for prospect in all_new_prospects:
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
        
        # 4. Send Email (Optional - requires environment variables)
        log.info(f"Preparing to send email to {prospect['name']} ({email})")
        # send_email(email, subject, body) # Uncomment when ready
        
        # 5. Update Database
        db.add_lead({
            "Name": prospect['name'],
            "Company": prospect['company'],
            "Title": prospect['title'],
            "Email": email,
            "Industry": prospect['industry'],
            "Location": prospect['location'],
            "Email Sent": "Yes", # Mark as yes for simulation
            "Date Contacted": datetime.now().strftime("%Y-%m-%d"),
            "Notes": f"Personalized email generated. Subject: {subject}"
        })
        
        # Respectful delay between sends
        time.sleep(5)

    log.info("Borealis Outreach Run Completed.")

if __name__ == "__main__":
    run_borealis_outreach()
