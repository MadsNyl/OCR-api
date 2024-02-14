from fastapi import (
    FastAPI,
    UploadFile,
    HTTPException
)

from lib.utils import (
    convert_image_to_text,
    get_text_sections
)


app = FastAPI()


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
