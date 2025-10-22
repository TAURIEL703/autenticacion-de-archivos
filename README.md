# Proyecto de Autenticación API – GRC Ciberseguridad

Este proyecto demuestra dos métodos de autenticación:
1. **API Key** usando FastAPI.
2. **JWT (JSON Web Token)** usando Flask.

## Estructura
- `autenticacion_api.py`: API protegida por API Key.
- `jwt_flask.py`: Generación y verificación de tokens JWT.
- `requirements.txt`: Dependencias necesarias.

## Ejecución
```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar API Key
uvicorn autenticacion_api:app --reload

# Ejecutar JWT
python jwt_flask.py
