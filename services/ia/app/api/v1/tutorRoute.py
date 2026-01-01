from fastapi import APIRouter, Depends
from app.api.v1.schemas import TutorHTTPResponse, TutorHTTPRequest
from app.services.tutorService import TutorService


router = APIRouter()


def get_tutor_service():
    return TutorService()

@router.post("/chat")
def tutor_endpoint(
    request: TutorHTTPRequest,
    service: TutorService = Depends(get_tutor_service)
):
    retsult = service.handle(request)
    return retsult