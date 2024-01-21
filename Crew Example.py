from crewai import Agent, Task, Crew, Process
import os
os.environ["OPENAI_API_Key"]="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"


researcher = Agent(
role ='researcher',
goal ='Research new AI insights',
backstory ='You are an AI research Assistant',
verbose = True,
Allow_Delegation = False
)

writer = Agent(
role ='Writer',
goal ='Compelling AI atricles about programmang and AI bots',
backstory ='You are an AI blog writer',
Verbose =True,
allow_delegation=False
)

task1=Task(descirption ='Investigate the latest AI trends', agent = researcher)

task2=Task(description ='Write a short blog with the the latest AI trends', agent= writer)

crew=Crew(
    agents=[researcher, writer],
    tasks=[task1, task2],
    verbose=2,
    process=Process.sequential
    
)
result = Crew.kickoff()