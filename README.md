# Cactugram

Este proyecto trata de una sencilla aplicación web desarrollada con Django, en la cual puedes registrar cactus y puedes crear una galería para cada uno de ellos. 

### Algunas caracteristicas principales: 
- Realizar las operaciones básicas sobre cada uno de los modelos (Crear, Editar, Listar, Eliminar)
- Subir Fotografías 
- Visualizar la galería de fotografías de cada cactus
- Realizar busqueda de cactus por nombre y nombre científico

- Modelo BD
![bd](https://user-images.githubusercontent.com/71096926/108020043-84bd6580-6fe9-11eb-8436-21ea6cce78ac.jpg)

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
- Home
![listar_cactus](https://user-images.githubusercontent.com/71096926/108020058-871fbf80-6fe9-11eb-83dc-12edcaa63cd6.jpg)

- Registrar Cactus
![registrar_cactus](https://user-images.githubusercontent.com/71096926/108020063-88e98300-6fe9-11eb-99d8-9456525e6cad.jpg)

- Actualizar Cactus
![actualizar_cactus](https://user-images.githubusercontent.com/71096926/108020030-8129de80-6fe9-11eb-94ba-b7e9f5f8205f.jpg)

- Eliminar Cactus
![eliminar_cactus](https://user-images.githubusercontent.com/71096926/108020050-8555fc00-6fe9-11eb-9692-fe6ed5278d39.jpg)

- Actualizar Cactus
![actualizar_foto_cactus](https://user-images.githubusercontent.com/71096926/108020034-825b0b80-6fe9-11eb-9da7-5e2fd44703c5.jpg)

- Galería Cactus
![registro_fotografico](https://user-images.githubusercontent.com/71096926/108020067-8ab34680-6fe9-11eb-8af8-942e0d8ac27d.jpg)

- Registrar Foto Cactus
![registrar_foto_cactus](https://user-images.githubusercontent.com/71096926/108020065-8a1ab000-6fe9-11eb-8940-d3279293014f.jpg)

- Fotografía Cactus
![eliminar_fotografia_cactus](https://user-images.githubusercontent.com/71096926/108020055-86872900-6fe9-11eb-9c47-0b4ee04fc68b.jpg)

- No hay fotografías en la galería del cactus
![no_hay_registro_fotografico](https://user-images.githubusercontent.com/71096926/108020061-8850ec80-6fe9-11eb-8962-076724beb78b.jpg)
