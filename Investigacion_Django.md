# UNIVERSIDAD AMERICANA

**Asignatura:** Desarrollo de Aplicaciones Web I  
**Tema:** Investigación sobre la creación de endpoints en Django nativo mediante vistas basadas en clases (CBV)  
**Estudiante:** Rosaura León  
**Docente:** José Torres  
**Grupo:** 4E  
**Año:** 2026

---

# 1. Introducción

Django es un framework de desarrollo web escrito en Python que permite construir aplicaciones web de manera organizada, segura y eficiente. Entre sus funcionalidades se encuentra la posibilidad de crear endpoints, los cuales permiten establecer puntos de comunicación entre un cliente y un servidor mediante solicitudes HTTP.

En Django nativo es posible desarrollar endpoints sin utilizar librerías externas, aprovechando las herramientas que proporciona el propio framework, como las vistas basadas en clases, el sistema de enrutamiento y las respuestas HTTP.

En esta investigación se estudia cómo crear endpoints utilizando una vista basada en clase y cómo implementar los cuatro métodos HTTP principales: GET, POST, PUT y DELETE. También se explica la relación de estos métodos con las operaciones CRUD, el manejo de solicitudes y respuestas en formato JSON, la protección CSRF y los principales módulos, funciones y decoradores necesarios para desarrollar un endpoint básico.

# 2. Objetivos

## 2.1. Objetivo general

Investigar el funcionamiento y la creación de endpoints en Django nativo mediante vistas basadas en clases, comprendiendo la utilización de los métodos HTTP GET, POST, PUT y DELETE y su relación con las operaciones CRUD.

## 2.2. Objetivos específicos

- Comprender qué son las vistas basadas en clases y cuál es la función de la clase `View` en Django.
- Identificar el funcionamiento de los métodos `get()`, `post()`, `put()` y `delete()`.
- Relacionar los métodos HTTP con las operaciones de creación, consulta, actualización y eliminación de datos.
- Conocer las herramientas de Django para recibir solicitudes y generar respuestas en formato JSON.
- Identificar los módulos, funciones y decoradores utilizados para configurar endpoints.
- Comprender cómo se definen las rutas y cómo se capturan parámetros mediante el archivo `urls.py`.

# 3. Vistas basadas en clases (CBV) en Django

Las vistas basadas en clases, conocidas como Class-Based Views (CBV), son una forma de desarrollar la lógica de una aplicación web utilizando clases y métodos. Django permite utilizarlas para organizar las operaciones que se realizan cuando un usuario o cliente envía una solicitud HTTP.

A diferencia de las vistas basadas en funciones, donde la lógica se desarrolla dentro de una función, las vistas basadas en clases permiten separar el comportamiento de acuerdo con el método HTTP recibido.

## 3.1. Clase View

La clase `View` es una clase proporcionada por Django que sirve como base para crear vistas basadas en clases. Se importa desde `django.views`.

Ejemplo:

```python
from django.views import View

class ProyectoView(View):
    def get(self, request):
        pass

    def post(self, request):
        pass
```

En este ejemplo se crea una clase llamada `ProyectoView` que hereda de `View`. Dentro de ella se definen métodos que permiten responder a diferentes solicitudes HTTP.

## 3.2. Método as_view()

El método `as_view()` permite convertir una clase en una vista que Django pueda utilizar en el sistema de rutas.

Cuando llega una solicitud, este método crea una instancia de la clase y prepara su ejecución para atender la petición correspondiente.

Ejemplo:

```python
from django.urls import path
from .views import ProyectoView

urlpatterns = [
    path("proyectos/", ProyectoView.as_view()),
]
```

En este caso, `ProyectoView.as_view()` conecta la vista basada en clase con la ruta `/proyectos/`.

## 3.3. Método dispatch()

El método `dispatch()` se encarga de recibir la solicitud y dirigirla al método correspondiente según el tipo de petición HTTP.

Por ejemplo:

- Si recibe GET, ejecuta `get()`.
- Si recibe POST, ejecuta `post()`.
- Si recibe PUT, ejecuta `put()`.
- Si recibe DELETE, ejecuta `delete()`.

Si se recibe un método HTTP que la vista no tiene implementado, Django responde normalmente con el código de estado 405 (Method Not Allowed).

# 4. Métodos HTTP y operaciones CRUD

Los métodos HTTP permiten establecer qué operación desea realizar el cliente sobre los recursos del servidor. En el desarrollo de aplicaciones, estos métodos se relacionan con las operaciones CRUD.

CRUD corresponde a las palabras Create, Read, Update y Delete, que representan crear, consultar, actualizar y eliminar información.

| Método HTTP | Operación CRUD | Función |
|---|---|---|
| GET | Read (Consultar) | Permite obtener información del servidor. |
| POST | Create (Crear) | Permite enviar información para crear un nuevo registro. |
| PUT | Update (Actualizar) | Permite actualizar o reemplazar la información de un recurso. |
| DELETE | Delete (Eliminar) | Permite eliminar un recurso del servidor. |

## 4.1. Método GET

El método GET se utiliza para consultar información almacenada en el servidor. Generalmente se emplea para obtener todos los registros o consultar información específica.

Ejemplo:

```python
def get(self, request):
    proyectos = Project.objects.all()

    datos = []

    for proyecto in proyectos:
        datos.append({
            "id": proyecto.id,
            "name": proyecto.name,
            "description": proyecto.description,
            "start_date": proyecto.start_date
        })

    return JsonResponse(datos, safe=False)
```

En este ejemplo se consultan todos los proyectos almacenados y se organizan sus datos para devolverlos en formato JSON.

## 4.2. Método POST

El método POST permite enviar información al servidor para crear un nuevo registro en la base de datos.

Ejemplo:

```python
def post(self, request):
    datos = json.loads(request.body)

    proyecto = Project.objects.create(
        name=datos["name"],
        description=datos["description"],
        start_date=datos["start_date"]
    )

    return JsonResponse({
        "mensaje": "Proyecto creado correctamente",
        "id": proyecto.id
    }, status=201)
```

En este caso, los datos enviados por el cliente se reciben en formato JSON y se utilizan para crear un nuevo proyecto.

El código de estado 201 indica que el recurso fue creado correctamente.

## 4.3. Método PUT

El método PUT permite actualizar o reemplazar la información de un recurso existente. En este proyecto se utiliza para modificar los datos de un proyecto identificado mediante su ID.

Ejemplo:

```python
def put(self, request, pk):
    proyecto = Project.objects.get(pk=pk)
    datos = json.loads(request.body)

    proyecto.name = datos["name"]
    proyecto.description = datos["description"]
    proyecto.start_date = datos["start_date"]

    proyecto.save()

    return JsonResponse({
        "mensaje": "Proyecto actualizado correctamente"
    })
```

El parámetro `pk` identifica el proyecto que se desea modificar. Después de recibir los nuevos datos, se actualizan sus atributos y se guarda el cambio en la base de datos.

## 4.4. Método DELETE

El método DELETE permite eliminar un registro de la base de datos. Para realizar esta operación se utiliza el identificador del recurso.

Ejemplo:

```python
def delete(self, request, pk):
    proyecto = Project.objects.get(pk=pk)
    proyecto.delete()

    return JsonResponse({
        "mensaje": "Proyecto eliminado correctamente"
    })
```

En este ejemplo se busca el proyecto mediante su identificador y posteriormente se elimina.

**Nota:** Los métodos PUT y DELETE del proyecto también contemplan el manejo de registros inexistentes, devolviendo una respuesta con estado 404.

# 5. Manejo de solicitudes y respuestas JSON

En Django, las solicitudes HTTP se reciben mediante el objeto `request`, que contiene información enviada por el cliente. Para desarrollar endpoints que intercambian información en formato JSON, se utilizan herramientas del lenguaje Python y del propio framework.

## 5.1. request.body

El atributo `request.body` permite acceder al contenido original de una solicitud HTTP. Su información se recibe como una secuencia de bytes.

Cuando el cliente envía datos en formato JSON, estos pueden procesarse utilizando el módulo `json`.

Ejemplo:

```python
import json

datos = json.loads(request.body.decode("utf-8"))
```

Explicación:

- `request.body`: obtiene el contenido enviado por el cliente.
- `decode("utf-8")`: convierte los bytes en una cadena de texto.
- `json.loads()`: convierte el texto JSON en un objeto de Python, normalmente un diccionario.

## 5.2. Diferencia entre request.POST y request.body

`request.POST` se utiliza principalmente para acceder a los datos enviados mediante formularios HTML con codificaciones compatibles, como `application/x-www-form-urlencoded` o `multipart/form-data`.

Por otro lado, `request.body` permite acceder al contenido original de la solicitud, por lo que resulta útil cuando se reciben datos en formato JSON.

Es importante tener en cuenta que Django no proporciona un atributo `request.PUT` equivalente a `request.POST`. Para procesar datos JSON enviados mediante PUT, se puede utilizar `request.body`.

## 5.3. JsonResponse

`JsonResponse` es una clase proporcionada por Django que permite devolver respuestas HTTP en formato JSON.

Se importa desde `django.http`.

Ejemplo:

```python
from django.http import JsonResponse

return JsonResponse({
    "mensaje": "Proyecto creado correctamente"
}, status=201)
```

En este ejemplo se devuelve un mensaje en formato JSON y se establece el código de estado 201.

Cuando se necesita devolver una lista en lugar de un diccionario, se utiliza el parámetro `safe=False`.

Ejemplo:

```python
return JsonResponse(lista_proyectos, safe=False)
```

Esto permite enviar una lista de proyectos como respuesta al cliente.

# 6. Protección CSRF en Django

CSRF significa Cross-Site Request Forgery, que en español se conoce como falsificación de solicitudes entre sitios.

Es un tipo de ataque en el que un sitio malicioso intenta provocar que el navegador de un usuario autenticado realice una acción no deseada en otro sitio web.

Django incluye mecanismos de protección CSRF para ayudar a prevenir este tipo de ataques.

## 6.1. CsrfViewMiddleware

`CsrfViewMiddleware` es un middleware de Django encargado de aplicar la protección CSRF a las solicitudes que modifican información, según las reglas del framework.

Este mecanismo se encuentra habilitado normalmente en la configuración del proyecto dentro de `MIDDLEWARE`.

Su función es comprobar que las solicitudes protegidas incluyan un token CSRF válido.

## 6.2. Decorador csrf_exempt

El decorador `csrf_exempt` permite excluir una vista de la comprobación CSRF de Django.

Se importa desde:

```python
from django.views.decorators.csrf import csrf_exempt
```

Este decorador puede utilizarse en vistas que reciben solicitudes externas, pero debe emplearse con precaución porque desactiva esa protección para la vista correspondiente.

## 6.3. Decorador method_decorator

El decorador `method_decorator` permite aplicar decoradores diseñados para funciones a métodos de una clase.

Se importa desde:

```python
from django.utils.decorators import method_decorator
```

En las vistas basadas en clases puede utilizarse para aplicar `csrf_exempt` al método `dispatch`.

Ejemplo:

```python
@method_decorator(csrf_exempt, name="dispatch")
class ProyectoView(View):
    pass
```

De esta manera, la exclusión de la comprobación CSRF se aplica a la vista basada en clase.

**Importante:** desactivar CSRF no debe considerarse una solución general para aplicaciones en producción. Cuando se utiliza autenticación mediante cookies, es necesario mantener una protección adecuada.

# 7. Configuración de rutas mediante urls.py

El archivo `urls.py` permite definir las direcciones o rutas que utiliza Django para conectar las solicitudes del cliente con las vistas correspondientes.

Para configurar estas rutas se utiliza el módulo `django.urls`.

## 7.1. Función path()

La función `path()` permite definir una ruta y asociarla con una vista.

Ejemplo:

```python
from django.urls import path
from .views import ProyectoView

urlpatterns = [
    path("proyectos/", ProyectoView.as_view(), name="lista_proyectos"),
]
```

En este ejemplo, la ruta `proyectos/` se conecta con la clase `ProyectoView`.

## 7.2. Rutas con parámetros

Django permite capturar valores dentro de las rutas utilizando convertidores de URL.

Ejemplo:

```python
path(
    "proyectos/<int:pk>/",
    ProyectoView.as_view(),
    name="detalle_proyecto"
)
```

El convertidor `<int:pk>` permite recibir un número entero y almacenarlo en el parámetro `pk`.

Por ejemplo, si el cliente accede a `/proyectos/5/`, Django recibe el valor `5` como identificador del proyecto.

En el proyecto, esta ruta se utiliza para actualizar y eliminar proyectos mediante los métodos PUT y DELETE.

## 7.3. Función include()

La función `include()` permite incorporar las rutas de una aplicación dentro del archivo principal de rutas del proyecto.

Ejemplo:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("gestion.urls")),
]
```

En este caso, las rutas definidas en `gestion/urls.py` quedan disponibles bajo el prefijo `/api/`.

# 8. Principales módulos, funciones y decoradores utilizados

| Elemento | Módulo o ubicación | Función |
|---|---|---|
| `View` | `django.views` | Clase base para crear vistas basadas en clases. |
| `as_view()` | Clase `View` | Convierte una clase en una vista utilizable en las rutas. |
| `dispatch()` | Clase `View` | Dirige la solicitud al método HTTP correspondiente. |
| `get()` | Método de la vista | Atiende solicitudes GET. |
| `post()` | Método de la vista | Atiende solicitudes POST. |
| `put()` | Método de la vista | Atiende solicitudes PUT. |
| `delete()` | Método de la vista | Atiende solicitudes DELETE. |
| `JsonResponse` | `django.http` | Genera respuestas en formato JSON. |
| `HttpResponse` | `django.http` | Permite generar respuestas HTTP. |
| `HttpRequest` | `django.http` | Representa la solicitud HTTP recibida. |
| `request.body` | Objeto `HttpRequest` | Permite acceder al contenido original de la solicitud. |
| `request.method` | Objeto `HttpRequest` | Indica el método HTTP utilizado en la solicitud. |
| `path()` | `django.urls` | Define las rutas de la aplicación. |
| `include()` | `django.urls` | Incorpora rutas de otras aplicaciones. |
| `loads()` | Módulo `json` | Convierte una cadena JSON en un objeto de Python. |
| `csrf_exempt` | `django.views.decorators.csrf` | Excluye una vista de la comprobación CSRF. |
| `method_decorator` | `django.utils.decorators` | Aplica decoradores a métodos de una clase. |
| `CsrfViewMiddleware` | `django.middleware.csrf` | Aplica la protección CSRF de Django. |

# 9. Implementación de endpoints en el proyecto

Para desarrollar los endpoints en Django nativo se utilizan principalmente los archivos `models.py`, `views.py` y `urls.py`.

Cada archivo cumple una función específica dentro de la aplicación.

## 9.1. Archivo models.py

El archivo `models.py` permite definir los modelos que representan las tablas de la base de datos.

En este proyecto se crearon los modelos `Project` y `Task`.

El modelo `Project` contiene los campos:

- `name`: almacena el nombre del proyecto.
- `description`: almacena la descripción.
- `start_date`: almacena la fecha de inicio.

El modelo `Task` contiene los campos:

- `title`: almacena el título de la tarea.
- `completed`: indica si la tarea está completada.
- `project`: establece la relación con el proyecto mediante una llave foránea.

## 9.2. Archivo views.py

El archivo `views.py` contiene la lógica que permite atender las solicitudes HTTP.

En el proyecto se utiliza una vista basada en clase llamada `ProjectView`, que hereda de `View`.

Esta clase implementa los métodos:

- `get()`: consulta los proyectos.
- `post()`: crea nuevos proyectos.
- `put()`: actualiza proyectos existentes.
- `delete()`: elimina proyectos.

También utiliza `JsonResponse` para devolver información al cliente en formato JSON y maneja errores cuando los datos enviados no son válidos o cuando un proyecto no existe.

## 9.3. Archivo urls.py

El archivo `gestion/urls.py` define las rutas que permiten acceder a los endpoints.

Ejemplo:

```python
from django.urls import path
from .views import ProjectView

urlpatterns = [
    path("proyectos/", ProjectView.as_view(), name="lista_proyectos"),
    path("proyectos/<int:pk>/", ProjectView.as_view(), name="detalle_proyecto"),
]
```

Por otra parte, el archivo principal `myPrimerApp/urls.py` utiliza `include()` para incorporar las rutas de la aplicación `gestion` bajo el prefijo `/api/`.

De esta manera, los endpoints quedan organizados y disponibles mediante las direcciones correspondientes.

# 10. Conclusión

La creación de endpoints en Django nativo mediante vistas basadas en clases permite desarrollar aplicaciones web de manera organizada, aprovechando las herramientas que proporciona el propio framework.

A través de esta investigación se comprendió la función de la clase `View`, el funcionamiento de los métodos HTTP GET, POST, PUT y DELETE y su relación con las operaciones CRUD.

También se identificó la importancia del manejo de solicitudes y respuestas JSON, la configuración de rutas mediante `urls.py` y los mecanismos de protección CSRF.

Finalmente, la implementación de estos conceptos permitió comprender cómo se establece la comunicación entre un cliente y un servidor, así como la manera en que Django facilita la creación y administración de endpoints sin depender necesariamente de librerías externas.

# 11. Referencias bibliográficas

Django Software Foundation. (s. f.). *Base views*. Django documentation. https://docs.djangoproject.com/en/6.1/ref/class-based-views/base/

Django Software Foundation. (s. f.). *Request and response objects*. Django documentation. https://docs.djangoproject.com/en/6.1/ref/request-response/

Django Software Foundation. (s. f.). *URL dispatcher*. Django documentation. https://docs.djangoproject.com/en/6.1/topics/http/urls/

Django Software Foundation. (s. f.). *Cross Site Request Forgery protection*. Django documentation. https://docs.djangoproject.com/en/6.1/ref/csrf/

Mozilla. (s. f.). *Métodos de petición HTTP*. MDN Web Docs. https://developer.mozilla.org/es/docs/Web/HTTP/Reference/Methods