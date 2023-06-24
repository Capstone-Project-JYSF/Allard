import re
import csv
import joblib

headers = [
    'case number', 'Who was the member adjudicating the decision?', 
    'What was the location of the landlord tenant board?', 
    'Did the decision state the landlord was represented?', 
    'Did the decision state the landlord attended the hearing?', 
    'Did the decision state the tenant was represented?', 
    'Did the decision state the tenant attended the hearing?', 
    'Did the decision state the landlord was a not-for-profit landlord (e.g. Toronto Community Housing)?', 
    'Did the decision state the tenant was collecting a subsidy?', 
    'What was the length of the tenancy', 
    'What was the monthly rent?', 'rental deposit amount', 'was there an rent increases', 
    'What was the total amount of arrears?', 
    'Over how many months did the arrears accumulate?', 
    'Does the tenant made a payment on the arrears after the eviction notice', 
    "Did the decision mention a history of arrears by the tenant separate from the arrears in the current claim (more than one period of arrears, recurrently coming in and out of arrears, arrears with previous landlord, etc.)?",
    'Did the member find the tenant had or seemed to have the ability to pay rent, but chose not do so?', 
    "What were the specific mental, medical, or physical conditions of the tenant, if any?",
    'Did the decision state that the tenant had children living with them?', 
    'Was the tenant employed at the time of the hearing?', 
    "If the tenant was not employed, did the decision state the tenant was receiving any form of government assistance (e.g. OW, childcare benefits, ODSP, OSAP)?",
    "If the tenant was employed, did the decision state any doubts about the stability of employment e.g. lack of guaranteed hours, contract work, etc.?",
    'Did the member find the tenant had sufficient income to pay rent?', 
    'Did the decision mention the tenant lost their job leading up to or during the period of the hearing?', 
    "Did the decision mention any other extenuating circumstances experienced by the tenant leading up to or during the period of the claim (e.g. hospitalization, death in the family, etc.)?",
    "Did the decision mention the tenant's difficulty finding alternative housing for any reason e.g.physical limitations, reliance on social assistance, etc.?",
    'Did the decision state the tenant was given prior notice for the eviction?', 
    'Did the decisions state postponement would result in the tenant accruing additional arrears?', 
    'Did the decision mention the validity of an N4 eviction notice?', 
    'Payment Plan', 
    'L1 present?', 'L2 present?', 'L3 present?', 'L4 present?', 'L8 present?', 'L9 present?', 'N5 present?', 'N6 present?', 'N7 present?', 'N8 present?', 'T1 present?', 'T2 present?', 'T3 present?', 'T5 present?', 'T6 present?']




def save_to_csv(data):
    """ 
    Save data to a csv file in current directory.
    """
    with open("form_data.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerow(data)


def convert_checkbox(selected):
    """ 
    Convert user's selected choices into standard convention
    Easier for model to process.
    Return: list
    """
    checkboxes = ["L1", "L2", "L3", "L4", "L8", "L9", "N5", "N6", "N8", "T1", "T2", "T3","T5","T6"]
    result = []
    for i in checkboxes:
        if i in selected:
            result.append(1)
        else:
            result.append(0)
    return result

def convert_length(length:str):
    """ 
    Convert user's input into a standard convention
    Return: int
    """
    avg = 6.306049004594181
    if "tated" in length or "N" in length:
        return avg
    elif length.isdigit() or "." in length:
        return int(length)
    else:
        return int(re.findall(r'\d+', length)[0])


def convert_rent(rent:str):
    """ 
    Convert user's input into a standard convention
    Return: float
    """
    avg = 1595.9445741324917
    if "tated" in rent or "N" in rent:
        return avg
    else:
        return float(rent.lstrip("$").replace(",", ""))
    
def convert_rent_deposit(rent_deposit:str):
    """ 
    Convert user's input into a standard convention
    Return: float
    """
    avg = 1365.9816966067863
    if "tated" in rent_deposit or "N" in rent_deposit:
        return avg
    else:
        return float(rent_deposit.lstrip("$").replace(",", ""))
    
def convert_arrear_amount(arrear: str):
    """ 
    Convert user's input into a standard convention
    Return: float
    """
    avg = 5240.342916006339

    if "tated" in arrear or len(arrear) > 10:
        return avg
    else:
        return float(arrear.strip("$-.").replace(",", ""))

def convert_arrear_month(month: str):
    """ 
    Convert user's input into a standard convention
    Return: float
    """
    avg = 6.306049004594181

    if "ot" in month or "T" in month:
        return avg
    else:
        return float(month.strip(">"))
    

def calculate_probabilities():
    """ 
    Load the model from models, and calculate the probabilities for
    3 possible outcomes.
    return: dict
    """
    # loaded_model = joblib.load('stacking_model.sav')
    # Perform your calculations and get the probabilities
    probabilities = {
        'probability1': 0.8,
        'probability2': 0.5,
        'probability3': 0.3
    }
    return probabilities