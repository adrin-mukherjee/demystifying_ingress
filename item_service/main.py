import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get('/products/{product_id}')
def get_product_by_id(product_id: int):
    return {
            "id": product_id,
            "product_name": f"product_{product_id}",
            "type": "electronics",
            "desc": "quintessential electronics",
        }


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=9091, reload=True)
