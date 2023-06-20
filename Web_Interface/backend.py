from fastapi import FastAPI, Form
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

csv_filepath = Path(__file__).parent / "form_data.csv"

@app.post("/submit-form")
async def submit_form(location: str = Form(...), l_represented: str = Form(...), length: str = Form(...),
                      rent: str = Form(...), rent_deposit: str = Form(...), checkbox: list[str] = Form(...)):
    # Create a dictionary with the form data
    form_data = {
        "location": location,
        "l_represented": l_represented, #landlord represented
        "length": length,
        "rent": rent,
        "rent_deposit": rent_deposit,
        "checkbox": checkbox
    }
    print(form_data)
    
    # Save the form data to a CSV file
    with open(csv_filepath, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=form_data.keys())
        writer.writerow(form_data)
    
    return pass_file("result.html")


@app.get("/")
async def start():
    return FileResponse("index.html")

@app.get("/{filename}")
async def pass_file(filename):
    return FileResponse(filename)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
