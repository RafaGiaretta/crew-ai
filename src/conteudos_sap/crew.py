from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import SerperDevTool
from typing import List
import os

os.environ["SERPER_API_KEY"] = " KEY SERPERDEV AQUI"

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase #notação de entrada para CREW, que recebe agentes e tasks
class ConteudosSap():
    """ConteudosSap crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    
    @agent # cada metodo com esta anotação instancia/define um agente
    def blog_fetcher(self) -> Agent:
        return Agent(
            config=self.agents_config['blog_fetcher'],
            verbose=True,
            tools=[SerperDevTool()]
        )    

    @agent # cada metodo com esta anotação instancia/define um agente
    def news_fetcher(self) -> Agent:
        return Agent(
            config=self.agents_config['news_fetcher'],
            verbose=True,
            tools=[SerperDevTool()]
        )
        
    @agent
    def content_processor(self) -> Agent:
        return Agent(
            config=self.agents_config['content_processor'],
            verbose=True
        )

    @agent
    def topic_classifier(self) -> Agent:
        return Agent(
            config=self.agents_config['topic_classifier'],
            verbose=True
        )

    @agent
    def newsletter_instagram(self) -> Agent:
        return Agent(
            config=self.agents_config['newsletter_instagram'],
            verbose=True
        )
        
    @agent
    def newsletter_linkedin(self) -> Agent:
        return Agent(
            config=self.agents_config['newsletter_linkedin'],
            verbose=True
        )
        
    @agent
    def top_news_picker(self) -> Agent:
        return Agent(
            config=self.agents_config['blog_fetcher'],
            verbose=True
        )    
    
    @agent # cada metodo com esta anotação instancia/define um agente
    def video_script_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['video_script_writer'],
            verbose=True
        )
        
                        
    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    
    @task # cada metodo com esta anotação instancia/gera um objeto task
    def blog_fetch_task(self) -> Task:
        return Task(
            config=self.tasks_config['blog_fetch_task'], # type: ignore[index]
            output_file='blog_fetcher.md'
        )

    @task
    def news_fetch_task(self) -> Task:
        return Task(
            config=self.tasks_config['news_fetch_task'], # type: ignore[index]
            output_file='news_fetcher.md'
        )
        
    @task
    def content_processing_task(self) -> Task:
        return Task(
            config=self.tasks_config['content_processing_task'], # type: ignore[index]
            output_file='report.md'
        )
        
    @task
    def topic_classification_task(self) -> Task:
        return Task(
            config=self.tasks_config['topic_classification_task'], # type: ignore[index]
        )

    @task
    def blog_fetch_task(self) -> Task:
        return Task(
            config=self.tasks_config['blog_fetch_task'], # type: ignore[index]
            output_file='report.md'
        )
        
    @task
    def instagram_newsletter_task(self) -> Task:
        return Task(
            config=self.tasks_config['instagram_newsletter_task'], # type: ignore[index]
            output_file='instagram_newsletter.md'
        )
    @task
    def linkedin_newsletter_task(self) -> Task:
        return Task(
            config=self.tasks_config['linkedin_newsletter_task'], # type: ignore[index]
            output_file='instagram_newsletter.md'
        )
        
    @task
    def top_news_selection_task(self) -> Task:
        return Task(
            config=self.tasks_config['top_news_selection_task'], # type: ignore[index]
        )

    @task
    def video_script_task(self) -> Task:
        return Task(
            config=self.tasks_config['video_script_task'], # type: ignore[index]
            output_file='video_script.md'
        )     
                  

    @crew #montagem do crew(tripulação)
    def crew(self) -> Crew:
        """Creates the ConteudosSap crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            #manager_llm="gpt-4-turbo",
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
