from pydantic import BaseModel


class SentimentAnalysisRequest(BaseModel):
    sentence: str

    class Config:
        schema_extra = {
            "example": {
                "sentence": "Everyone is good"
            }
        }
