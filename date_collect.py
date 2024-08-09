recent_meals = []

def add_recent_meal(meal):
    if len(recent_meals) >= 10:
        recent_meals.pop(0)  # 가장 오래된 기록을 삭제합니다.
    recent_meals.append(meal)

add_recent_meal('오므라이스')
add_recent_meal('비빔밥')
add_recent_meal('된장찌개')
add_recent_meal('김치찌개')
print(recent_meals)
