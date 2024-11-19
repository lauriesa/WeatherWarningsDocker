from dataHandler import *

import uvicorn
from fastapi import FastAPI

app = FastAPI()

data = readData()
alerts = parseXML("weather_alerts.xml")

@app.get("/")
def central_function():
    return alerts

if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")




showAlerts(alerts)