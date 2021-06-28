from pydantic import BaseModel

class Input(BaseModel):
    text: str

class OutputSize(BaseModel):
    output_size: int

class Output(BaseModel):
    text: str