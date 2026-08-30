from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>BP AI Music Production</title>
        <style>
            body {
                background-color: #0f172a;
                color: #f8fafc;
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
        </style>
    </head>
    <body>
        <div style="text-align: center;">
            <h1>BP AI Music Production</h1>
            <p>Sistem backend berjalan dengan lancar!</p>
        </div>
    </body>
    </html>
    """
```eof

Fail `main.py` di atas menggunakan kerangka FastAPI yang bersih dan memastikan sebarang kod CSS diletakkan di dalam *string* Python yang betul agar tidak mencetuskan ralat sintaks. Sila kemas kini fail `main.py` anda di GitHub dengan kod ini.
