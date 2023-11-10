
# env
`pip install virtualenv`
#### create the env
    `python -m env `
#### Activate the envirnonment
source env/Scripts/activate

#### install requirements
pip install -r requirements.txt

# Run
uvicorn main:app --reload
uvicorn main:app  --reload --host 0.0.0.0 --port 8000

# API Documentation:
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/redoc