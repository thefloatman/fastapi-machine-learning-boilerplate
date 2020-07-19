from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


class SentimentAnalyzer:
	def __init__(self, sentence):
		self.sentence = sentence

	def detect(self):
		analyser = SentimentIntensityAnalyzer()
    score = analyser.polarity_scores(sentence)
    
		return score
