import os
import shutil
from fastapi import FastAPI, File, UploadFile, Form, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

from ats_score import calculate_ats_score
from resume_parser import parse_resume

app = FastAPI()

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

@app.post("/getats")
@limiter.limit("5/minute")
async def upload_resume(
    request: Request,
    file: UploadFile = File(...),
    job_description: str = Form(...)
):
    temp_path = f"temp_{file.filename}"
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    data = parse_resume(temp_path)
    os.remove(temp_path)

    resume_text = data.get("text", "").strip()
    if not resume_text:
        return JSONResponse(content={"error": "Could not extract text from resume."})

    try:
        score = calculate_ats_score(resume_text, job_description)
        return JSONResponse(content={"ats_score": score})
    except Exception as e:
        return JSONResponse(content={"error": str(e)})
