from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets
from .models import Agent, Task, Crew
from .serializers import AgentSerializer, TaskSerializer, CrewSerializer
from crewai import Crew as CrewAI, Process


class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class CrewViewSet(viewsets.ModelViewSet):
    queryset = Crew.objects.all()
    serializer_class = CrewSerializer

    @action(detail=True, methods=['post'])
    def execute_kickoff(self, request, pk=None):
        try:
            crew = self.get_object()  # Obtém a Crew pelo ID
            agents = list(crew.agents.all())
            tasks = list(crew.tasks.all())

            # Cria a instância da Crew do Crew AI com as informações do banco de dados
            crewai_crew = CrewAI(
                agents=agents,  # Certifique-se de que os agentes estão no formato correto
                tasks=tasks,    # Certifique-se de que as tarefas estão no formato correto
                process=Process.sequential if crew.process == 'sequential' else Process.hierarchical  # Usando o processo
            )
            # Execute o kickoff
            result = crewai_crew.kickoff()  # Chama o método kickoff

            return Response({"result": result}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
