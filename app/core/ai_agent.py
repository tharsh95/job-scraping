import json
from openai import OpenAI
from app.core.config import config
from app.models.schemas import AnalysisResponse

client = OpenAI(api_key=config.OPENAI_API_KEY)

async def analyze_content(content: str):
    """
    Analyze content using OpenAI's GPT model and return structured analysis.
    """
    prompt = """
You are a technical career assistant. I will paste a full job description and company overview below. Your job is to extract and summarize the most important and relevant information that I need to prepare for an upcoming recruiter call.

Please provide your response in the following JSON format:
{
  "company_overview": {
    "what_they_do": "",
    "industry": "",
    "mission_and_product": ""
  },
  "unique_highlights": {
    "technology_and_innovation": "",
    "team_and_background": "",
    "investors_and_funding": "",
    "cultural_edge": ""
  },
  "role_summary": {
    "title": "",
    "tech_stack": [],
    "location": "",
    "working_hours": "",
    "compensation": {
      "base": "",
      "total_ctc": "",
      "equity_or_esops": "",
      "bonuses": ""
    },
    "remote_or_onsite": "",
    "benefits": []
  },
  "requirements": {
    "technical_skills": [],
    "ai_or_agent_frameworks": [],
    "experience_required": "",
    "soft_skills": []
  },
  "responsibilities": {
    "core_tasks": [],
    "ownership_level": "",
    "team_collaboration": "",
    "product_involvement": ""
  },
  "culture_and_values": {
    "values": [],
    "ideal_candidate_traits": []
  },
  "preparation_checklist": {
    "tools_to_review": [],
    "concepts_to_study": [],
    "ai_frameworks_to_learn": []
  },
  "questions_to_ask_recruiter": [] # List the question to ask recruiter
}

Here's the full job description and company text:
# Full Stack Software Engineer | AI | Job Description

### **Role Overview**

Full Stack Software Engineer (JavaScript, Python), Pay: 40LPA (16 Base), Remote role (India-based candidates) (US hours), 5 days/week

---

### About Us

We're an AI agentic learning startup with roots in **San Francisco** and **Toronto**, on a mission to revolutionize how people learn. Our platform doesn't just teach courses—it talks back. It questions, explains, remembers, and adapts. Imagine learning from a real teacher, except it's an AI that never sleeps—and it boosts retention by **10x**.

We're backed by **top-tier investors** and built by a powerhouse team from **IIT, Microsoft, Amazon, Bain, and Goldman Sachs**. If you want to build something cutting-edge, work with insanely driven people, and own major product decisions—welcome home.

---

### What We're Looking For

- **1–2 years of strong JavaScript experience** (React, Node, or similar) **along with Python**. You're full stack and love building high-impact features.
- **Hands-on experience with AI agents, LangChain, or similar LLM frameworks**. You've designed flows, built pipelines, or deployed agentic apps.
- A portfolio of **high-quality UI work**—clean, modern, responsive, with smooth animations and an intuitive feel. The usual stuff doesn't cut it.
- You've worked in **early-stage AI or tech startups (Seed or Series A)** and thrived in ambiguous environments where speed and ownership matter.
- You've **created your own PRDs, scoped solutions, tested end-to-end, and shipped to prod**. You don't wait for permission—you plan, build, and improve.
- You've achieved **quantifiable results**—boosted speed, drove adoption, increased revenue, reduced bugs, or launched something people loved.
- **Able to join soon**. We're hiring fast and moving faster.

---

### What You'll Do

- **Build the Future of Learning**: Architect and develop AI-powered interactive video features that feel like Zoom calls with your smartest teacher.
- **Design & Deploy**: Build beautiful, performant UIs and scalable backend services that serve thousands of learners every day.
- **Collaborate Deeply**: Work cross-functionally with product, design, and AI teams to create experiences that are equal parts magical and reliable.
- **Own Your Work**: Write, test, and ship full-stack code that you're proud of. Debug, refactor, and raise the bar.
- **Improve Systems**: Help shape internal tools, dev velocity, code quality standards, and documentation as we scale.

---

### Who You Are

- A **product-minded engineer** who thinks about the learner experience, not just the code.
- A **strategic builder** who designs scalable solutions and sees three steps ahead.
- A **gritty executor**—willing to fix the subtle bugs, polish the edge cases, and do the hard things that make the product sing.
- A **self-starter** who doesn't wait to be told what to do—you pitch, test, iterate, and ship.
- A **low-ego team player** who gives and receives feedback openly and lifts up others.

---

### Our Culture & Values

- **Customer Obsession**: Everything we ship must delight, not just function.
- **Be an Owner**: Every line of code you write is a reflection of your standards.
- **Superpumped**: High agency, high pace—we're solving hard problems with heart.
- **Bias Toward Output**: Done is better than perfect. Ship, learn, repeat.
- **Nothing But Excellence**: We sweat the small stuff. World-class or nothing.

---

### Perks & Benefits

- **Competitive Pay**: Includes base salary + **ESOPs** + monthly performance bonuses tied to product impact.
- **Work-Life Balance**: Health benefits, gym memberships, paid vacations, your birthday off, and more.
- **Exponential Learning**: Get deep exposure to **LLMs, LangChain, streaming pipelines**, and real-time AI deployments.
- **Major Ownership**: As one of our first engineers, you'll have enormous influence over the product, systems, and team culture.

---

If you're a passionate engineer who codes like a builder, thinks like a product owner, and learns like a founder—we'd love to hear from you.
give me aa prompt i give to llm which extracts important which I can study

    Content:
    {content[:config.MAX_CONTENT_LENGTH]}  # Truncate content
    """

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            response_format={ "type": "json_object" }
        )

        # Extract the raw output
        raw_output = response.choices[0].message.content
        # Parse the raw output into JSON
        parsed_data = json.loads(raw_output)

        # Validate using Pydantic model
        analysis = AnalysisResponse.parse_obj(parsed_data)
        return analysis
    except json.JSONDecodeError as e:
        raise ValueError(f"Error decoding JSON from AI response: {str(e)}")
    except Exception as e:
        raise ValueError(f"Error analyzing content: {str(e)}")
