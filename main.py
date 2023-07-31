from fastapi import FastAPI

app=FastAPI()

@app.get('/api/v1')
def FastAPI():
    return {'status':'ok 👍 '}

# To run the app using python main.py
if __name__ == "__main__":
    port = int(8000)

    app_module = "main:app"
    uvicorn.run(app_module, host="0.0.0.0", port=port, reload=True)