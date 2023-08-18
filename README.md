# api-broker-tg

### Запуск проекта

`docker compose up --build`  
`docker compose exec -u root web python manage.py createsuperuser` Создать суперпользователя если нужно

### Работа с приложением
1. Создаём пользователя `POST http://127.0.0.1:8000/auth/users/`  
    ```json
    {
        "username": "test",
        "password": "123"
    }
    ```

2. Получаем токен 
    `POST http://127.0.0.1:8000/auth/token/login/`
    ```json
    {
        "username": "test",
        "password": "123"
    }
    ```

3. Прописываем токен в Headers:
Пример `Authorization: Token 5b42a345845ad19c7fed952ba0e597f2da358470`

4. Получаем токен для Telegram бота `GET http://127.0.0.1:8000/api/tg/`

5. Переходим в бота https://t.me/apimesseger234_bot  
Запускаем  
Прописываем полученный токен. Пример: `/set_token nntwCVQq123glit8rssPaar123XGh4VejLGUcgr1235b5d8gPG`

6. Отправляем сообщение через API `POST http://127.0.0.1:8000/api/tg/`
    ```json
    {
        "text": "test123"
    }
    ```

7. Вывод всех сообщений отправленных через api пользователем `GET http://127.0.0.1:8000/api/msgs/`