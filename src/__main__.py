import uvicorn
from fastapi import FastAPI
from src.api.routers import all_routers


app = FastAPI()


for router in all_routers:
    app.include_router(router)


def main() -> None:
    uvicorn.run("main:app", host='127.0.0.1', port=8001, reload=True)


if __name__ == "__main__":
    main()