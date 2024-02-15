from fastapi import (
    FastAPI,
    UploadFile,
    HTTPException,
    Request
)
from fastapi.responses import JSONResponse

from lib.utils import (
    convert_image_to_text,
    get_text_sections
)

from settings import api_key


app = FastAPI()


@app.middleware("http")
async def check_api_key(request: Request, call_next):
    response = await call_next(request)
    try:
        print(api_key)
        print(request.headers)
        api_key_header = request.headers["x-api-key"]
        if api_key_header != api_key:
            return JSONResponse(
                status_code=403,
                content={"detail": "Invalid API Key"}
            )
        return response
    except KeyError:
        return JSONResponse(
            status_code=403,
            content={"detail": "API Key is required"}
        )


@app.post("/")
async def read_image(image: UploadFile):
    content_type = image.content_type

    if not content_type or content_type.lower() != "image/jpeg":
        raise HTTPException(
            status_code=400,
            detail="Only jpeg images are supported"
        )
    
    try:
        text = convert_image_to_text(image.file)
        sections = get_text_sections(text)
        return {
            "full_text": text,
            "sections": sections
        }
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="An error occurred while processing the image"
        )
