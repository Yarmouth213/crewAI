import os
from crewai import agent, task, crew, process
os.environ["OPENAI_API_Key"]="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"
researcher = agent(
role ='researcher',
goal ='Research new AI insights',
backstory ='You are an AI research Assistant',
verbose = True,
Allow_Delegation = False
)
writer =agent(
role ='Writer',
goal ='Compelling AI atricles about programmang and AI bots',backstory ='You are an AI blog writer',
verbose =True,
allow_delegation=False
)
task1=task(descirption ='Investigate the latest AI trends', Agent=researcher)
task2=task(description ='Write a short blog with the the latest AI trends', Agent=writer)

crew=crew(
    agents=[researcher, writer],
    tasks=[task1, task2],
    verbose=2,
    process=process.sequential
    
)
result = crew.kickoff()