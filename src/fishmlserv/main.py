from typing import Union
from fastapi import FastAPI
from sklearn.neighbors import KNeighborsClassifier
from fishmlserv.model.manager import get_model_path
import os
import pickle

app = FastAPI()
with open(get_model_path(), "rb") as f:
    fish_model = pickle.load(f)


@app.get("/")
def read_root():
    return {"Hello": "world"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/fish")
def fish(length: float, weight:float):
    """
    물고기의 종류 판별기

    Args:
        length (float): 물고기 길이(cm)
        weight (float): 물고기 무게(g)

    Returns:
        dict: 물고기 종류를 담은 딕셔너리
    """
    ### 모델 불러오기
    #with open("/home/whitecapella/code/fishmlserv/note/model.pkl", "rb") as f:
    #    fish_model = pickle.load(f)

    #prediction = fish_model.predict([[length, weight]])

    fish_class = "모름"
    #if prediction[0] == 1:
    #   fish_class = "도미"
    #else:
    #   fish_class = "빙어"

    return {
                "prediction": fish_class,
                "length": length, 
                "weight": weight
            }

@app.get("/prediction")
def pre(qlength: float, qweight:float):
    """
    물고기 예측기

   c955b6dba9e3 Args:
        length (float): 물고기 길이(cm)
        weight (float): 물고기 무게(g)

    Returns:
        dict: 물고기 종류를 담은 딕셔너리
    """
    #bream_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0, 31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0, 35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0]
    #bream_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0, 500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0, 700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0]

    #smelt_length = [9.8, 10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
    #smelt_weight = [6.7, 7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]
    fish_class = "모름"
    #length = bream_length + smelt_length
    #weight = bream_weight + smelt_weight
    kn = KNeighborsClassifier()

    #fish_data = []
    #fish_target = []
    #for l, w in zip(length,weight):
    #    fish_data.append([l,w])

    #fish_target = [1] * 35 + [0] * 14
    #kn.fit(fish_data, fish_target)
    
    q = fish_model.predict([[qlength, qweight]])
    if q == 1:
        fish_class = "do-mi"
    else:
        fish_class = "bing-er"

    return {
                "prediction": fish_class,
                "length": qlength,
                "weight": qweight
            }


pre(45.4, 415.7)
