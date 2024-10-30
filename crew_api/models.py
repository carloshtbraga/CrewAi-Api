from django.db import models


class Agent(models.Model):
    role = models.CharField(max_length=100, help_text="Papel do agente, ex: 'Content Writer'")
    goal = models.TextField(help_text="Objetivo do agente, ex: 'Compose articles on trending topics'")
    verbose = models.BooleanField(default=False, help_text="Define se o agente será detalhado nas respostas")
    memory = models.BooleanField(default=False, help_text="Se o agente tem ou não memória persistente")
    backstory = models.TextField(blank=True, help_text="História de fundo do agente")
    llm = models.ForeignKey('Llm', on_delete=models.SET_NULL, related_name='agents', help_text="Modelo de linguagem natural do agente", blank=True, null=True)
    # tools = models.JSONField(help_text="Ferramentas disponíveis para o agente", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.role}"


class Task(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name="tasks", help_text="Agente responsável pela tarefa")
    description = models.TextField(help_text="Descrição da tarefa, incluindo o objetivo e detalhes, ex: 'Compose an insightful article on {topic}'")
    expected_output = models.TextField(help_text="Formato esperado do output da tarefa, ex: 'A 4 paragraph article on {topic}'", blank=True)
    async_execution = models.BooleanField(default=True, help_text="Define se a execução da tarefa é assíncrona")
    output_file = models.CharField(max_length=100, help_text="Nome do arquivo de saída para o output da tarefa", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.description}"

    from django.db import models


class Crew(models.Model):
    PROCESS_CHOICES = [
        ('sequential', 'Sequential'),
        ('hierarchical', 'Hierarchical'),
    ]

    agents = models.ManyToManyField(Agent, related_name='crews', help_text="Agentes que compõem a equipe")
    tasks = models.ManyToManyField(Task, related_name='crews', help_text="Tarefas atribuídas à equipe")
    process = models.CharField(max_length=50, choices=PROCESS_CHOICES, help_text="Tipo de processo da equipe")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Crew ({self.process})"


class Llm(models.Model):
    model = models.CharField(max_length=100, help_text="Nome do modelo, ex: gemini-1.5-flash")
    verbose = models.BooleanField(default=False, help_text="Define se a llm será detalhado nas respostas")
    temperature = models.FloatField(default=0.5, null=True, blank=True,  help_text="Define a temperatura da amostragem")

    def __str__(self):
        return f"{self.model}"
