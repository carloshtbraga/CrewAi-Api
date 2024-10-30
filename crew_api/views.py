# views.py
from rest_framework import status, viewsets, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Agent, Task, Crew, Llm
from .serializers import AgentSerializer, TaskSerializer, CrewSerializer, llmSerializer, UserRegistrationSerializer
from crewai import Crew as CrewAICrew, Process
from .helpers import create_agents, create_tasks
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]


class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    permission_classes = [IsAuthenticated]


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class CrewViewSet(viewsets.ModelViewSet):
    queryset = Crew.objects.all()
    serializer_class = CrewSerializer

    @action(detail=True, methods=["post"])
    def execute_kickoff(self, request, pk=None):
        try:
            topic = request.data.get('topic')
            if not topic:
                return Response({"error": "O campo 'topic' é obrigatório."}, status=status.HTTP_400_BAD_REQUEST)
            crew = self.get_object()
            db_tasks = crew.tasks.all()

            # Cria agentes e tarefas utilizando as funções auxiliares
            configured_agents, agent_mapping = create_agents(crew)
            configured_tasks = create_tasks(db_tasks, agent_mapping)

            # Configura a Crew AI
            crew_ai = CrewAICrew(
                agents=configured_agents,
                tasks=configured_tasks,
                process=Process[crew.process],
            )

            result = crew_ai.kickoff(inputs={'topic': topic})

            return Response({"result": result}, status=status.HTTP_200_OK)

        except Exception as e:
            # Trata a exceção e retorna uma resposta de erro
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class LlmViewSet(viewsets.ModelViewSet):
    queryset = Llm.objects.all()
    serializer_class = llmSerializer

