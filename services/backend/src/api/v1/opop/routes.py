from fastapi import APIRouter, HTTPException, status
from tortoise.exceptions import DoesNotExist, IntegrityError

from .models import Opop
from .schemas import OpopCreate, OpopPublic, OpopUpdate

opop_router = APIRouter()


@opop_router.get("/", response_model=list[OpopPublic])
async def get_opops():
	return await Opop.all()


@opop_router.post("/", response_model=OpopPublic)
async def create_opop(opop: OpopCreate):
	opop_dict = opop.dict()
	try:
