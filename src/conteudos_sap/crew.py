from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import SerperDevTool
from typing import List

import os

os.environ["SERPER_API_KEY"] = os.getenv("SERPER_KEY")

@CrewBase
class ConteudosSap():
    """RafaNews crew"""

    agents: List[BaseAgent]
    tasks: List[Task]


    @agent
    def news_seeker(self) -> Agent:
        return Agent(
            config=self.agents_config['news_seeker'], # type: ignore[index]
            verbose=True,
            tools=[SerperDevTool()]
        )

    @agent
    def news_cleaner(self) -> Agent:
        return Agent(
            config=self.agents_config['news_cleaner'], # type: ignore[index]
            verbose=True
        )
        
    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['reporting_analyst'], # type: ignore[index]
            verbose=True,
            llm="gpt-4o"
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    
        
    @task
    def news_research_task(self) -> Task:
        return Task(
            config=self.tasks_config['news_research_task'], # type: ignore[index]
            output_file='news_research.md'
        )
        
    @task
    def news_cleaning_task(self) -> Task:
        return Task(
            config=self.tasks_config['news_cleaning_task'], # type: ignore[index]
        )
        
    @task
    def news_reporting_task(self) -> Task:
        return Task(
            config=self.tasks_config['news_reporting_task'], # type: ignore[index]
            output_file='resumos.md'
        )
        
    @crew
    def crew(self) -> Crew:
        """Creates the RafaNews crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge


        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            verbose=True,
            manager_llm="gpt-4o",  # Specify which LLM the manager should use
            process=Process.hierarchical, # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
            planning=True, 
        )
