# Laluan untuk halaman utama (index.html)
@app.get("/", response_class=HTMLResponse)
def read_index(request: Request):
    return templates.TemplateResponse(request, "index.html")

# Laluan untuk halaman kesan bunyi (effects.html)
@app.get("/effects", response_class=HTMLResponse)
def read_effects(request: Request):
    return templates.TemplateResponse(request, "effects.html")

# Laluan untuk halaman keputusan (result.html)
@app.get("/result", response_class=HTMLResponse)
def read_result(request: Request):
    return templates.TemplateResponse(request, "result.html")

# Laluan untuk halaman studio AI (studioai.html)
@app.get("/studioai", response_class=HTMLResponse)
def read_studioai(request: Request):
    return templates.TemplateResponse(request, "studioai.html")
    
