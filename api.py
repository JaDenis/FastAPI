from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html

app = FastAPI()

@app.get("/")
async def index():
    return {"message": "Hello, Replit!"}

@app.get("/agents/")
async def create_agent(agent: str):
    return {"message": agent}

@app.get("/api", include_in_schema=False)
async def dark_swagger_ui():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=f"{app.title} - Fast UI", 
        swagger_ui_parameters={"syntaxHighlight.theme": "arta", "defaultModelsExpandDepth": -1, "persistAuthorization": True}, # monokai arta
        swagger_css_url = "https://cdn.jsdelivr.net/gh/Madrobotz/Fastapi-Swagger-UI-Dark/assets/swagger_ui_dark.min.css"
    )

    # For more swagger_ui_parameters visit: https://springdoc.org/properties.html#_swagger_ui_properties

    # TODO: Edit css for components and host css on a new github account to fork from there
    # loading animation
    # button.opblock-control-arrow
    # .copy-to-clipboard button
    # select.content-type
    # input
