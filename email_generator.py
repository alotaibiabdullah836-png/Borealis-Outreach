import os
import logging
from openai import OpenAI
from typing import Dict

# Initialize logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
log = logging.getLogger(__name__)

# Initialize OpenAI client
client = OpenAI()

BOREALIS_CONTEXT = """
Borealis (AGT-USA Inc.) provides Facility-to-Chip™ cooling solutions.
Key Product: Vega.
Value Proposition:
- AI is melting racks; legacy cooling (CRAC) can't keep up.
- Vega handles 500kW per unit (vs 100kW for traditional units).
- Retrofits to any facility.
- Saves $3.9M per AI rack by preventing compute throttling.
- 30% overhead reduction on cooling, returning power to compute.
- One responsible system, commissioned in days.
"""

def generate_personalized_email(prospect: Dict) -> str:
    """
    Generate a highly personalized, human-sounding outreach email using LLM.
    """
    prompt = f"""
    You are a senior founder at Borealis. Write a personalized, professional, and respectful outreach email to the following prospect.
    
    Prospect Info:
    Name: {prospect['name']}
    Title: {prospect['title']}
    Company: {prospect['company']}
    Industry: {prospect['industry']}
    Location: {prospect['location']}
    Recent News: {prospect.get('recent_news', 'N/A')}
    Business Challenge: {prospect.get('business_challenge', 'N/A')}
    
    Borealis Context:
    {BOREALIS_CONTEXT}
    
    Guidelines:
    - Feel completely human-written, not robotic.
    - No generic sales language or aggressive tactics.
    - Use business psychology: make them feel safe, understood, and respected.
    - Focus on relevance, credibility, and business value.
    - Position the conversation as an exploration.
    - Create a natural reason to respond.
    - Mention their specific industry/role challenges.
    
    Write the Subject Line and the Body.
    """
    
    log.info(f"Generating personalized email for {prospect['name']} at {prospect['company']}")
    
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a senior executive at a high-tech infrastructure company."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    
    return response.choices[0].message.content

if __name__ == "__main__":
    # Test email generation
    sample_prospect = {
        "name": "John Doe",
        "company": "Hyperscale AI",
        "title": "CEO",
        "industry": "AI Infrastructure",
        "location": "Singapore",
        "recent_news": "Hyperscale AI recently announced a new 500MW data center expansion.",
        "business_challenge": "Struggling with high energy costs due to traditional air cooling."
    }
    
    email_content = generate_personalized_email(sample_prospect)
    print(email_content)
