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


@app.get("/fans")
def get_fans() -> List[RecordDict]:
    api = Api(os.environ["AIRTABLE_ARVERNE_GET_POST"])
    table = api.table("app2huKgwyKrnMRbp", "tblCwWhH3YuNV34ec")
    data = table.all()
    return data


@app.get("/erv_units")
def get_erv_units() -> List[RecordDict]:
    api = Api(os.environ["AIRTABLE_ARVERNE_GET_POST"])
    table = api.table("app2huKgwyKrnMRbp", "tblQtcVgB6iYbyhis")
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
