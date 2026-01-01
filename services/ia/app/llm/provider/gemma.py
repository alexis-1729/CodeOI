import google.generativeai as genai

class GemmaProvider:
    def __init__(self, api_key: str, model: str):
        genai.configure(api_key = api_key)
        self.model_name = model
        self.model = genai.GenerativeModel(model)

    def complete(self, system_prompt: str, user_prompt: str)-> str:
        temperature = 0.3
        max_tokens = 1000

        prompt = (
            f"{system_prompt}\n\n"
            f"---Contexto del estudiante--\n"
            f"{user_prompt}"
        )

        response = self.model.generate_content(
            prompt,
            generation_config={
                "temperature": temperature,
                "max_output_tokens": max_tokens
            }
        )

        if not response or not response.text:
            return ""
        return response.text.strip()
    