# Vulcano


## Requerimientos
-----------------------------------------------
* psql (PostgreSQL) 12.4
* Python 3.8
-----------------------------------------------
* Django==3.1.2
* django-cors-headers==3.5.0
* django-model-utils==4.0.0
* djangorestframework==3.12.1
* httpcore==0.12.0
* imutils==0.5.3
* opencv-python==4.4.0.44
* Pillow==8.0.1
* psycopg2-binary==2.8.6

## Instalación
1. Clone el proyecto
2. Dentro del directorio **vulcan-be** cree el entorno virtual usando virtualenv:
    ```commandline
    vulcan-be$ virtualenv -p python3.8 env
    ```
3. Active el entorno virtual:
    ```commandline
    vulcan-be$ source env/bin/activate
    ```
4. Instale las librerías y paquetes requeridos:
    ```commandline
    vulcan-be$ pip3 install -r requirements.txt
    ```
5. Configure los datos de la base de datos, cambie estos por los de su base de datos.
Se encuentran en la ruta **vulcan-be/hefesto_be/fire/settings.py** la variable **DATABASES**. 

6. Ejecute las migraciones del proyecto:
    ```commandline
    vulcan-be$ python3 manage.py migrate
    ```
7. Ejecute el proyecto:
    ```commandline
    vulcan-be$ python3 manage.py runserver
    ```
   
## Utiles para despliegue con Heroku
https://codigofacilito.com/articulos/deploy-django-heroku
https://stackoverflow.com/questions/49469764/how-to-use-opencv-with-heroku
https://stackoverflow.com/questions/55330749/error-while-running-python-manage-py-collectstatic-noinput-after-changin
