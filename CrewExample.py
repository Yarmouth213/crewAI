from crewai import Agent, Task, Crew, Process
import os
os.environ ["OPENAI_API_Key"] = "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"

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
    process=Process.sequential
    
)
result = crew.kickoff()
tech_crew.kickoff()