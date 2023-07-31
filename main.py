from fastapi import FastAPI

app=FastAPI()

@app.get('/api/v1')
def FastAPI():
    return {'status':'ok 👍 '}