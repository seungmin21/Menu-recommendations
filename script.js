let recentMeals = [];
const allMenus = ['김치찌개', '비빔밥', '된장찌개', '불고기', '냉면', '쌀국수', '초밥'];

document.addEventListener('DOMContentLoaded', (event) => {
    loadRecentMeals();
    displayRecentMeals();
});

function addRecentMeal() {
    const newMealInput = document.getElementById('new-meal');
    const newMeal = newMealInput.value;
    if (newMeal) {
        if (recentMeals.length >= 3) {
            recentMeals.shift();  // 가장 오래된 기록을 삭제합니다.
        }
        recentMeals.push(newMeal);
        saveRecentMeals();
        displayRecentMeals();
        newMealInput.value = '';
    }
}

function displayRecentMeals() {
    const recentMealsList = document.getElementById('recent-meals-list');
    recentMealsList.innerHTML = '';
    recentMeals.forEach(meal => {
        const listItem = document.createElement('li');
        listItem.textContent = meal;
        recentMealsList.appendChild(listItem);
    });
}

function recommendMenu() {
    const availableMenus = allMenus.filter(menu => !recentMeals.includes(menu));
    const recommendedMenu = availableMenus.length > 0 ? availableMenus[Math.floor(Math.random() * availableMenus.length)] : '모든 메뉴를 최근에 드셨습니다!';
    document.getElementById('recommended-menu').textContent = `추천 메뉴: ${recommendedMenu}`;
}

function saveRecentMeals() {
    localStorage.setItem('recentMeals', JSON.stringify(recentMeals));
}

function loadRecentMeals() {
    const savedMeals = localStorage.getItem('recentMeals');
    if (savedMeals) {
        recentMeals = JSON.parse(savedMeals);
    }
}
