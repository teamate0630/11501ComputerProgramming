score = [60,70,80]

settings = {"multiplier": 1.1, "bonus": 5}

def analyze_scores(*scores, **options):
    """
    分析學生分數。

    Parameters:
        *scores: 接收不定數量的分數
        **options: 接收選擇性設定，例如 multiplier 和 bonus

    Returns:
        一個字典，包含調整後的分數、平方、總分及平均分數。
    """
    multiplier = options.get("multiplier", 1.1)
    bonus = options.get("bonus", 5)

    adjusted = [
        score * multiplier + bonus
        for score in scores
    ]

    squared = [
        score ** 2
        for score in adjusted
    ]

    total = sum(adjusted)
    average = total / len(adjusted) if adjusted else 0

    return {
        "adjusted_scores": adjusted,
        "squared_scores": squared,
        "total": total,
        "average": average
    }
    
result = analyze_scores(*score, **settings)
print(result)