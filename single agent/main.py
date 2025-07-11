from crew import InvestimentCrew

def run_investiment_assistent(pergunta: str):
    crew_agent = InvestimentCrew()
    result = crew_agent.crew().kickoff(inputs={'pergunta': pergunta})
    return result