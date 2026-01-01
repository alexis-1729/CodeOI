from app.llm.context_builder import ContextBuilder
from app.llm.guardrails import GuardraiException, Guardrails
from app.llm.prompt_loader import PromptLoader
from app.schemas.tutorSchema import TutorRequest, TutorResponse, TutorAction

class TutorOrchestrator:
    def __init__(self, cliente):
        self.cliente = cliente
        self.context_builder = ContextBuilder()
        self.promptLoader = PromptLoader()
        self.guardrails = Guardrails()

    def run(self, request: TutorRequest)-> str:
        self._validate_request(request)

        # self.guardrails.validate_request(request.context)
        
        context_prompt = self.context_builder.build(request.context)

        system_prompt, user_prompt = self._build_prompts(
            request, context_prompt
        )

        raw_response = self.cliente.complete(
            system_prompt = system_prompt,
            user_prompt = user_prompt
        )

        safe_response = self.guardrails.santize_response(raw_response)

        return safe_response
    
    def _validate_request(self, request: TutorRequest):
        if request.action is None:
            return ValueError("Action requerida")
        
    def _build_prompts(self, request: TutorRequest, context_prompt: str):
        system_prompt = self.promptLoader.load("system")

        action_map = {
            TutorAction.EXPLAIN: "explain",
            TutorAction.SIMPLE_EXPLANATION: "simple",
            TutorAction.EXAMPLE: "example",
            TutorAction.HINT: "hint",
            TutorAction.MISTAKES: "mistakes",
            TutorAction.WHY_IT_WORKS: "why",
        }

        action_key = request.action.value
        prompt_name = action_map[action_key]

        action_prompt = self.promptLoader.load(prompt_name)

        user_prompt = (
            f"{context_prompt}\n\n"
            f"Instruccion:\n{action_prompt}"
        )

        return system_prompt, user_prompt

        