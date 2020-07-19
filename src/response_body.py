from pydantic import BaseModel


class SentimentAnalysisResponse(BaseModel):
    result: dict

    class Config:
        schema_extra = {
            "example": {
                "result": {
                    "result": {
                        "neg": 0,
                        "neu": 0.408,
                        "pos": 0.592,
                        "compound": 0.4404
                    }
                }
            }
        }
