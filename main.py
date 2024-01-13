import os
from typing import List

try:
    from dotenv import load_dotenv

    load_dotenv()
except Exception as e:
    print(e)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pyairtable import Api
from pyairtable.api.types import RecordDict

AIRTABLE_APP = "app2huKgwyKrnMRbp"

app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000",
    "https://ph-tools.github.io",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
import json


@app.get("/cert_results")
def get_certification_results() -> List[RecordDict]:
    api = Api(os.environ["AIRTABLE_ARVERNE_GET_POST"])
    table = api.table(AIRTABLE_APP, "tblh7tTM2RJkt4zF1")
    data = table.all()
    return data


@app.get("/materials")
def get_materials() -> List[RecordDict]:
    api = Api(os.environ["AIRTABLE_ARVERNE_GET_POST"])
    table = api.table(AIRTABLE_APP, "tblaqehqmP6xfOPUP")
    data = table.all()
    return data


@app.get("/window_unit_types")
def get_window_unit_types() -> List[RecordDict]:
    api = Api(os.environ["AIRTABLE_ARVERNE_GET_POST"])
    table = api.table(AIRTABLE_APP, "tbln2qVrxqSNlAJOK")
    data = table.all()
    return data


@app.get("/frame_types")
def get_frame_types() -> List[RecordDict]:
    api = Api(os.environ["AIRTABLE_ARVERNE_GET_POST"])
    table = api.table(AIRTABLE_APP, "tblJm0uhhChDY0jKQ")
    data = table.all()
    return data


@app.get("/glazing_types")
def get_glazing_types() -> List[RecordDict]:
    api = Api(os.environ["AIRTABLE_ARVERNE_GET_POST"])
    table = api.table(AIRTABLE_APP, "tblbreMnmdsKDCYTN")
    data = table.all()
    return data


@app.get("/appliances")
def get_appliances() -> List[RecordDict]:
    api = Api(os.environ["AIRTABLE_ARVERNE_GET_POST"])
    table = api.table(AIRTABLE_APP, "tblgk5pneolD192Dv")
    data = table.all()
    return data


@app.get("/lighting")
def get_lighting() -> List[RecordDict]:
    api = Api(os.environ["AIRTABLE_ARVERNE_GET_POST"])
    table = api.table(AIRTABLE_APP, "tblRH6A9tLyKGsUD0")
    data = table.all()
    return data


@app.get("/fans")
def get_fans() -> List[RecordDict]:
    api = Api(os.environ["AIRTABLE_ARVERNE_GET_POST"])
    table = api.table(AIRTABLE_APP, "tblCwWhH3YuNV34ec")
    data = table.all()
    return data


@app.get("/pumps")
def get_pumps() -> List[RecordDict]:
    api = Api(os.environ["AIRTABLE_ARVERNE_GET_POST"])
    table = api.table(AIRTABLE_APP, "tbl3F59OhLXcgaWm0")
    data = table.all()
    return data


@app.get("/erv_units")
def get_erv_units() -> List[RecordDict]:
    api = Api(os.environ["AIRTABLE_ARVERNE_GET_POST"])
    table = api.table(AIRTABLE_APP, "tblQtcVgB6iYbyhis")
    data = table.all()

    # -- Temp for testing only --
    # WRITE:
    # with open("data.json", "w") as f:
    #     json.dump(data, f)

    # READ:
    # with open("data.json") as f:
    #     data = json.load(f)

    return data


@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": str(os.environ["AIRTABLE_ARVERNE_GET_POST"])}
