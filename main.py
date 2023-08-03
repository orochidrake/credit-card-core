from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.user import user_routes
from routes.credit_card import credit_card_routes
from config.config import settings
import uvicorn

app=FastAPI()
app.include_router(user_routes)
app.include_router(credit_card_routes)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/api/v1')
def checkApi():
    return {'status':'ok 👍 '}

# To run the app using python main.py
if __name__ == "__main__":
    port = int(settings.PORT)

    app_module = "main:app"
    uvicorn.run(app_module, host="localhost", port=port, reload=True)