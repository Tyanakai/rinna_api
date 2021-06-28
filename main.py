from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import BackgroundTasks

from module import io
from module import schemas
from module import models

app = FastAPI()
model = models.Rinna()

@app.post("/upload")
async def upload_input(data: str):
    filename = io.save_input(data)
    return {"filename": filename}

def prediction(filename, output_size: int=50):
    data = io.load_input(filename)
    model.load()
    input_tensor = model.tokenize(data)
    output_tensor = model.generate(input_tensor, output_size)
    text = model.decode(output_tensor)
    io.save_output(text, filename)
    return {"output was saved"}

@app.get("/predict")
async def predict(filename, output_size:int, background_tasks: BackgroundTasks):
    if io.check_output(filename):
        raise HTTPException(status_code=404, detail="The predicts already exist")
    background_tasks.add_task(prediction, filename, output_size)
    return {"filename": filename}

@app.get("/download")
async def download(filename):
    if not io.check_output(filename):
        raise HTTPException(status_code=404, detail="The file is not found")
    output = io.load_output(filename)
    return {"output": output}
