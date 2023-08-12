import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get('/users/{user_id}')
def get_user_by_id(user_id: int):
    return {
            "id": user_id,
            "name": f"user_{user_id}",
            "type": "service_user"
        }


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8081, reload=True)
