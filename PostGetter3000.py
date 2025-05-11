import requests
import random

def main():
    # Генеруємо випадкове число від 1 до 100
    post_id = random.randint(1, 100)

    # Формуємо URL для API
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"

    try:
        # Робимо GET-запит
        response = requests.get(url)
        response.raise_for_status()  # Піднімає виняток, якщо статус не 200

        # Парсимо JSON
        data = response.json()

        # Виводимо потрібні поля
        print("ID:", data['id'])
        print("Title:", data['title'])
        print("Body:", data['body'])

    except requests.RequestException as e:
        print("Помилка при запиті до API:", e)

if __name__ == "__main__":
    main()