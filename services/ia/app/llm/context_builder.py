class ContextBuilder:

    def build(self, context):
        return (
            f"Perfil de estudiante:\n"
            f"- Edad: {context.student_age}\n"
            f"- Nivel: {context.level.value}\n"
            f"- Olimpiada: {context.olympiad}\n\n"
            f"Contexto de la leccion:\n"
            f"- Tema: {context.topic}\n"
            f"- Titulo: {context.lesson_title}\n"
            f"- Excerpt:\n{context.lesson_excerpt}\n\n"
            f"Presentacion preferida: {context.prefered_language.value}"
        )