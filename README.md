`api_hotel_web` - назва контейнеру з бекендом, потрібно замінити на актуальну для свого середовища
щоб дізнатися актуальну - `docker ps -a | grep api_hotel_web`


щоб глянути логи - `docker logs -f --tail 100 api_hotel_web`

щоб перезапустити бекенд - `docker restart api_hotel_web`

коли змінюється файл requirements.txt - `docker build --rm -t api-hotels .`

запуск проекту - `docker-compose up -d`

ПЕРЕД ПЕРШИМ ВИКОРИСТАННЯМ ВИКОНАТИ НАСТУПНІ КОМАНДИ

`docker exec -it api_hotel_web_1 bash` - зайти в контейнер бекенду

`python manage.py migrate` - запуск міграцій в конейнері

`python manage.py createsuperuser` - створення адміна, потрібно виконати наступні інструкції