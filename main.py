import os
from typing import List, Tuple
import json

try:
    from dotenv import load_dotenv

    load_dotenv()
except Exception as e:
    print(e)

from requests.exceptions import HTTPError
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import HTTPException
from pyairtable import Api
from pyairtable.api.types import RecordDict

# AirTable Database ID data
AIRTABLE_BASE_IDS = {
    "proj_2242": {
        "app": "app2huKgwyKrnMRbp",
        "summary": "tblb8D5jcw1KyB522",
        "config": "tblOPg6rOq7Uy2zJT",
        "cert_results": "tblh7tTM2RJkt4zF1",
        "materials": "tblaqehqmP6xfOPUP",
        "window_unit_types": "tbln2qVrxqSNlAJOK",
        "frame_types": "tblJm0uhhChDY0jKQ",
        "glazing_types": "tblbreMnmdsKDCYTN",
        "appliances": "tblgk5pneolD192Dv",
        "lighting": "tblRH6A9tLyKGsUD0",
        "fans": "tblCwWhH3YuNV34ec",
        "pumps": "tbl3F59OhLXcgaWm0",
        "erv_units": "tblQtcVgB6iYbyhis",
    },
    "proj_2305": {
        "app": "app64a1JuYVBs7Z1m",
        "summary": "tblapLjAFgm7RIllz",
        "config": "tblRMar5uK7mDZ8yM",
        "cert_results": "tbluEAhlFEuhfuE5v",
        "materials": "tblkWxg3xXMjzjO32",
        "window_unit_types": "tblGOpIen7MnCuQRe",
        "frame_types": "tblejOjMq62zdRT3D",
        "glazing_types": "tbl3JAeRMqiloWQ65",
        "appliances": "tblqfzzcqc3o2IcD4",
        "lighting": "tblkLN5vn6fcXnTRT",
        "fans": "tbldbadmmNca7E1Nr",
        "pumps": "tbliRO0hZim8oQ2qw",
        "erv_units": "tblkIaP1TspndVI5f",
    },
}


def get_airtable_ids(project_id: str, table_name: str) -> Tuple[str, str]:
    """
    Return the Airtable base-id and table name for a given project number.

    Args:
    * project_id: The project number (ie: "proj_2242")
    * table_name: The name of the table to return (ie: "cert_results")

    Returns:
    * base_id: The AirTable 'base-id' for the project (ie: "app2...bp").
    * table_name: The AirTable 'table-name' for the project (ie: "tblC...ec").
    """

    app_id = AIRTABLE_BASE_IDS[project_id]["app"]
    table_name = AIRTABLE_BASE_IDS[project_id][table_name]
    return app_id, table_name


app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000",
    "https://ph-tools.github.io",
    "https://bldgtyp.github.io",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/{project_id}/summary")
def get_summary(project_id: str) -> List[RecordDict]:
    api = Api(os.environ["PH_VIEW_GET"])
    try:
        table = api.table(*get_airtable_ids(project_id, "summary"))
    except HTTPError as e:
        raise HTTPException(
            status_code=400,
            detail=f"Error occurred while fetching data for project: {project_id}/summary\n{e}",
        )
    data = table.all()
    return data


@app.get("/{project_id}/config")
def get_config(project_id: str) -> List[RecordDict]:
    api = Api(os.environ["PH_VIEW_GET"])
    table = api.table(*get_airtable_ids(project_id, "config"))
    data = table.all()
    return data


@app.get("/{project_id}/cert_results")
def get_certification_results(project_id: str) -> List[RecordDict]:
    api = Api(os.environ["PH_VIEW_GET"])
    table = api.table(*get_airtable_ids(project_id, "cert_results"))
    data = table.all()
    return data


@app.get("/{project_id}/materials")
def get_materials(project_id: str) -> List[RecordDict]:
    api = Api(os.environ["PH_VIEW_GET"])
    table = api.table(*get_airtable_ids(project_id, "materials"))
    data = table.all()
    return data


@app.get("/{project_id}/window_unit_types")
def get_window_unit_types(project_id: str) -> List[RecordDict]:
    api = Api(os.environ["PH_VIEW_GET"])
    table = api.table(*get_airtable_ids(project_id, "window_unit_types"))
    data = table.all()
    return data


@app.get("/{project_id}/frame_types")
def get_frame_types(project_id: str) -> List[RecordDict]:
    api = Api(os.environ["PH_VIEW_GET"])
    table = api.table(*get_airtable_ids(project_id, "frame_types"))
    data = table.all()
    return data


@app.get("/{project_id}/glazing_types")
def get_glazing_types(project_id: str) -> List[RecordDict]:
    api = Api(os.environ["PH_VIEW_GET"])
    table = api.table(*get_airtable_ids(project_id, "glazing_types"))
    data = table.all()
    return data


@app.get("/{project_id}/appliances")
def get_appliances(project_id: str) -> List[RecordDict]:
    api = Api(os.environ["PH_VIEW_GET"])
    table = api.table(*get_airtable_ids(project_id, "appliances"))
    data = table.all()
    return data


@app.get("/{project_id}/lighting")
def get_lighting(project_id: str) -> List[RecordDict]:
    api = Api(os.environ["PH_VIEW_GET"])
    table = api.table(*get_airtable_ids(project_id, "lighting"))
    data = table.all()
    return data


@app.get("/{project_id}/fans")
def get_fans(project_id: str) -> List[RecordDict]:
    api = Api(os.environ["PH_VIEW_GET"])
    table = api.table(*get_airtable_ids(project_id, "fans"))
    data = table.all()
    return data


@app.get("/{project_id}/pumps")
def get_pumps(project_id: str) -> List[RecordDict]:
    api = Api(os.environ["PH_VIEW_GET"])
    table = api.table(*get_airtable_ids(project_id, "pumps"))
    data = table.all()
    return data


@app.get("/{project_id}/erv_units")
def get_erv_units(project_id: str) -> List[RecordDict]:
    api = Api(os.environ["PH_VIEW_GET"])
    table = api.table(*get_airtable_ids(project_id, "erv_units"))
    data = table.all()

    # -- Temp for testing only --
    # WRITE:
    # with open("data.json", "w") as f:
    #     json.dump(data, f)

    # READ:
    # with open("data.json") as f:
    #     data = json.load(f)

    return data


@app.get("/{project_id}/", tags=["root"])
async def read_root(project_id: str) -> dict:
    return {"message": "root"}
