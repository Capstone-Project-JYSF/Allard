from fastapi import FastAPI, Form, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import csv
from fastapi.responses import FileResponse, RedirectResponse
import uvicorn
from fastapi.staticfiles import StaticFiles
from pathlib import Path

css_directory = Path(__file__).parent / "css"
imgs_directory = Path(__file__).parent / "images"

app = FastAPI()
app.mount("/css", StaticFiles(directory= css_directory), name="css")
app.mount("/images", StaticFiles(directory=imgs_directory), name="images")

# # Allow cross-origin resource sharing (CORS)
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

class FormData(BaseModel):
    location: str
    l_represented: str
    length: str
    rent: str
    rent_deposit: str
    checkbox: list[str] = []

# @app.post("/submit-form")
# def submit_form(data: FormData):
#     # Create a dictionary with the form data
    
    
#     print("Hello World")
    
#     # Save the form data to a CSV file
#     with open("form_data.csv", mode="w", newline="") as file:
#         writer = csv.writer(file)#, fieldnames=data.__fields__.keys()
#         writer.writerow(
#             [data.location, data.l_represented, data.length, data.rent_deposit, ",".join(data.checkbox)])
    
#     return {}

# @app.post("/submit-form")
# async def submit_form(data: dict):
#     # Process the received form data
#     location = data.get('location')
#     l_represented = data.get('l_represented')
#     length = data.get('length')
#     rent = data.get('rent')
#     rent_deposit = data.get('rent_deposit')
#     checkbox = data.get('checkbox')

#     print("Hellloooooo")
#     # Save the form data to a CSV file
#     with open('form_data.csv', mode='a', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow([location, l_represented, length, rent,rent_deposit,checkbox])

#     return {"message": "Form submitted successfully"}

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
    checkbox = data.get('checkbox')

    # Save the form data to a CSV file
    csv_data = [location, l_represented, length, rent,rent_deposit,checkbox]
    save_to_csv(csv_data)

    return RedirectResponse(url="/result.html")

def save_to_csv(data):
    with open("form_data.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(data)

@app.get("/")
async def start():
    return FileResponse("index.html")

@app.get("/{filename}")
async def pass_file(filename):
    return FileResponse(filename)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
