from fastapi import FastAPI, WebSocket, WebSocketDisconnect
app = FastAPI()

class SocketManager:
    def __init__(self):
        self.sockets: list[WebSocket] = []
    
    async def connect(self, socket: WebSocket):
        await socket.accept()
        self.sockets.append(socket)

    def disconnect(self, socket: WebSocket):
        self.sockets.remove(socket)

    async def send_personal_message(self, message: str, socket: WebSocket):
        await socket.send_text(message)

    async def broadcast(self, message: str):
        for socket in self.sockets:
            await socket.send_text(message)

manager = SocketManager()

@app.get("/")
async def index():
    return {"message": "Hello, Vercel!"}

@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: id):
    await manager.connect(websocket)
    try: 
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(f"You sent: {data}", websocket)
            await manager.broadcast(f"Client #{client_id} sent: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} has left")



