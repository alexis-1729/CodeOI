from fastapi import APIRouter
from app.api.v1.routes import topicRoute, levelRoute, lessonRoute



api_router_v1 = APIRouter(
    prefix = "/api/v1"
)

api_router_v1.include_router(
    topicRoute.router,
    prefix = "/topics",
    tags = ["Topics"]
)

api_router_v1.include_router(
    levelRoute.router,
    prefix = "/level",
    tags = ["Levels"]
)

api_router_v1.include_router(
    lessonRoute.router,
    prefix = "/lessons",
    tags = ["Lessons"]
)

router = APIRouter()

router.include_router(api_router_v1)
