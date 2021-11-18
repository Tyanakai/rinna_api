from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import BackgroundTasks

import models
import transact
import schemas

app = FastAPI()
model = models.Rinna()

@app.post("/upload")
async def upload_input(data: schemas.Input):
    filename = transact.save_input(data)
    return {"filename": filename}

def prediction(filename: str, output_size: schemas.OutputSize=50):
    data = transact.load_input(filename)
    model.load()
    input_tensor = model.tokenize(data)
    output_tensor = model.generate(input_tensor, output_size)
    text = model.decode(output_tensor)
    transact.save_output(text, filename)
    return {"output was saved"}

@app.get("/predict")
async def predict(filename: str, output_size:schemas.OutputSize, background_tasks: BackgroundTasks):
    if transact.check_output(filename):
        raise HTTPException(status_code=404, detail="The predicts already exist")
    background_tasks.add_task(prediction, filename, output_size)
    return {"filename": filename}

@app.get("/download", response_model=schemas.Output)
async def download(filename: str):
    if not transact.check_output(filename):
        raise HTTPException(status_code=404, detail="The file is not found")
    output = transact.load_output(filename)
    return {"output": output}
