from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html

app = FastAPI()

@app.get("/")
async def index():
    return {"message": "Hello, Replit!"}

@app.get("/agents/")
async def create_agent(agent: str):
    return {"message": agent}

@app.get("/docs2", include_in_schema=False)
async def custom_swagger_ui_html_github():
    print("lol kek")
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=f"{app.title} - Fast UI", 
        swagger_ui_parameters={"syntaxHighlight.theme": "arta"}, # monokai arta
        swagger_css_url = "https://cdn.jsdelivr.net/gh/JaDenis/Fastapi-Swagger-UI-Dark/assets/swagger_ui_dark.min.css"
    )
