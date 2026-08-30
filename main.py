from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html lang="ms">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>BP AI Music Studio</title>
        <style>
            body {
                background-color: #0b0f19;
                color: #ffffff;
                font-family: 'Montserrat', sans-serif;
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
            <h2>BP AI Music Studio</h2>
            <p>Pelayan sedang aktif dan berjalan dengan lancar!</p>
        </div>
    </body>
    </html>
    """
    
