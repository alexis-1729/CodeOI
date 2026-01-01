from abc import ABC
from app.core.config import settings
from app.llm.provider.gemma import GemmaProvider


class LLMClient:
    """
    Interfaz para cualquier cliente
    """

    def __init__(self):
        self.provider = self._load_provider()
        
    def _load_provider(self):
        if settings.LLM_PROVIDER == "gemma":
            return GemmaProvider(
                api_key= settings.GOOGLE_API_KEY,
                model= settings.GOOGLE_MODEL
            )

    def complete(
        self,
        system_prompt: str,
        user_prompt: str
    )-> str:
        return self.provider.complete(
            system_prompt= system_prompt,
            user_prompt= user_prompt
        )
        
