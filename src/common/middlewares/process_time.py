import time
from typing import Coroutine, Any, Callable

from fastapi.openapi.models import Response
from starlette.requests import Request


async def calculate_process_time(start_time: float) -> float:
    return time.monotonic() - start_time


async def add_process_time_header(request: Request, call_next: Callable[[Request], Coroutine[Any, Any, Response]]) -> Response:
    start_time = time.monotonic()
    response = await call_next(request)
    process_time = await calculate_process_time(start_time)
    response.headers["X-Process-Time"] = f"{process_time:.6f}"
    return response
