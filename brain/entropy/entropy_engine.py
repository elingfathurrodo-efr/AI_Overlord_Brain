def calculate_entropy(known,unknown):

    total = known + unknown

    if total == 0:
        return 0

    entropy = unknown / total

    return round(entropy,2)
