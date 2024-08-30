from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/fish")
def fish(length: float, weight: float):
    """
    물고기의 길이와 무게를 받아 길이와 무게를 보여줌

    Args:
        prediction (str) : 물고기의 종류
        length (float) : 물고기의 길이(cm)
        weight (float) : 물고기의 무게(g)

    Returns:
        dict : 물고기의 정보를 담은 딕셔너리
    """
    if length > 30.0:
        prediction = "도미"
    else:
        prediction = "빙어"

    return {
            "prediction":   prediction,
            "length"    :   length, 
            "weight"    :   weight}


