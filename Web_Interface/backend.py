from fastapi import FastAPI, Form, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import csv
from fastapi.responses import FileResponse, RedirectResponse, JSONResponse
import uvicorn
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import json
import joblib
from fastapi.templating import Jinja2Templates
from backend_functions import *

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
    l_represented: int
    l_attendance: int
    t_represented: int
    t_attend: int
    non_profit: int
    subsidy: int
    rent_increase: int
    pay_after_eviction: int
    history_arrears: int
    ability_pay: int
    condition: int
    children: int
    income: int
    job_loss: int
    extenuating: int
    house_search: int
    prior_notice: int
    postponement_arrear: int
    n4: int
    employment: int
    payment_plan: float
    length: str
    rent: str
    rent_deposit: str
    arrear_amount: str
    arrear_month: str
    gov_assistance: int
    stability: int
    checkbox: list[str] = []




@app.post("/submit-form")
async def submit_form(request: Request):
    form_data = await request.form()
    data = dict(form_data)

    print(data)
    # Process the received form data
    location = data.get('location')
    l_represented = data.get('l_represented')
    l_attendance = data.get('l_attendance')
    t_represented = data.get('t_represented')
    t_attend = data.get('t_attend')
    non_profit = data.get('non_profit')
    subsidy = data.get('subsidy')
    rent_increase = data.get('rent_increase')
    pay_after_eviction = data.get('pay_after_eviction')
    history_arrears = data.get('history_arrears')
    ability_pay = data.get('ability_pay')
    condition = data.get('condition')
    children = data.get('children')
    income = data.get('income')
    job_loss = data.get('job_loss')
    extenuating = data.get('extenuating')
    house_search = data.get('house_search')
    prior_notice = data.get('prior_notice')
    postponement_arrear = data.get('postponement_arrear')
    n4 = data.get('n4')
    payment_plan = data.get('payment_plan')
    employment = data.get('employment')
    length = convert_length(data.get('length'))
    rent = convert_rent(data.get('rent'))
    rent_deposit = convert_rent_deposit(data.get('rent_deposit'))
    arrear_amount = convert_arrear_amount(data.get('arrear_amount'))
    arrear_month = convert_arrear_month(data.get('arrear_month'))
    gov_assistance = data.get('gov_assistance')
    stability = data.get('stability')
    checkbox = convert_checkbox(data.get('checkbox[]').split(','))
    print(checkbox)


    # Save the form data to a CSV file
    csv_data = [
        'XXX', 'John Doe', 
        location, l_represented, l_attendance, 
        t_represented, t_attend, non_profit, 
        subsidy, length, rent, 
        rent_deposit, rent_increase, arrear_amount, 
        arrear_month, pay_after_eviction, history_arrears,
        ability_pay, condition,children, 
        employment, gov_assistance,stability,
        income, job_loss, extenuating,
        house_search,prior_notice, postponement_arrear, 
        n4, payment_plan, 
        ] + checkbox 
    
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
