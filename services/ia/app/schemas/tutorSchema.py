from pydantic import BaseModel, Field
from enum import Enum
from typing import Optional, List

class Level(str, Enum):
    INTRO = "introductory"
    BASIC = "basic"
    INTERMEDIATE= "intermediate"
    ADVANCED = "advanced"

class TutorAction(str, Enum):
    EXPLAIN = "explica"
    SIMPLE_EXPLANATION = "explicacion_simple"
    EXAMPLE = "ejemplo"
    HINT = "pista"
    MISTAKES = "errores_comunes"
    WHY_IT_WORKS = "por_que_funciona"

class ProgramingLanguage(str, Enum):
    C= "c"
    CPP= "cpp"
    PYTHON = "python"
    PSEUDOCODE = "pseudocodigo"

class TutorContext(BaseModel):
    level: Level
    topic: str = Field(..., example = "Two Pointers")
    lesson_title: str
    lesson_excerpt: str = Field(
        ...,
        description = "Fragmento del texto que es relevante de la leccion"
    )
    olympiad: str = Field(default = "OMI")
    student_age: Optional[int] = Field(
        default=15,
        ge=8,
        le=20
    )
    prefered_language: ProgramingLanguage = ProgramingLanguage.PSEUDOCODE

class TutorRequest(BaseModel):
    action: TutorAction
    context: TutorContext
    previous_messages: Optional[List[str]] = Field(
        default = None,
        description = "Los mensajes son opcional"
    )

class TutorResponse(BaseModel):
    content: str
    action: TutorAction
    warnings: Optional[List[str]] = None
