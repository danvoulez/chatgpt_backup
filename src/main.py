from fastapi import FastAPI
from services.logger import logger
from services.status import router as status_router

app = FastAPI()
app.include_router(status_router)

logger.info("PromptOS iniciado com sucesso.")
