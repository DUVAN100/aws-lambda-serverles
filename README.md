# Título del proyecto

Descripción corta del proyecto

## Requisitos previos

Antes de comenzar, asegúrate de tener los siguientes requisitos:

- Node.js y npm instalados en tu sistema
- Una cuenta de AWS con credenciales de acceso (access key y secret key)

## Instalación

Para instalar las dependencias del proyecto, ejecuta el siguiente comando:

## Configuración de AWS

Para configurar tus credenciales de AWS, ejecuta el siguiente comando en tu terminal:


Asegúrate de reemplazar "<tu_access_key>" y "<tu_secret_key>" con tus credenciales de acceso reales de AWS.

## Configuración del servicio

Antes de desplegar tu función Lambda en AWS, asegúrate de configurar correctamente tu servicio en el archivo `serverless.yml`. Este archivo contiene la configuración de tu servicio, incluyendo el nombre del servicio, la región de AWS, las funciones Lambda que contiene y los eventos que activan estas funciones.

## Despliegue

Para desplegar tu servicio en AWS, ejecuta el siguiente comando:


Serverless Framework desplegará tu servicio en AWS y te dará una URL que puedes usar para invocar tus funciones Lambda.

## Invocación

Para invocar tus funciones Lambda, puedes usar la URL que Serverless Framework te dio después de desplegar tu servicio. También puedes usar la herramienta de línea de comandos `awscli` para invocar tus funciones.

## Eliminación

Para eliminar tu servicio de AWS, ejecuta el siguiente comando:


Serverless Framework eliminará todas las funciones Lambda y los recursos asociados a tu servicio en AWS.

## Contribución

Si deseas contribuir a este proyecto, haz lo siguiente:

1. Haz un fork del repositorio
2. Crea una rama con el nombre de tu nueva función o característica (`git checkout -b nombre-de-tu-rama`)
3. Haz tus cambios
4. Haz un commit con tus cambios (`git commit -am "Descripción de tus cambios"`)
5. Haz push de tus cambios a tu repositorio (`git push origin nombre-de-tu-rama`)
6. Crea un pull request en GitHub

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

# Instalacion de docker
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
# URL install docker
# https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04
# Instalación
npm install -g serverless
npm install --save-dev serverless-python-requirements

# Instalar plugin para uso de step functions AWS
npm install --save-dev serverless-step-functions

# Configuración
serverless config credentials --provider aws --key <ACCESS_KEY> --secret <SECRET_KEY>

# Crear un nuevo servicio de Serverless
serverless create --template aws-python3 --path my-service
cd my-service

# Crear una nueva función Lambda
serverless create function --function <NOMBRE_DE_LA_FUNCION> --handler handler.<NOMBRE_DE_LA_FUNCION>

# Editar la función Lambda
# Editar el archivo handler.py en la carpeta de la función Lambda para agregar el código de la función

# Desplegar el servicio
serverless deploy

# Verificar información del servicio desplegado
serverless info