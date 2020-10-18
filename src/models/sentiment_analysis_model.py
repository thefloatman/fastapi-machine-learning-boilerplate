from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


class SentimentAnalysisModel:
	def __init__(self, sentence):
		self.sentence = sentence

	def analyze(self):
		analyser = SentimentIntensityAnalyzer()
		score = analyser.polarity_scores(self.sentence)
		
		return score
