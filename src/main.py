import uvicorn
from fastapi import FastAPI
from src.config import middleware
from src.routers import sentiment_analysis_router

app = FastAPI()

def fastapi_app():
    middleware.config(app)

    @app.get('/')
    def server_is_up():
        return 'server is up'

    app.include_router(sentiment_analysis_router.router)

    return app


app = fastapi_app()

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8081)
