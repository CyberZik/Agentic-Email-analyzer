import os
from crewai import LLM
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import (
	FileReadTool,
	ScrapeWebsiteTool
)



@CrewBase
class AiAgentEmailSecurityAnalyzerCrew:
    """AiAgentEmailSecurityAnalyzer crew"""

    
    @agent
    def email_artifact_extractor(self) -> Agent:
        
        return Agent(
            config=self.agents_config["email_artifact_extractor"],
            tools=[
				FileReadTool()
            ],
            reasoning=False,
            inject_date=True,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
        )
    
    @agent
    def authentication_validator(self) -> Agent:
        
        return Agent(
            config=self.agents_config["authentication_validator"],
            tools=[
				ScrapeWebsiteTool()
            ],
            reasoning=False,
            inject_date=True,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
        )
    
    @agent
    def threat_intelligence_enricher(self) -> Agent:
        
        return Agent(
            config=self.agents_config["threat_intelligence_enricher"],
            tools=[
				ScrapeWebsiteTool()
            ],
            reasoning=False,
            inject_date=True,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
        )
    
    @agent
    def header_anomaly_detector(self) -> Agent:
        
        return Agent(
            config=self.agents_config["header_anomaly_detector"],
            tools=[

            ],
            reasoning=False,
            inject_date=True,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
        )
    
    @agent
    def psychological_manipulation_detector(self) -> Agent:
        
        return Agent(
            config=self.agents_config["psychological_manipulation_detector"],
            tools=[

            ],
            reasoning=False,
            inject_date=True,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
        )
    
    @agent
    def holistic_ai_analyst(self) -> Agent:
        
        return Agent(
            config=self.agents_config["holistic_ai_analyst"],
            tools=[

            ],
            reasoning=False,
            inject_date=True,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
        )
    
    @agent
    def risk_decision_arbiter(self) -> Agent:
        
        return Agent(
            config=self.agents_config["risk_decision_arbiter"],
            tools=[

            ],
            reasoning=False,
            inject_date=True,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
        )
    
    @agent
    def security_report_archivist(self) -> Agent:
        
        return Agent(
            config=self.agents_config["security_report_archivist"],
            tools=[

            ],
            reasoning=False,
            inject_date=True,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
        )
    

    
    @task
    def extract_email_artifacts(self) -> Task:
        return Task(
            config=self.tasks_config["extract_email_artifacts"],
        )
    
    @task
    def validate_email_authentication(self) -> Task:
        return Task(
            config=self.tasks_config["validate_email_authentication"],
        )
    
    @task
    def enrich_threat_intelligence(self) -> Task:
        return Task(
            config=self.tasks_config["enrich_threat_intelligence"],
        )
    
    @task
    def detect_header_anomalies(self) -> Task:
        return Task(
            config=self.tasks_config["detect_header_anomalies"],
        )
    
    @task
    def analyze_psychological_manipulation(self) -> Task:
        return Task(
            config=self.tasks_config["analyze_psychological_manipulation"],
        )
    
    @task
    def synthesize_ai_analysis(self) -> Task:
        return Task(
            config=self.tasks_config["synthesize_ai_analysis"],
        )
    
    @task
    def make_final_risk_decision(self) -> Task:
        return Task(
            config=self.tasks_config["make_final_risk_decision"],
        )
    
    @task
    def generate_security_reports(self) -> Task:
        return Task(
            config=self.tasks_config["generate_security_reports"],
        )
    

    @crew
    def crew(self) -> Crew:
        """Creates the AiAgentEmailSecurityAnalyzer crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
