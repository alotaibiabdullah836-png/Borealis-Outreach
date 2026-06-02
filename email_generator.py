import logging
from typing import Dict

# Initialize logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
log = logging.getLogger(__name__)

def generate_personalized_email(prospect: Dict) -> str:
    """
    Generate a professional, personalized outreach email using a Smart Template for Borealis.
    This version does not require an OpenAI API Key.
    """
    name = prospect.get('name', 'there')
    company = prospect.get('company', 'your company')
    title = prospect.get('title', 'Executive')
    industry = prospect.get('industry', 'infrastructure')
    
    subject = f"Cooling Architecture for {company}'s AI Infrastructure"
    
    body = f"""Hello {name},

I hope you're having a productive week.

I'm reaching out because of your role as {title} at {company}. With the rapid expansion of {industry} requirements, we've seen that traditional cooling infrastructure is increasingly becoming a bottleneck for high-density AI racks.

At Borealis (AGT-USA), we've developed the Vega system— a Facility-to-Chip™ cooling solution specifically designed for this challenge. Unlike legacy CRAC units that handle ~100kW, a single Vega unit manages up to 500kW and retrofits directly into your existing facility.

Our partners are seeing significant returns by preventing compute throttling, which can save upwards of $3.9M per AI rack. 

I'd love to share how our cooling architecture can return that 30% power overhead back to your compute operations. Would you be open to a brief exploration call next Tuesday or Wednesday?

Best regards,

Founder, Borealis
AGT-USA Inc.
https://borealis-aurora-d00f11.fly.dev
"""
    
    log.info(f"Generated Smart Template email for {name} at {company}")
    return f"Subject: {subject}\n\n{body}"

if __name__ == "__main__":
    # Test smart template generation
    sample_prospect = {
        "name": "John Doe",
        "company": "Hyperscale AI",
        "title": "CEO",
        "industry": "AI Infrastructure",
    }
    
    email_content = generate_personalized_email(sample_prospect)
    print(email_content)
