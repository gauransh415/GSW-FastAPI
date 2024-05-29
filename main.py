from fastapi import FastAPI, Path

app = FastAPI()

info = {
   1:{ "name":"Gauransh",
    "health": "low",
    "efficiency": "high"    
  }
}
@app.get("/")
def index():
    return {"message": "Hanji,good morning"}

@app.get("/get-info/{info_id}")
def get_info(info_id: int=Path(None,description="The ID of the info one wants to view")):
    return info[info_id]
