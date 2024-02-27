# calculator
requirements:

1. docker
2. docker-compose
   
how to use:

1. remove ".example" from env filename
2. In main folder run command:
docker-compose build
3. run migration
docker-compose run backend python manage.py migrate
4. When build is done run by command:
docker-compose up
5. To use the application, enter into your browser
http://localhost:8080/

