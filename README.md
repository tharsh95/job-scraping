# FastAPI Web Scraper with AI Analysis

## Overview
This project is a FastAPI application that performs the following tasks:
1. Scrapes content from a given URL using an async scraper.
2. Analyzes the scraped content using an AI agent.
3. Provides results through a RESTful API.

## Features
- **Web Scraping**: Extracts content from JavaScript-rendered websites using Playwright.
- **AI Analysis**: Uses an AI agent to analyze content and provide structured responses.
- **Authorization**: Secured with an API key in the `Authorization` header.

---

## Installation

### Prerequisites
- Python 3.10 or later
- Docker (optional for containerization)
- Playwright (for web scraping)

### Local Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/tharsh95/job-scraping.git
   cd job-scraping
   ```
2. Install
   ```bash
   pip install -r requirements.txt
   playwright install
   ```
3. Run the application
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```
   ## Hosted Link
   ```bash
   http://ec2-13-201-76-216.ap-south-1.compute.amazonaws.com/scrape
   ```
## Endpoints
### POST /scrape
  - Scrapes a URL and analyzes its content.

  Request
  Headers:
  ```bash
Authorization: Bearer <Secret_Api_key>
  ```
### Body
```bash
{
  "url": "https://example.com"
}
```
### Response
Status code - 200 OK
```bash
{
  "company_overview": {
    "what_they_do": "An AI agentic learning startup focused on revolutionizing how people learn through an interactive platform that utilizes AI technology.",
    "industry": "Education/Tech",
    "mission_and_product": "Revolutionize the learning experience by providing an AI-powered platform that engages users and boosts retention."
  },
  "unique_highlights": {
    "technology_and_innovation": "Utilizing AI agents, LangChain, and similar frameworks to create interactive learning experiences.",
    "team_and_background": "Founded by a team with backgrounds from IIT, Microsoft, Amazon, Bain, and Goldman Sachs. Backed by top-tier investors.",
    "investors_and_funding": "Backed by top-tier investors, operates as a remote-first company (India-based candidates for remote roles), offering competitive compensation including ESOPs and bonuses tied to product impact.",
    "cultural_edge": "Values customer obsession, ownership, high agency and pace, bias toward output, and excellence in everything they do."
  },
  "role_summary": {
    "title": "Full Stack Software Engineer",
    "tech_stack": ["JavaScript", "Python", "AI agents", "LangChain"],
    "location": "Remote (India-based candidates)",
    "working_hours": "US hours, 5 days/week",
    "compensation": {
      "base": "16LPA",
      "total_ctc": "40LPA",
      "equity_or_esops": "Included in compensation package",
      "bonuses": "Monthly performance bonuses"
    },
    "remote_or_onsite": "Remote",
    "benefits": ["Health benefits", "Gym memberships", "Paid vacations", "Birthday off"]
  },
  "requirements": {
    "technical_skills": ["JavaScript", "Python", "React", "Node"],
    "ai_or_agent_frameworks": ["AI agents", "LangChain"],
    "experience_required": "1–2 years of strong JavaScript experience, hands-on experience with AI agents or similar frameworks, and experience in early-stage AI or tech startups",
    "soft_skills": ["Product-minded", "Strategic thinker", "Gritty executor", "Self-starter", "Low-ego team player"]
  },
  "responsibilities": {
    "core_tasks": ["Architect and develop AI-powered interactive video features", "Build UIs and backend services", "Collaborate with product, design, and AI teams", "Ownership of full-stack code", "Contribute to system improvements"],
    "ownership_level": "High ownership and responsibility for the product",
    "team_collaboration": "Deep collaboration across functions",
    "product_involvement": "Direct involvement in designing and deploying interactive learning features"
  },
  "culture_and_values": {
    "values": ["Customer Obsession", "Be an Owner", "Superpumped", "Bias Toward Output", "Nothing But Excellence"],
    "ideal_candidate_traits": ["Passionate engineer", "Product owner mindset", "Founder-like learning approach"]
  },
  "preparation_checklist": {
    "tools_to_review": ["AI agents", "LangChain"],
    "concepts_to_study": ["Interactive learning design", "AI-powered features"],
    "ai_frameworks_to_learn": ["LangChain"]
  },
  "questions_to_ask_recruiter": []
} ro 
```
### Errors:

#### 401 Unauthorized: Missing or invalid API key.
#### 500 Internal Server Error: Failed to scrape or analyze content.

--
