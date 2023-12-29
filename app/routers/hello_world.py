from fastapi import APIRouter

router = APIRouter(prefix="/api/v1/hello-world", tags=["hello-world"])


@router.get("")
async def get_hello_world() -> str:
    return "Hello World!"
