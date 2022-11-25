from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import numpy as np
from bdi_predict.ml_logic.registry import load_model
from bdi_predict.ml_logic.params import LOCAL_REGISTRY_PATH
from datetime import datetime
import pytz


app = FastAPI()

app.state.model = load_model()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/predict")
def predict(X1:float,
            X2:float,
            X3:float,
            X4:float,
            X5:float,
            X6:float,
            X7:float
):
    """
    Type hniting is used to indicate the datatypes expected for the parameters of the functino 
    FastAPI uses this info in order to hand errors to the developpers providing incompatible parameters.
    FastAPI also provides variables of the expected datatype to use without type hinting we need to manually convert the 
    parameters of the functions which are all recieved as strings.
    """
    
    X = [X1, X2, X3, X4, X5, X6, X7]
    X_pred = pd.DataFrame(X) 
    assert X_pred.shape == (7, 1)
    
    model = app.state.model
    
    y_pred = model.predict(X_pred)
    y_pred = float(y_pred[0])
    
    return {
        "BDI PREDICTION VALUE": y_pred
    }


@app.get("/")
def root():
    return {
    'greetings': 'Welcome the BDI prediction interface.'
}