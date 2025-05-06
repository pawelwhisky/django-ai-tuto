from django.http import JsonResponse
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_sentiment(request):
    text = request.GET.get("text", "")
    if not text:
        return JsonResponse({"error": "No text provided"}, status=400)

    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(text)

    return JsonResponse({
        "text": text,
        "sentiment": score
    })
