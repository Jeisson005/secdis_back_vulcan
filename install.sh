#!/bin/bash

echo -e "\n\nInstalación del proyecto\n\n"
echo "Recuerde haber configurado las credenciales de la base de datos en el script settings.py
ubicado en la ruta vulcan-be/hefesto_be/fire/settings.py, la variable: DATABASES"
read -p "Si ya configuro las credenciales de la base de datos presione enter para continuar"

py3_v=$(python3 -V)
py38_v=$(python3.8 -V)
psql_v=$(psql -V)
flag=false

echo -e "\n\nVerificando que tenga PostgreSQL"
if [[ "$psql_v" == *"psql (PostgreSQL)"* ]]; then
    echo -e "\n\nVerificando que exista la versión de python3.8"
    if [[ "$py3_v" == *"Python 3.8"* ]]; then
        echo -e "\n\nCreando entorno virutal con virtualenv y python3 -> python3.8  ..."
        virtualenv -p python3 env
        flag=true
    elif [[ "$py38_v" == *"Python 3.8"* ]]; then
        echo -e "\n\nCreando entorno virutal con virtualenv y python3.8 ..."
        virtualenv -p python3.8 env
        flag=true
    fi

    if [ "$flag" = true ]; then
      echo -e "\n\nActivando entorno virtual ..."
      source env/bin/activate
      echo -e "\n\nInstalando librerías y paquetes requeridos ..."
      pip3 install -r requirements.txt

      echo -e "\n\nRecuerde haber configurado las credenciales de la base de datos en el script settings.py
      ubicado en la ruta vulcan-be/hefesto_be/fire/settings.py, la variable: DATABASES"
      read -p "Si ya configuro las credenciales de la base de datos presione enter para continuar"

      echo -e "\n\nCreando/validando migraciones"
      python3 manage.py makemigrations
      echo -e "\n\nEjecutando las migraciones en la base de datos"
      python3 manage.py migrate

      echo -e "\n\nEjecutando el proyecto"
      python3 manage.py runserver
    else
      echo -e "\n\nNo se pudo instalar el entorno virtual"
    fi
else
    echo -e "\n\nNo cuenta con PostgreSQL instalado."
fi