from tortoise import Tortoise
from fastapi import FastAPI


def register_tortoise(app, config=None, generate_schemas=False):
	"""Регистрация tortoise

	:param FastAPI app: Приложение
	:param dict | None config: Конфигурация
	:param bool generate_schemas: Включать в схему?
	"""
	@app.on_event("startup")
	async def init_orm():
		await Tortoise.init(config=config)
		if generate_schemas:
			await Tortoise.generate_schemas()

	@app.on_event("shutdown")
	async def close_orm():
		await Tortoise.close_connections()
