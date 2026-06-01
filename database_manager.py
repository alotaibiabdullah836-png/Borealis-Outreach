import pandas as pd
import os
import logging
from datetime import datetime
from typing import Dict, List

# Initialize logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
log = logging.getLogger(__name__)

DB_PATH = os.path.join(os.path.dirname(__file__), "data", "crm_database.xlsx")

class DatabaseManager:
    def __init__(self, path: str = DB_PATH):
        self.path = path
        self.columns = [
            "Name", "Company", "Title", "Email", "Industry", "Location",
            "Date Added", "Date Contacted", "Email Sent", "Replied",
            "Meeting Booked", "Follow-up Required", "Notes", "Last Activity Date"
        ]
        self._initialize_db()

    def _initialize_db(self):
        if not os.path.exists(os.path.dirname(self.path)):
            os.makedirs(os.path.dirname(self.path), exist_ok=True)
        
        if not os.path.exists(self.path):
            df = pd.DataFrame(columns=self.columns)
            df.to_excel(self.path, index=False)
            log.info(f"Initialized new CRM database at {self.path}")

    def get_all_leads(self) -> pd.DataFrame:
        return pd.read_excel(self.path)

    def is_contacted(self, email: str) -> bool:
        df = self.get_all_leads()
        return email in df['Email'].values

    def add_lead(self, lead_data: Dict):
        df = self.get_all_leads()
        
        new_row = {col: lead_data.get(col, "") for col in self.columns}
        new_row["Date Added"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_row["Email Sent"] = "No"
        new_row["Replied"] = "No"
        new_row["Meeting Booked"] = "No"
        
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        df.to_excel(self.path, index=False)
        log.info(f"Added new lead: {lead_data['Name']} from {lead_data['Company']}")

    def update_lead_status(self, email: str, updates: Dict):
        df = self.get_all_leads()
        if email in df['Email'].values:
            for key, value in updates.items():
                if key in self.columns:
                    df.loc[df['Email'] == email, key] = value
            df.loc[df['Email'] == email, "Last Activity Date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            df.to_excel(self.path, index=False)
            log.info(f"Updated status for {email}")

if __name__ == "__main__":
    # Test database manager
    db = DatabaseManager()
    sample_lead = {
        "Name": "John Doe",
        "Company": "Hyperscale AI",
        "Title": "CEO",
        "Email": "john@hyperscale.ai",
        "Industry": "AI Infrastructure",
        "Location": "Singapore"
    }
    if not db.is_contacted(sample_lead["Email"]):
        db.add_lead(sample_lead)
    
    db.update_lead_status("john@hyperscale.ai", {"Email Sent": "Yes", "Date Contacted": datetime.now().strftime("%Y-%m-%d")})
    print(db.get_all_leads())
