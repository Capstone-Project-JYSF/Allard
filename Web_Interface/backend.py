from fastapi import FastAPI, Form, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import csv
from fastapi.responses import FileResponse, RedirectResponse, JSONResponse
import uvicorn
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import json
from fastapi.templating import Jinja2Templates

css_directory = Path(__file__).parent / "css"
imgs_directory = Path(__file__).parent / "images"

app = FastAPI()
app.mount("/css", StaticFiles(directory= css_directory), name="css")
app.mount("/images", StaticFiles(directory=imgs_directory), name="images")

# Allow cross-origin resource sharing (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create an instance of the Jinja2Templates class
templates = Jinja2Templates(directory=Path(__file__))

class FormData(BaseModel):
    location: str
    l_represented: str
    length: str
    rent: str
    rent_deposit: str
    checkbox: list[str] = []


def calculate_probabilities():
    # Perform your calculations and get the probabilities
    probabilities = {
        'probability1': 0.8,
        'probability2': 0.5,
        'probability3': 0.3
    }
    return probabilities

def save_to_csv(data):
    with open("form_data.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(data)


@app.post("/submit-form")
async def submit_form(request: Request):
    form_data = await request.form()
    data = dict(form_data)

    print(data)
    # Process the received form data
    location = data.get('location')
    l_represented = data.get('l_represented')
    length = data.get('length')
    rent = data.get('rent')
    rent_deposit = data.get('rent_deposit')
    checkbox = data.get('checkbox[]').split(',')
    print(checkbox)


    # Save the form data to a CSV file
    csv_data = [location, l_represented, length, rent,rent_deposit]+checkbox 
    save_to_csv(csv_data)

    # Perform calculations and get probabilities
    probabilities = calculate_probabilities()

    # Prepare the JSON response
    response_data = {
        'probabilities': probabilities
    }

    return JSONResponse(content=response_data)



@app.get("/result")
async def show_result(request: Request):
    # Your code to retrieve the probabilities from the model
    probabilities = [0.7, 0.2, 0.1]

    context = {"request": request, "probabilities": probabilities}
    return templates.TemplateResponse("result.html", context)

@app.get("/")
async def start():
    return FileResponse("index.html")

@app.get("/{filename}")
async def pass_file(filename):
    return FileResponse(filename)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
