from fastapi import FastAPI
from routes.user import user_routes
from config.config import settings
import uvicorn

app=FastAPI()
app.include_router(user_routes)

@app.get('/api/v1')
def checkApi():
    return {'status':'ok 👍 '}

# To run the app using python main.py
if __name__ == "__main__":
    port = int(settings.PORT)

    app_module = "main:app"
    uvicorn.run(app_module, host="0.0.0.0", port=port, reload=True)