#app.py

from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def hello_world():
    
    return {"message": "Hello,World"}

@app.get("/result/{score}")
async def result_exam(score):
    score = int(score)
    if(score >= 50):
        result = "Pass"
    else:    
        result = "No pass"

    return {"your result is": result}

@app.get("/bmi")
async def bmi(weight: float, height: float):
    bmi = weight/(height/100)**2
    
    return str(bmi)
    
// เวลาเรียกใช้  .../bmi?weight=55&height=165

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)
