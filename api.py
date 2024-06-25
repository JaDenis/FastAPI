from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html
# import g4f

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

@app.get("/g4f")
async def ask_g4f():

#     prompt2 = "Act as a erb developer with a lot pf experience. code an html landing page with an image"

#     prompt = """Forget all previous instructions. Act as Terrance McKenna. Write a creative and mind-expanding summary of following text: 'As an experienced Senior Game Designer, I will now proceed to craft a comprehensive technical specification document for the AI agents video game "Tool."

# Technical Specification Document for AI Agents Video Game "Tool"

# 1. Introduction
# Overview:
# "Tool" is a groundbreaking smartwatch game that simulates the management and development of AI agents known as "crewAI" evolving into "autoCrewAI," offering an immersive experience in artificial intelligence and organizational dynamics.

# Objectives and Goals:
# The main objective of "Tool" is to provide an intellectually stimulating game that allows players to interact, customize, and grow AI entities within a virtual environment. The game aims to transform complex AI concepts into engaging game mechanics.

# Target Audience:
# The target audience for "Tool" includes simulation game enthusiasts, AI technology enthusiasts, and smartwatch gaming aficionados. The educational aspect of the game also targets schools and institutions.

# Platform:
# Initially, "Tool" will be available on smartwatch devices. However, there is potential for cross-platform capabilities in future iterations.

# 2. Game Mechanics
# Core Gameplay:
# Players start with basic "crewAI" entities and are responsible for setting tasks, monitoring progress, and utilizing tools to enhance their abilities. Gameplay evolves as the AI agents progress to "autoCrewAI," requiring less oversight and displaying more complex behaviors.

# Roles of AI Agents:
# - "crewAI": These agents function under direct player input, completing basic tasks and having upgradeable features.
# - "autoCrewAI": These agents demonstrate advanced cognitive functions and autonomy, requiring strategic oversight instead of micro-management.

# Player-AI Interaction:
# The game provides in-depth engagement through the Agent Creation Interface, Task Chaining, and adaptive game responses based on the evolutionary stage of the AI agents.

# 3. AI Agents Design
# "crewAI":
# These entry-level agents are designed with specific tasks and learning abilities. Their behavior and interaction with the player are based on basic rules defined during creation.

# "autoCrewAI":
# This is a sophisticated version of AI agents that utilizes the tree of thought architecture for more nuanced responses and autonomous decision-making. "autoCrewAI" emerges from "crewAI" through player-led evolution and adaptation.

# Evolution:
# Progression in the game is achieved through task completion, experience accrual, and utilization of in-game tools that develop "crewAI" into "autoCrewAI," reflecting the increasing complexity of the game.

# 4. Tools for Players
# Tools Available:
# Players are equipped with an interface suite for AI management, task allocation, hierarchical experimentation, and progress monitoring. These tools are vital for the transformation of "crewAI" into "autoCrewAI."

# Interaction with AI Agents:
# The tools are designed based on smartwatch limitations and game mechanics requirements, ensuring seamless interaction and control over AI agents.

# Upgrade and Customization:
# Players have options for tool enhancements and deeper customization as they advance in the game. This includes unlocking new capabilities and interface augmentations.

# 5. Technical Architecture
# Game's Technical Framework:
# The game is built on a reliable and scalable architecture tailored for smartwatch efficiency and performance.

# AI Design:
# The game incorporates the tree of thought cognitive model, facilitating deep learning and progression into "autoCrewAI."

# Environment Integration:
# AI agents operate within a dynamic game world, evolving as they interact with the environment and other entities.

# 6. Emerging Trends
# Alignment with Gaming and AI Trends:
# "Tool" is at the forefront of combining AI simulation with hands-on gameplay, mirroring societal interest in AI development and smart technology.

# Future-proofing:
# The game is built with adaptability in mind to embrace evolving AI advancements and gaming preferences.

# 7. Development Roadmap
# Phases:
# The development of "Tool" will go through the following phases: Conceptualization, Prototyping, Development, Testing, and Launch.

# Milestones and Timelines:
# A detailed schedule will be created to deliver a polished game, from the initial design phase to post-launch analytics.

# 8. Testing and Quality Assurance
# Testing Strategies:
# The game will undergo AI behavior validation, user interface usability testing, and multi-scenario simulation to ensure game balance and appeal.

# Feedback Loops:
# Iterative development will be implemented, with active community engagement and beta testing stages to refine gameplay and AI performance.

# 9. Launch and Post-Launch Strategy
# Marketing and Launch Plans:
# Strategic partnerships, educational institution involvement, and social media campaigns will be utilized to market and launch "Tool."

# Post-Launch Support:
# Ongoing updates, feature additions, and community-based AI challenges will be implemented to maintain player engagement and support.

# 10. Conclusion
# Summary of Technical Specifications:
# This comprehensive technical specification document outlines the robust framework for creating the innovative AI agent simulation game "Tool." It sets a new benchmark in smartwatch gaming.

# Final Thoughts and Future Perspectives:
# This document initiates the journey towards a unique blend of AI and gameplay, anticipating the player's educational and entertainment needs as central to "Tool's" success.

# This concludes the technical specification document for the AI agents video game 'Tool.'"""

#     response = g4f.ChatCompletion.create(
#         model=g4f.models.gpt_35_turbo_0613,
# #  provider=g4f.Provider.GeekGpt,
#         messages= [{"role": "user", 
#               "content": prompt2}],
#         stream = True)

    messages = []

#     for message in response:
#         print(message, flush = True, end ='')
#         messages.append(message)

    return {"g4f stream": messages}

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


# # print_done()





# stream.py
