from global_intelligence.knowledge_reader import read_knowledge
from global_intelligence.intelligence_analyzer import analyze_knowledge
from global_intelligence.prediction_engine import predict_market


def global_intelligence():

    db = read_knowledge()

    intelligence_score = analyze_knowledge(db)

    prediction = predict_market()

    return {

        "intelligence_score":intelligence_score,
        "market_prediction":prediction

    }
