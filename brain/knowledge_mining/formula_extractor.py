import re

def extract_formulas(text):

    formulas=re.findall(r"\bRSI\b|\bEMA\b|\bMACD\b",text)

    return formulas
