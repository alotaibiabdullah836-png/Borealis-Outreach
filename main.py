import os
import logging
import pandas as pd
from scraper.run import scrape_year, clean, scrape_sebi_aif, match_investors, STARTUPTALKY_URLS, FINAL_COLS_GENERAL, FINAL_COLS_FULL, DATA_DIR
from email_sender import send_email

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
log = logging.getLogger(__name__)

def run_scraper():
    os.makedirs(DATA_DIR, exist_ok=True)
    
    all_full_df = []
    for year, url in STARTUPTALKY_URLS.items():
        df = scrape_year(year, url)
        if not df.empty:
            all_full_df.append(df)

    full_df = pd.concat(all_full_df, ignore_index=True) if all_full_df else pd.DataFrame()
    full_df = clean(full_df)

    sebi_df = scrape_sebi_aif()

    # Match investors with SEBI AIF registry
    general_investors_df = match_investors(full_df, sebi_df)

    # Save general investor contacts
    if not general_investors_df.empty:
        general_investors_df = general_investors_df[FINAL_COLS_GENERAL].drop_duplicates(subset=["investor", "investor_email"])
        investors_path = os.path.join(DATA_DIR, "investors.csv")
        general_investors_df.to_csv(investors_path, index=False)
        log.info(f"Saved {len(general_investors_df)} investor contacts to {investors_path}")
    else:
        log.warning("No investor contacts found.")

    # Save full funding data
    for year, url in STARTUPTALKY_URLS.items():
        df_year = full_df[full_df["date"].str.contains(year, na=False)].copy()
        if not df_year.empty:
            df_year = df_year[FINAL_COLS_FULL].drop_duplicates(subset=["startup_name", "investor", "date"])
            funding_path = os.path.join(DATA_DIR, f"funding_{year}.csv")
            df_year.to_csv(funding_path, index=False)
            log.info(f"Saved {len(df_year)} full funding deals to {funding_path}")
            
    return general_investors_df

def send_outreach_emails(investors_df):
    if investors_df.empty:
        log.info("No investors to email.")
        return

    # Filter out rows without email
    valid_emails_df = investors_df[investors_df['investor_email'].astype(bool) & investors_df['investor_email'].str.contains('@')]
    
    log.info(f"Found {len(valid_emails_df)} investors with valid email addresses.")
    
    subject = os.getenv("EMAIL_SUBJECT", "Investment Opportunity")
    body_template = os.getenv("EMAIL_BODY", "Hello {investor_name},\n\nWe have an exciting investment opportunity in the {domain} space.\n\nBest regards,\n[Your Name]")

    for index, row in valid_emails_df.iterrows():
        email = row['investor_email']
        investor_name = row['investor']
        domain = row.get('domain', 'startup')
        
        body = body_template.format(investor_name=investor_name, domain=domain)
        
        log.info(f"Sending email to {investor_name} at {email}...")
        send_email(email, subject, body)
        
        # Add a small delay to avoid rate limits
        time.sleep(2)

if __name__ == "__main__":
    log.info("Starting Investor Outreach Scraper...")
    
    # 1. Run the scraper to get data
    investors_df = run_scraper()
    
    # 2. Send emails to the scraped investors
    # Uncomment the line below to actually send emails after configuring environment variables
    # send_outreach_emails(investors_df)
    
    log.info("Process completed.")
