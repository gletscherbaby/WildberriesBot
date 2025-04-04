# Функция для получения неотвеченных отзывов с оценкой 4 и 5
def get_unanswered_reviews(token):
    url = "https://feedbacks-api.wildberries.ru/api/v1/feedbacks"
    
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    
    params = {
        "state": "new"  # Только новые (неотвеченные) отзывы
    }

    response = requests.get(url, headers=headers, params=params)
    
    print(f"Ответ от сервера: {response.text}")  # Выводим полный ответ сервера
    
    if response.status_code == 200:
        reviews_data = response.json()["data"]["feedbacks"]
        
        positive_reviews = [
            {
                "id": review["id"],
                "text": review["text"]
            }
            for review in reviews_data if review["productValuation"] >= 4 and review["answer"] is None
        ]
        
        return positive_reviews
    else:
        print(f"Ошибка при запросе данных: {response.status_code}")
        return []
