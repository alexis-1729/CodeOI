from pydantic import BaseModel
from enum import Enum
from typing import Optional


class TutorAction(str, Enum):
    EXPLAIN = "explica"
    SIMPLE_EXPLANATION = "explicacion_simple"
    EXAMPLE = "ejemplo"
    HINT = "pista"
    MISTAKES = "common_mistakes"
    WHY_IT_WORKS = "why_it_works"


class TutorHTTPRequest(BaseModel):
    user_id: str
    topic: str
    level: str
    lesson_title: str
    lesson_excerpt: str
    action: TutorAction
    previous_response: Optional[str] = None


class TutorHTTPResponse(BaseModel):
    content: str
