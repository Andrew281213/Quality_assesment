from fastapi import FastAPI
from fastapi import Response, status, Request
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from pydantic import ValidationError
from pydantic.error_wrappers import ErrorWrapper
from starlette.responses import JSONResponse

from .api import router as api_router
from .database.config import TORTOISE_ORM
from .database.register import register_tortoise

app = FastAPI(debug=True)
# app.mount("/static", StaticFiles(directory=static_dir), name="static")
app.include_router(api_router, prefix="/api")
origins = [
	"http://localhost",
	"http://localhost:8081"
]
app.add_middleware(
	CORSMiddleware,
	allow_origins=origins,
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"]
)


@app.exception_handler(RequestValidationError)
async def validation_accept_handler(request: Request, exc: RequestValidationError) -> Response:
	try:
		raw_errors = exc.raw_errors
		error_wrapper: ErrorWrapper = raw_errors[0]
		validation_error: ValidationError = error_wrapper.exc
		errors = validation_error.errors()
		error_type = errors[0].get("type")
		custom_detail = errors[0].get("msg", "")
		error_fields = []
		for error in errors:
			if error.get("type") == error_type:
				error_fields += error.get("loc", [])
		error_fields = ", ".join(error_fields)
		custom_detail = custom_detail + " " + error_fields
		return JSONResponse(
			status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
			content={"detail": custom_detail}
		)
	except AttributeError:
		return JSONResponse(
			status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
			content={"detail": "Не удалось преобразовать данные в json"}
		)


register_tortoise(app, config=TORTOISE_ORM, generate_schemas=False)
