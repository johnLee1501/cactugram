# Cactugram

Este proyecto trata de una sencilla aplicación web desarrollada con Django, en la cual puedes registrar cactus y puedes crear una galería para cada uno de ellos. 

### Algunas caracteristicas principales: 
- Realizar las operaciones básicas sobre cada uno de los modelos (Crear, Editar, Listar, Eliminar)
- Subir Fotografías 
- Visualizar la galería de fotografías de cada cactus
- Realizar busqueda de cactus por nombre y nombre científico



## Getting Started

Estas instrucciones te proporcionarán una copia del proyecto en funcionamiento en tu máquina local con fines de desarrollo y prueba.

### Prerrequisito

Si quieres probar, necesitarás estos requisitos previos

```
Python > 3.6
```

### Instalación

Primero, clona el proyecto en tu computadora

```
git clone https://github.com/johnLee1501/cactugram.git
```

luego, cree un entorno virtual para el proyecto, puede usar virtualenvwrapper-win si su sistema operativo es Windows

```
pip install virtualenvwrapper-win
mkvirtualenv <nombre_del_entorno>
```

después de eso, instala los paquetes en requirements.txt para asegurarte de tener todo lo necesario

```
pip install -r requirements.txt
```

finalmente configura tu servidor de base de datos Mysql, puedes hacerlo fácilmente utilizando laragon si tu sistema operativo es Windows. Ten en cuenta la siguiente configuración de settings.py, puedes modificarla de ser necesario
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cactugram',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
por último realiza las migraciones de tu modelo a la base de datos.
```
py manage.py makemigrations
py manage.py migrate
```

Listo! ya puedes ejecutarlo

```
py manage.py runserver
```


## Autor

* **John Vega**

## Screenshots
