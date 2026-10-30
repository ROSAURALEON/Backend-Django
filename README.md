# Proyecto Backend Django

## UNIVERSIDAD AMERICANA

**Asignatura:** Desarrollo de Aplicaciones Web I  
**Tema:** Creación de endpoints en Django nativo mediante vistas basadas en clases (CBV)  
**Estudiante:** Rosaura León  
**Docente:** José Torres  
**Grupo:** 4E  
**Año:** 2026

---

## 1. Descripción del proyecto

Este proyecto consiste en desarrollar una aplicación web utilizando Django nativo y vistas basadas en clases (CBV), con el propósito de crear endpoints que permitan realizar operaciones sobre los datos de los proyectos.

La aplicación utiliza los métodos HTTP GET, POST, PUT y DELETE para consultar, crear, actualizar y eliminar registros, mediante solicitudes y respuestas en formato JSON.

## 2. Objetivo

Desarrollar endpoints en Django nativo mediante vistas basadas en clases, aplicando los métodos HTTP y las operaciones CRUD para gestionar información de proyectos.

## 3. Tecnologías utilizadas

- Python.
- Django.
- SQLite.
- Visual Studio Code.
- JSON.
- HTTP.

## 4. Modelos de la aplicación

La aplicación cuenta con dos modelos principales:

- **Project:** almacena el nombre, la descripción y la fecha de inicio de cada proyecto.
- **Task:** almacena el título, el estado de finalización y el proyecto al que pertenece cada tarea.

## 5. Endpoints implementados

| Método HTTP | Ruta | Función |
|---|---|---|
| GET | `/api/proyectos/` | Consultar todos los proyectos. |
| POST | `/api/proyectos/` | Crear un proyecto. |
| PUT | `/api/proyectos/<id>/` | Actualizar un proyecto. |
| DELETE | `/api/proyectos/<id>/` | Eliminar un proyecto. |

**Nota:** Los endpoints implementados corresponden al modelo `Project`. El modelo `Task` está definido, pero todavía no cuenta con endpoints propios.

## 6. Estructura del proyecto

Los archivos principales son:

- `gestion/models.py`: contiene los modelos Project y Task.
- `gestion/views.py`: contiene la lógica de los endpoints.
- `gestion/urls.py`: define las rutas de la aplicación.
- `myPrimerApp/urls.py`: incorpora las rutas de la aplicación al proyecto.
- `myPrimerApp/settings.py`: contiene la configuración de Django.
- `gestion/migrations/`: contiene las migraciones de la base de datos.

## 7. Investigación

La investigación académica completa sobre la creación de endpoints en Django nativo mediante vistas basadas en clases se encuentra en el siguiente documento:

[Consultar investigación completa](Investigacion_Django.md)

## 8. Cómo ejecutar el proyecto

1. Tener Python instalado.
2. Abrir una terminal en la carpeta del proyecto.
3. Crear y activar un entorno virtual si todavía no existe.
4. Instalar Django:

   ```bash
   pip install django
   ```

5. Ejecutar las migraciones:

   ```bash
   python manage.py migrate
   ```

6. Iniciar el servidor:

   ```bash
   python manage.py runserver
   ```

7. Consultar los proyectos desde la siguiente dirección:

   `http://127.0.0.1:8000/api/proyectos/`

## 9. Conclusión

El desarrollo de este proyecto permitió comprender cómo crear endpoints en Django nativo mediante vistas basadas en clases, aplicar los métodos HTTP y realizar operaciones CRUD. También permitió conocer la importancia de los modelos, las rutas, las solicitudes y las respuestas JSON en el desarrollo de aplicaciones web.