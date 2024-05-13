from textwrap import dedent
from crewai import Task


class PRDTask:
    # Task for Product Owner for the contribution of Product Requirement Document
    def product_owner_task(self, agent, requirement):
        return Task(
            # based on the requirement create a task for the product owner
            description=dedent(
                f"""\
                Create a Product Requirement Document (PRD) based on the following requirement {requirement}
                """
            ),
            agent=agent,
            expected_output="Product Requirement Document (PRD)",
        )

    # Task for Lead Business Analyst for the contribution of Product Requirement Document
    def lead_business_analyst_task(self, agent, task):
        return Task(
            # based on the requirement create a task for the lead business analyst
            description=dedent(
                f"""\
                Analyze the requirement from product owner and translate it into clear and concise technical requirements for the development team
                """
            ),
            agent=agent,
            expected_output="Technical Requirements from PRD",
            context=[task],
        )

    # Task for Architect for the contribution of Product Requirement Document
    def architect_task(self, agent, task):
        return Task(
            # based on the technical requirements create a task for the architect approve the PRD based on the technical feasibility
            description=dedent(
                f"""\
                Review the technical requirements and approve the Product Requirement Document (PRD) based on the technical feasibility
                """
            ),
            agent=agent,
            context=[task],
            expected_output="Approved Content of PRD",
            output_file="",
        )
