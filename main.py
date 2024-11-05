from fastapi import FastAPI

from core.configs import settings

from api.v1.api import api_router


app = FastAPI(title='Cursos API - FastAPI SQL Alchemy')
app.include_router(api_router, prefix=settings.API_V1_STR)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", 
                host="0.0.0.0", 
                port=8000, 
                log_level='debug', 
                reload=True)
    
"""
token eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNzX3Rva2VuIiwiZXhwIjoxNzMxNDA5NzE2LCJpYXQiOjE3MzA4MDQ5MTYsInN1YiI6IjEifQ.fS0IxwW2sKGXV0wOjSJe_G6c4bZxw9x0VDQnY5xRyvU
tipo: Bearer
"""