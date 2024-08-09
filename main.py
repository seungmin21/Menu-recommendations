import json
import random

recent_meals = []

def add_recent_meal(meal):
    if len(recent_meals) >= 3:
        recent_meals.pop(0)  # 가장 오래된 기록을 삭제합니다.
    recent_meals.append(meal)

# 파일 생성
def save_recent_meals(file_name='recent_meals.json'):
    with open(file_name, 'w') as file:
        json.dump(recent_meals, file)

#  생성 파일 읽기
def load_recent_meals(file_name='recent_meals.json'):
    global recent_meals
    with open(file_name, 'r') as file:
        recent_meals = json.load(file)

def recommend_menu():
    all_menus = ['참치캔', '비빔밥', '컵라면', '봉지라면', '냉면', '물 말은 밥', '계란말이', '버섯볶음', '라면스프계란찜', '치즈밥', '파스타']
    available_menus = [menu for menu in all_menus if menu not in recent_meals]
    return random.choice(available_menus) if available_menus else '모든 메뉴를 최근에 드셨습니다!'

# 데이터 로드
try:
    load_recent_meals()
except FileNotFoundError:
    pass

# 최근 먹은 음식 추가
add_recent_meal('물 말은 밥에 반찬')
add_recent_meal('아이스아메리카노')
add_recent_meal('스팸볶음')

# 추천 메뉴 출력
recommended_menu = recommend_menu()
print(f'추천 메뉴: {recommended_menu}')

# 데이터 저장
save_recent_meals()
