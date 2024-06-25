from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html

app = FastAPI()

# create a websocket online game
# - 1. socket.io integration
# - 2. trading/crafting shader logic
# - 3. call provider APIs with requests
# - 4. ensure deployment to Railway
#
# create a next.js ui components pack
# - 1. pick best components from Magic UI, Aceternity, daisyUI, NextUI
# - 2. establish minimalistic easy-to-use architecture
# - 3. ensure deployment to Railway
# - 4. develop main Coding Dashboard
# - 5.

@app.get("/")
async def landing_page():
    return {"NxtAI API": "version 0.1.0"}

@app.get("/users")
async def create_a_user(user: str):
    return {"Created user": user}

@app.post("/task/create")
async def create_task(task: str):
    return "created task"

task = "AITask"
@app.get("/task/{task}")
async def get_task(task: str):
    return {"socket message": task}

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
        title=f"ARtifactVault API", 
        swagger_ui_parameters={"syntaxHighlight.theme": "arta", "defaultModelsExpandDepth": -1, "persistAuthorization": True}, # monokai arta
        swagger_css_url = "https://cdn.jsdelivr.net/gh/Madrobotz/Fastapi-Swagger-UI-Dark2/assets/swagger_ui_dark.min.css")

    # For more swagger_ui_parameters 
    # visit: https://springdoc.org/properties.html#_swagger_ui_properties


# from fastapi.staticfiles import StaticFiles
# @app.get("/", tags=["swaggerui"], include_in_schema=False)
# async def get_documentation():
#      return get_swagger_ui_html(
#         openapi_url="/swaggerfile",
#         title="docs",
#         # swagger_js_url="https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/3.34.0/swagger-ui-bundle.min.js",
#         swagger_js_url="/static/js/swagger-ui-bundle.min.js",
#         swagger_css_url="/static/css/swagger-ui.css",
#     )