from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html

app = FastAPI(swagger_ui_parameters={"swagger_css_url"})

@app.get("/")
async def index():
    return {"message": "Hello, Replit!"}

@app.get("/agents/")
async def create_agent(agent: str):
    return {"message": agent}

@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html_github():
    return get_swagger_ui_html(
        openapi_url = app.openapi_url,
        title=f"{app.title} - Swagger UI",
        swagger_css_url = "https://raw.githubusercontent.com/JaDenis/Fastapi-Swagger-UI-Dark/main/assets/swagger_ui_dark.min.css"
    )
