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


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)
