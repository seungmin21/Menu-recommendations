import random

all_menus = ['김치찌개', '비빔밥', '된장찌개', '불고기', '냉면', '쌀국수', '초밥']

def recommend_menu():
    available_menus = [menu for menu in all_menus if menu not in recent_meals]
    return random.choice(available_menus) if available_menus else '모든 메뉴를 최근에 드셨습니다.';

recommended_menu = recommend_menu()
print(f'추천 메뉴: {recommended_menu}')