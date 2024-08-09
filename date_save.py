import json

# 파일 생성 함수
def save_recent_meals(file_name='recent_meals.json'):
    with open(file_name, 'w') as file:
        json.dump(recent_meals, file)

# 파일 읽는 함수
def load_recent_meals(file_name='recent_meals.json'):
    global recent_meals
    with open(file_name, 'r') as file:
        recent_meals = json.load(file)

# 예제 사용
save_recent_meals()
load_recent_meals()
print(recent_meals)
