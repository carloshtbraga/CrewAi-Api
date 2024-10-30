# helpers.py
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from crewai import Agent as CrewAIAgent, Task as CrewAITask

# Carregando as variáveis de ambiente
load_dotenv()


def create_gemini15flash_llm_instance():
    """Cria e retorna uma instância da LLM."""
    try:
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError(
                "A variável de ambiente 'GOOGLE_API_KEY' não foi encontrada."
            )
        return ChatGoogleGenerativeAI(
            model="gemini-1.5-flash",
            verbose=True,
            temperature=0.5,
            google_api_key=api_key,
        )
    except Exception as e:
        # Trata a exceção e relança
        raise Exception(f"Erro ao criar instância da LLM: {e}")


def create_agents(crew):
    """
    Cria e retorna uma lista de agentes configurados para a Crew AI.

    Args:
        crew (Crew): Instância do modelo Crew do banco de dados.

    Returns:
        tuple: Uma tupla contendo a lista de agentes configurados e um dicionário de mapeamento de IDs.
    """
    try:
        configured_agents = []
        agent_mapping = {}

        for agent in crew.agents.all():
            crewai_agent = CrewAIAgent(
                role=agent.role,
                goal=agent.goal,
                llm=create_gemini15flash_llm_instance(),
                memory=agent.memory,
                backstory=agent.backstory,
                verbose=agent.verbose,
            )

            configured_agents.append(crewai_agent)
            agent_mapping[agent.id] = crewai_agent

        return configured_agents, agent_mapping
    except Exception as e:
        # Trata a exceção e relança
        raise Exception(f"Erro ao criar agentes: {e}")


def create_tasks(db_tasks, agent_mapping):
    """
    Cria e retorna uma lista de tarefas configuradas para a Crew AI.

    Args:
        db_tasks (QuerySet): Conjunto de tarefas do banco de dados.
        agent_mapping (dict): Mapeamento de IDs de agentes para instâncias de agentes configurados.

    Returns:
        list: Lista de tarefas configuradas.
    """
    try:
        configured_tasks = []

        for task in db_tasks:
            # Verifica se a tarefa tem um agente atribuído
            crewai_agent = agent_mapping.get(task.agent.id) if task.agent else None

            crewai_task = CrewAITask(
                description=task.description,
                expected_output=task.expected_output,
                async_execution=task.async_execution,
                output_file=task.output_file,
                agent=crewai_agent,
            )

            configured_tasks.append(crewai_task)

        return configured_tasks
    except Exception as e:
        # Trata a exceção e relança
        raise Exception(f"Erro ao criar tarefas: {e}")
