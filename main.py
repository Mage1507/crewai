from crewai import Crew
from langchain_openai import ChatOpenAI
from agents.prd_agents import PRDAgent
from tasks.prd_tasks import PRDTask
from crewai.process import Process
import os

from tools.file_management_tool import FileManager

os.environ["OPENAI_API_KEY"] = ""

agent = PRDAgent()

task = PRDTask()

# Agents
product_owner_agent = agent.product_owner_agent()
lead_business_analyst_agent = agent.lead_business_analyst_agent()
architect_agent = agent.architect_agent()

# Tasks
product_owner_task = task.product_owner_task(
    product_owner_agent,
    "Creation of a new, modern draft platform that will be utilized by NHL(Natioanl Hockey League) and all 32 clubs during the Draft event to select players, add players, and perform perform trades",
)
lead_business_analyst_task = task.lead_business_analyst_task(
    lead_business_analyst_agent, product_owner_task
)
architect_task = task.architect_task(architect_agent, lead_business_analyst_task)

# Crew
crew = Crew(
    agents=[product_owner_agent, lead_business_analyst_agent, architect_agent],
    tasks=[product_owner_task, lead_business_analyst_task, architect_task],
    process=Process.hierarchical,
    manager_llm=ChatOpenAI(model="gpt-4"),
    verbose=2,
)

crew.kickoff()

# usage metrics

file_manager = FileManager(["write_file"])

write_tool = file_manager.get_tool(0)

write_tool.invoke(
    {
        "file_path": "",
        "text": str(crew.usage_metrics),
    }
)
