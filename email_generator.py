import logging
import random
from typing import Dict

# Initialize logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
log = logging.getLogger(__name__)

def generate_personalized_email(prospect: Dict) -> str:
    """
    Generate a high-impact, psychologically-driven outreach email for Borealis.
    Focuses on curiosity, relevance, and business value rather than a cold sales pitch.
    """
    name = prospect.get('name', 'there')
    company = prospect.get('company', 'your company')
    title = prospect.get('title', 'Executive')
    
    # Selection of psychologically framed subject lines
    subjects = [
        f"Quick question regarding {company}'s AI infrastructure",
        f"Cooling architecture for {company}'s next expansion",
        f"A brief exploration: {company} + Borealis",
        f"Reducing {company}'s power overhead by 30%"
    ]
    
    # Selection of high-impact body templates
    templates = [
        f"""Hello {name},

I’ve been following {company}’s progress in the AI infrastructure space, and it’s clear you’re scaling at an impressive rate. 

As you likely know, the "thermal wall" is becoming the single biggest bottleneck for high-density racks. We’ve developed a Facility-to-Chip™ architecture at Borealis (AGT-USA) called Vega that handles 500kW per unit—specifically to prevent the compute throttling that costs most hyperscalers millions.

I’m not here to sell you anything today. I’m interested in an exploration of how our technology might return that 30% power overhead back to your compute operations.

Would you be open to a brief, low-pressure conversation next week to see if there's a fit?

Best regards,

Founder, Borealis
AGT-USA Inc.
https://borealis-aurora-d00f11.fly.dev""",

        f"""Hi {name},

I'm reaching out because, as {title} at {company}, you're likely dealing with the massive cooling challenges that come with modern AI deployments.

Most legacy systems (CRAC) were never built for the 100kW+ racks we see today. Our Vega system handles 500kW and retrofits into your existing facility in days, not months. The goal is simple: stop burning compute power on inefficient cooling.

I'd love to share some of the math on how we're saving facilities $3.9M per rack by keeping chips at peak performance.

Are you open to a quick 10-minute exchange of ideas next Tuesday or Wednesday?

Best,

Founder, Borealis
AGT-USA Inc.
https://borealis-aurora-d00f11.fly.dev"""
    ]
    
    subject = random.choice(subjects)
    body = random.choice(templates)
    
    log.info(f"Generated Psychological Outreach email for {name} at {company}")
    return f"Subject: {subject}\n\n{body}"
