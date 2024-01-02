## See the [Frontend](https://github.com/PH-Tools/PH_View_React)

## Installation / Setup
1) `python3 -m venv .venv`
1) `source .venv/bin/activate`
1) `pip install -r requirements.txt`


## Run Locally in Dev Mode
1) `source .venv/bin/activate`
1) Make sure `origins = ["http://localhost:3000", ...]` is set in `main.py`
1) Run `uvicorn main:app --reload`

## Deployment to [Render.com](https://render.com/)
1) Make sure `origins = [..., "https://ph-tools.github.io"]` is set in `main.py`
1) Use the command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
1) Push to GitHub
1) Manually Deployment