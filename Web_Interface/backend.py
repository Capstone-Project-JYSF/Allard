from fastapi import FastAPI, Form
from pydantic import BaseModel
import csv
from fastapi.responses import FileResponse
import uvicorn
from fastapi.staticfiles import StaticFiles
from pathlib import Path

css_directory = Path(__file__).parent / "css"
imgs_directory = Path(__file__).parent / "images"

app = FastAPI()
app.mount("/css", StaticFiles(directory= css_directory), name="css")
app.mount("/images", StaticFiles(directory=imgs_directory), name="images")

# csv_filepath = Path(__file__).parent / "form_data.csv"

class FormData(BaseModel):
    location: str
    l_represented: str
    length: str
    rent: str
    rent_deposit: str
    checkbox: list[str] = []

@app.post("/submit-form")
def submit_form(data: FormData):
    # Create a dictionary with the form data
    
    
    print(data)
    
    # Save the form data to a CSV file
    with open("form_data.csv", mode="w", newline="") as file:
        writer = csv.writer(file)#, fieldnames=data.__fields__.keys()
        writer.writerow(
            [data.location, data.l_represented, data.length, data.rent_deposit, ",".join(data.checkbox)])
    
    return pass_file("result.html")


@app.get("/")
async def start():
    return FileResponse("index.html")

@app.get("/{filename}")
async def pass_file(filename):
    return FileResponse(filename)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
