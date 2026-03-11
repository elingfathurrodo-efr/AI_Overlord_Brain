from global_knowledge.web_scanner import scan_url
from global_knowledge.knowledge_parser import parse_html
from global_knowledge.knowledge_filter import filter_trading_knowledge
from global_knowledge.knowledge_storage import load_knowledge,save_knowledge


def learn_from_web(url):

    html = scan_url(url)

    if html is None:
        return None

    text = parse_html(html)

    if not filter_trading_knowledge(text):
        return None

    knowledge = load_knowledge()

    knowledge.append({

        "source":url,
        "content":text[:500]

    })

    save_knowledge(knowledge)

    return "knowledge_saved"
