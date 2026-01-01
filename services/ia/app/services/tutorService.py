from app.llm.tutor_orchestrator import TutorOrchestrator
from app.llm.cliente import LLMClient
from app.schemas.tutorSchema import TutorRequest, TutorContext
from app.api.v1.schemas import TutorHTTPRequest

class TutorService:
    
    def __init__(self):
        client = LLMClient()
        self.orchestrator = TutorOrchestrator(client)

    def handle(self, request: TutorHTTPRequest)-> str:

        tutor_input = TutorRequest(
            action = request.action,
            context = TutorContext(
                level = request.level,
                topic = request.topic,
                lesson_title = request.lesson_title,
                lesson_excerpt = request.lesson_excerpt
            ),
            previous_messages =(
                [request.previous_response]
                if request.previous_response else None
            )
        )

        return self.orchestrator.run(tutor_input)