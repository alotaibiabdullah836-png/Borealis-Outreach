# Investor Outreach Scraper

A free, automated scraper that collects startup funding data from public sources, cross-references investors against the SEBI AIF registry to surface contact details, and allows for automated email outreach. No paid subscriptions needed.

## What's tracked

### Full funding data (`data/funding_<year>.csv`)

| Column | Description |
|---|---|
| `startup_name` | Name of the startup |
| `domain` | Sector / industry (e.g. EdTech, FinTech, HealthTech) |
| `round` | Funding stage (Seed, Series A, Series B, Angel …) |
| `amount_usd` | Ticket size in USD (null if undisclosed) |
| `investor` | Investor name (one row per investor per deal) |
| `headquarters` | City / state where the startup is based |
| `date` | Date of funding announcement |
| `scraped_at` | Date this row was collected |

### Investor contacts (`data/investors.csv`)

| Column | Description |
|---|---|
| `investor` | Investor name |
| `investor_email` | Contact email from SEBI AIF registry (if matched) |
| `sebi_reg_no` | SEBI AIF registration number (if matched) |
| `aif_category` | AIF category (Category I / II / III) |
| `investor_city` | City from SEBI registry |
| `startup_name` | Name of the startup funded |
| `domain` | Sector / industry |
| `round` | Funding stage |
| `amount_usd` | Ticket size in USD |
| `headquarters` | Startup headquarters |
| `date` | Date of funding announcement |

## Data sources

| Source | URL | Method |
|---|---|---|
| StartupTalky 2026 | [link](https://startuptalky.com/indian-startups-funding-investors-data-2026/) | HTML table |
| StartupTalky 2025 | [link](https://startuptalky.com/indian-startups-funding-investors-data-2025/) | HTML table |
| StartupTalky 2024 | [link](https://startuptalky.com/indian-startups-funding-investor-data-2024/) | HTML table |
| SEBI AIF Registry | [link](https://www.sebi.gov.in/sebiweb/other/OtherAction.do?doRecognisedFpi=yes&intmId=16) | HTML scrape |

## How it works

1.  **Every Monday at 6:00 AM IST** a GitHub Actions workflow runs `main.py`
2.  StartupTalky tables (2024, 2025, 2026) are scraped and parsed into structured rows.
3.  The SEBI AIF registry is scraped to collect fund names, registration numbers, categories, contact emails, and cities.
4.  Investors are fuzzy-matched against SEBI fund names (≥ 50% token overlap) to enrich with contact details.
5.  All CSVs are deduplicated and saved to the `data/` directory.
6.  (Optional) Automated emails are sent to investors with valid contact information based on a customizable template.

## Output files

| File | Description |
|---|---|
| `data/funding_2024.csv` | All startup funding deals scraped for 2024 |
| `data/funding_2025.csv` | All startup funding deals scraped for 2025 |
| `data/funding_2026.csv` | All startup funding deals scraped for 2026 |
| `data/investors.csv` | Investors enriched with SEBI AIF contact data |

## Setup (for your own fork)

### 1. Fork this repo

### 2. Enable GitHub Actions
Go to the `Actions` tab and click **Enable workflows**

### 3. Configure Email Sending (Optional)
If you wish to use the automated email sending feature, you need to set up environment variables. Create a file named `.env` in the root directory of the project (e.g., `/home/ubuntu/investor-outreach-scraper/.env`) with the following content:

```
SENDER_EMAIL="your_email@example.com"
SENDER_PASSWORD="your_email_password"
EMAIL_SUBJECT="Investment Opportunity: [Your Company Name]"
EMAIL_BODY="""Hello {investor_name},

I hope this email finds you well. My name is [Your Name] and I am the [Your Title] at [Your Company Name].

We are currently raising capital for our innovative {domain} startup, [Your Company Name], which is [briefly describe what your company does and its impact].

We believe our solution addresses a significant market need and has strong growth potential. We have attached our pitch deck for your review and would be grateful for the opportunity to discuss this further.

Would you be open to a brief call next week to learn more?

Best regards,
[Your Name]
[Your Title]
[Your Company Website (Optional)]
"""
```

**Important:**
*   Replace `your_email@example.com` and `your_email_password` with your actual email credentials. If you are using Gmail, you might need to generate an App Password for this to work, as regular passwords are often blocked for security reasons. Search for 
