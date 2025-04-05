from fastapi import APIRouter, Depends, HTTPException
import os

router = APIRouter()

def verify_api_key(api_key: str):
    if api_key != os.getenv("API_KEY"):
        raise HTTPException(status_code=401, detail="Unauthorized")
    return api_key

@router.get("/status")
async def status(api_key: str = Depends(verify_api_key)):
    return {"status": "online"}
