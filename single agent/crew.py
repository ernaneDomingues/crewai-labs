from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.knowledge.source.pdf_knowledge_source import PDFKnowledgeSource
import os
from dotenv import load_dotenv

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

pdf_tool = PDFKnowledgeSource(
    file_paths=[r'Desempenho Financeiro Petrobras 1T25.pdf', r'Petrobras ITR Reais Port.pdf', r'Petrobras Relatório de Produção e Vendas 1T25.pdf', 'Petrobras Relatório Fiscal 1T25.pdf']
)

llm_tool = LLM(model='gemini/gemini-2.5-pro',
               api_key=gemini_api_key,
               temperature=0)

@CrewBase
class InvestimentCrew:
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def investiment_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['investiment_analyst'],
            verbose=True,
            tools=[],
            llm=llm_tool,
        )

    @task
    def investment_task(self) -> Task:
        return Task(
            config=self.tasks_config['reporting_task'],
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=[self.investiment_analyst()],
            tasks=[self.investment_task()],
            process=Process.sequential,
            verbose=True,
            knowledge_sources=[pdf_tool],
        )