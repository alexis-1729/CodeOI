from fastapi import APIRouter
from app.api.v1 import tutorRoute

api_router_v1 = APIRouter(
    prefix = "/api/v1"
)

api_router_v1.include_router(
    tutorRoute.router,
    prefix = "/tutor",
    tags = ["TUtor"]
)

router = APIRouter()

router.include_router(api_router_v1)
