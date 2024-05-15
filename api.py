from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html

app = FastAPI()

@app.get("/")
async def landing_page():
    return {"AutoPro API": "version 0.1.0"}

@app.get("/users")
async def create_a_user(user: str):
    return {"Created user": user}

@app.post("/items")
def create_an_item(item: dict):
    return {"item": item}

@app.post("/steam")
def get_steam_achievements(steam_token: str, steam_user_id: int):
    return {"steam_token": steam_token,
            "steam_user_id": steam_user_id}

@app.get("/api", include_in_schema=False)
async def dark_swagger_ui():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=f"AutoPro API", 
        swagger_ui_parameters={"syntaxHighlight.theme": "arta", "defaultModelsExpandDepth": -1, "persistAuthorization": True}, # monokai arta
        swagger_css_url = "https://cdn.jsdelivr.net/gh/Madrobotz/Fastapi-Swagger-UI-Dark2/assets/swagger_ui_dark.min.css"
    )

    # For more swagger_ui_parameters visit: https://springdoc.org/properties.html#_swagger_ui_properties