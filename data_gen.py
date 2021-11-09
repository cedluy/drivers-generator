import json
import random
import pandas as pd
from faker import Faker
from pathlib import Path

SOURCE_FILE = Path(__file__).resolve()
SOURCE_DIR = SOURCE_FILE.parent

fichier = "drivers_data.json"

json_file = SOURCE_DIR / "drivers_data.json"
csv_file = SOURCE_DIR / "drivers_data.csv"

data_list = []

fake = Faker()

for _ in range(50):
    dico = {}

    id_beging_date = str(fake.date_between(start_date="-9y", end_date="now")).replace("-", "")
    id_exp_date = str(int(id_beging_date)+100000)

    birthday_date = str(fake.date_between(start_date="-65y", end_date="-18y")).replace("-", "")
    
    dico["driver.externalId"] = ""
    dico["driver.firstName"] = fake.first_name()
    dico["driver.lastName"] = fake.last_name()
    dico["driver.nonLatinFirstName"] = ""
    dico["driver.nonLatinLastName"] = ""
    dico["driver.dateOfBirth"] = birthday_date
    dico["driver.email"] = fake.free_email()
    dico["driver.license"] = fake.bothify(text="%%%%%%%%%%")
    dico["driver.cardNumber"] = fake.bothify(text="%%%%%%%%%%%%%%%%")
    dico["driver.idType"] = "ID"
    dico["driver.idDocumentNumber"] = fake.bothify(text="%%%%%%%%%%%%%%%%")
    dico["driver.idIssueDate"] = id_beging_date
    dico["driver.idExpirationDate"] = id_exp_date
    dico["driver.idIssuingCountry"] = fake.country_code()
    dico["driver.address"] = f"{fake.street_name()} {fake.street_suffix()} {random.randrange(1,99)}"
    dico["driver.postalCode"] = fake.postcode()
    dico["driver.city"] = fake.city()
    dico["driver.country"] = fake.country_code()
    dico["driver.contractStartDate"] = str(fake.date_between(start_date="-1y", end_date="now")).replace("-", "")
    dico["driver.contractApplicableLaw"] = "BE"

    data_list.append(dico)

with open(fichier, "w") as f:
    json.dump(data_list, f, indent=4)

df = pd.read_json (json_file)
df.to_csv (csv_file)