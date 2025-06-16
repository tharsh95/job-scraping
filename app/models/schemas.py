from pydantic import BaseModel, HttpUrl, Field
from typing import List, Optional

class ScrapeRequest(BaseModel):
    url: HttpUrl = Field(..., description="The URL of the website to scrape.")

class Compensation(BaseModel):
    base: str = Field(..., description="Base salary information")
    total_ctc: str = Field(..., description="Total cost to company")
    equity_or_esops: str = Field(..., description="Equity or ESOPs details")
    bonuses: str = Field(..., description="Bonus structure information")

class CompanyOverview(BaseModel):
    what_they_do: str = Field(..., description="What the company does")
    industry: str = Field(..., description="Industry the company operates in")
    mission_and_product: str = Field(..., description="Company's mission and product details")

class UniqueHighlights(BaseModel):
    technology_and_innovation: str = Field(..., description="Key technological innovations")
    team_and_background: str = Field(..., description="Team composition and background")
    investors_and_funding: str = Field(..., description="Investor and funding information")
    cultural_edge: str = Field(..., description="Unique cultural aspects")

class RoleSummary(BaseModel):
    title: str = Field(..., description="Job title")
    tech_stack: List[str] = Field(..., description="Required technology stack")
    location: str = Field(..., description="Job location")
    working_hours: str = Field(..., description="Working hours")
    compensation: Compensation = Field(..., description="Compensation details")
    remote_or_onsite: str = Field(..., description="Work arrangement")
    benefits: List[str] = Field(..., description="List of benefits")

class Requirements(BaseModel):
    technical_skills: List[str] = Field(..., description="Required technical skills")
    ai_or_agent_frameworks: List[str] = Field(..., description="Required AI/agent frameworks")
    experience_required: str = Field(..., description="Required experience")
    soft_skills: List[str] = Field(..., description="Required soft skills")

class Responsibilities(BaseModel):
    core_tasks: List[str] = Field(..., description="Core responsibilities")
    ownership_level: str = Field(..., description="Level of ownership expected")
    team_collaboration: str = Field(..., description="Team collaboration expectations")
    product_involvement: str = Field(..., description="Product involvement details")

class CultureAndValues(BaseModel):
    values: List[str] = Field(..., description="Company values")
    ideal_candidate_traits: List[str] = Field(..., description="Desired candidate traits")

class PreparationChecklist(BaseModel):
    tools_to_review: List[str] = Field(..., description="Tools to review")
    concepts_to_study: List[str] = Field(..., description="Concepts to study")
    ai_frameworks_to_learn: List[str] = Field(..., description="AI frameworks to learn")

class AnalysisResponse(BaseModel):
    company_overview: CompanyOverview
    unique_highlights: UniqueHighlights
    role_summary: RoleSummary
    requirements: Requirements
    responsibilities: Responsibilities
    culture_and_values: CultureAndValues
    preparation_checklist: PreparationChecklist
    questions_to_ask_recruiter: List[str] = Field(..., description="Questions to ask the recruiter")
