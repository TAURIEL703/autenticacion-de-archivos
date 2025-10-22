from fastapi import FastAPI, Header, HTTPException

app = FastAPI()

API_KEY = "clave123"

@app.get("/")
def home():
    return {"message": "Bienvenido a la API"}

@app.get("/data")
def get_data(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="API Key inválida")
    return {"status": "autenticado", "data": "Acceso concedido a los datos protegidos"}
