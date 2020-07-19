from pydantic import BaseModel


class SentimentAnalysisResponse(BaseModel):
    result: list

    class Config:
        schema_extra = {
            "example": {
                "result": [{"box": [164, 67, 151, 200], "confidence":0.9954631924629211, "keypoints":{"left_eye": [
                    199, 147], "right_eye":[271, 147], "nose":[233, 195], "mouth_left":[204, 220], "mouth_right":[267, 219]}}]
            }
        }
