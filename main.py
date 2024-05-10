from crewai import Crew
from agents.prd_agents import PRDAgent
from tasks.prd_tasks import PRDTask
from crewai.process import Process
import os

os.environ["OPENAI_API_KEY"] = ""

agent = PRDAgent()

task = PRDTask()

# Agents
product_owner_agent = agent.product_owner_agent()
lead_business_analyst_agent = agent.lead_business_analyst_agent()
architect_agent = agent.architect_agent()

# Tasks
product_owner_task = task.product_owner_task(product_owner_agent)
lead_business_analyst_task = task.lead_business_analyst_task(
    lead_business_analyst_agent, product_owner_task
)
architect_task = task.architect_task(architect_agent, lead_business_analyst_task)

# Crew
crew = Crew(
    agents=[product_owner_agent, lead_business_analyst_agent, architect_agent],
    tasks=[product_owner_task, lead_business_analyst_task, architect_task],
    process=Process.sequential,
    verbose=2,
)

result = crew.kickoff()

# crew usage metrics
print(crew.usage_metrics)
