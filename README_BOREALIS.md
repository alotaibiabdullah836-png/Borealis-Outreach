# Borealis Automated Outreach System

This system is custom-built for Borealis (AGT-USA Inc.) to automate lead generation and highly personalized outreach for high-value executives in the data center and AI infrastructure sectors.

## Core Features

1.  **Lead Discovery:** Automatically finds CEOs, Founders, and VPs at data centers, hyperscalers, and AI infrastructure companies.
2.  **AI Personalization:** Every email is written by AI (GPT-4) to feel completely human, using your website context and the prospect's company news.
3.  **CRM Database:** Automatically tracks every lead in an Excel file (`data/crm_database.xlsx`) so you never email the same person twice.
4.  **Daily Automation:** Runs every day at 6:00 AM Kuwait Time via GitHub Actions.

## How to Set It Up (The Final Steps)

I have already uploaded all the code to your GitHub. To make it start working, you just need to do these two things:

### 1. Enable the "Daily Brain" (GitHub Actions)
Since I don't have permission to create the automation file directly, please do this:
1.  Go to your GitHub repository: [Investor-outreach-](https://github.com/jhr5rnbk9w-dotcom/Investor-outreach-)
2.  Click **"Add file"** -> **"Create new file"**.
3.  Name it exactly: `.github/workflows/borealis_outreach.yml`
4.  Paste the following code into it:

```yaml
name: Borealis Daily Outreach

on:
  schedule:
    - cron: '0 3 * * *' # Runs at 6:00 AM Kuwait Time (UTC+3)
  workflow_dispatch:

jobs:
  outreach:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          pip install pandas openpyxl requests beautifulsoup4 openai python-dotenv

      - name: Run Borealis Outreach
        run: python main_borealis.py
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          SENDER_EMAIL: ${{ secrets.SENDER_EMAIL }}
          SENDER_PASSWORD: ${{ secrets.SENDER_PASSWORD }}

      - name: Commit and push CRM updates
        run: |
          git config --global user.name "Borealis Bot"
          git config --global user.email "bot@borealis.com"
          git add data/crm_database.xlsx
          git commit -m "Update CRM Database [skip ci]" || echo "No changes"
          git push
```

### 2. Add your "Secrets"
For the system to send emails and use AI, you need to add your credentials to GitHub:
1.  Go to your GitHub repository **Settings** -> **Secrets and variables** -> **Actions**.
2.  Click **"New repository secret"** and add these:
    *   `OPENAI_API_KEY`: Your OpenAI API key (for the AI to write emails).
    *   `SENDER_EMAIL`: The email address you want to send from.
    *   `SENDER_PASSWORD`: Your email password (or App Password if using Gmail).

## How to Monitor
-   **CRM Database:** Every day, the system will update the `data/crm_database.xlsx` file in your GitHub repository. You can download it anytime to see who was contacted.
-   **Actions Tab:** Click the "Actions" tab on GitHub to see if the system ran successfully.

This system is now ready to generate high-value conversations for Borealis!
