import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from .sentiment_analyzer import SentimentAnalyzer
from .request_body import SentimentAnalysisRequest
from .response_body import SentimentAnalysisResponse

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080"
]


HEADERS = {'Content-type': 'application/json', 'Accept': 'text/plain'}


def fastapi_app():
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get('/')
    def server_is_up():
        return 'server is up'

    @app.post('/analyze', response_model=SentimentAnalysisResponse)
    def post_sentiment_analysis(request_body: SentimentAnalysisRequest):
      result = SentimentAnalyzer(request_body.sentence).analyze()
      response = SentimentAnalysisResponse(result=result)
      return response

    return app


app = fastapi_app()

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8081)
