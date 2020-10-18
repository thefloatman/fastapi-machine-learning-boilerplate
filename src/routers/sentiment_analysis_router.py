from fastapi import APIRouter
from src.models.sentiment_analysis_model import SentimentAnalysisModel
from src.interfaces.requests.sentiment_analysis_request import SentimentAnalysisRequest
from src.interfaces.responses.sentiment_analysis_response import SentimentAnalysisResponse

router = APIRouter()

@router.post('/analyze', response_model=SentimentAnalysisResponse)
def post_sentiment_analysis(request_body: SentimentAnalysisRequest):
  result = SentimentAnalysisModel(request_body.sentence).analyze()
  response = SentimentAnalysisResponse(result=result)
  return response
