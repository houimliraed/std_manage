from fastapi import FastAPI


app = FastAPI()

students = {
    1:{
    "name":"Raed",
    "age":"Houimli",
    "class":"testing",
    }

}


@app.get("/")
def index():
    return {"name" : "first data"}

@app.get("/get_student/{student_id}")
def get_student(student_id : int):
    return students[student_id]["name"]
    