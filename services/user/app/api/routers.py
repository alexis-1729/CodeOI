from fastapi import APIRouter
from app.api.v1.routes import UserRoute

api_router_v1 = APIRouter(
    prefix = "/api/v1"
)

api_router_v1.include_router(
    UserRoute.router,
    prefix = "/user",
    tags = ["User"]
)

router = APIRouter()
router.include_router(api_router_v1)

