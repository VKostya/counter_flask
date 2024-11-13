# Использование Docker в приложении Flask с БД  
Данное приложение обладает следующим функционалом:
- при переходе на стартовую страницу добавляет запись с датой обращения и user-agent
- при переходе на /count выводит счетчик обращений
- при переходе на /list отображает **все** обращения
## Деплой  
Для деплоя приложения небходимо 
- скачать содержимое данного репозитория
- поменять переменные среды в файле docker-compose.yml (*необязательный шаг*)
- обновить файл db.py, если на предыдущем шаге менялись параметры  
- выполнить команду `docker-compose up`
После деплоя на localhost:8765 будет доступно flask приложение, а на localhost:5050 pgAdmin для администрирования базой данных
## Тестирование
Приложение было протестировано локально и на [https://labs.play-with-docker.com/#](https://labs.play-with-docker.com/#) 
![image](https://github.com/user-attachments/assets/a29cc52b-be17-48e4-9847-5fb854ea087d)
при деплое на  [https://labs.play-with-docker.com/#](https://labs.play-with-docker.com/#)  возникла ошибка, из-за которой не получалось зарезолвить имя db, но получалось подключиться напрямую по ip-адресу
