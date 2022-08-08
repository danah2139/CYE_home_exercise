from fastapi import APIRouter, Request, Response
import requests
from .config import API_BASEURL


router = APIRouter(prefix="/api/login",)


@router.post("/", tags=["login"])
async def login(request: Request, response: Response):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    body = await request.body()
    res = requests.post(url=API_BASEURL + router.prefix, data=body, headers=headers)
    response.status_code = res.status_code
    return res.json()
