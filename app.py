#app.py

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='')



@app.get('/')
def hello_world():
    
    return {"message": "Hello,World"}


@app.get('/formget.html', response_class=HTMLResponse)
def main(request: Request):
    return templates.TemplateResponse('formget.html', {'request': request})

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
    
# เวลาเรียกใช้  .../bmi?weight=55&height=165


@app.get("/add")
async def add(a: int, b: int):
    return {"sum": a+b}


@app.get("/mul")
async def mul(a, b):
    return int(a) * int(b)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)
