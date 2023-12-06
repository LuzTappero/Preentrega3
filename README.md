# TERCERA PRE ENTREGA

#Configuración inicial del proyecto

0. Instalar `django`:  `pip install django`
1. Crear carpeta para nuestro repositorio, yo elegí nombrarla: "MIPROYECTOFINAL.PY"
2. dentro de esa carpeta: `django-admin startproject MIPROYECTOFINAL`. Este comando dejará creada una nueva carpeta `MIPROYECTOFINAL`

3. Dentro de la carpeta `proyecto-final-47790/MIPROYECTOFINAL/MIPROYECTOFINAL` corri el comando `python manage.py startapp Home` y a continuación realice lo mismo para las aplicaciones Products y Store.
es decir mi aplicación contiene la Aplicacion de MIPROYECTOFINAL donde se encuentra el archivo Settings en el cual se guardan las aplicaciones creadas, y las url generales.

#Configurar apps

## APP Home:
Se encuentra la siguiente URL:
1. path ('', views.Home, name='home'), la cual lleva a la página principal del proyecto.

En teplates de Home se encuentra el siguiente template:
1. index.html que posee el contenido de la pagina principal(Home)
2. navbar.html que posee el contenido de la barra de navegación que es común a las tres pestañas
3. footer.html que posee el contenido de la barra de navegación que es común a las tres pestañas

En la carpeta Static de Home se encuentran todos los archivos estaticos provenientes de CSS que le dan el estilo a la página.

## APP Product:
En esta aplicación están desarrollados los 3 modelos solicitados para esta consigna y los formularios correspondientes; allí se encuentra: 
- la clase 'Producto'
- la clase 'Comentario' y
- la clase 'CategoriaProducto'

Hay formularios para crear nuevos datos a las clases de PRODUCTO, COMENTARIO Y CATEGORIAPRODUCTO; 
Hay formulario de busqueda para interaccionar con la base de datos con las clases PRODUCTO Y COMENTARIO. 

En la seccion de url de la app 'Product' se encuentran las siguientes:
 
##
1. path ('Products/', views.Products, name='Products')---->Vista principal de la pestaña PRODUCTS
2. path ('Products/crear/', views.crear_productos, name="crear_productos") ----> Formulario para crear productos
3. path ('Products/buscar/', views.buscar_productos , name="buscar_productos")----> Formulario para buscar productos
4. path ('Products/crearComentario/', views.crear_comentario , name= "crear_comentario")---->Formulario para crear comentarios o reseñas
5. path ('Products/buscarComentario/', views.buscar_comentario, name="buscar_comentario")----> Formulario para buscar comentarios o reseñas
6. path ('Products/crearCategorias/', views.crear_categoria_producto, name="crear_categoria")----> Formulario para crear categorias de productos

## Configurar forms
En el archivo forms.py se encuentran los formularios previamente nombrados; tanto de creación de datos como de búsqueda;

En el archivo views se encuentran desarrolladas las vistas que luego, se podran ver a través del servidor.

En el archivo templates/Products se encuentran los siguientes archivos:
1. products.html: Es el que le da el diseño principal a la página; tiene heredado el navbar.html desde la App de Home; que permite navegar gracias a los botones entre las tres pestañas, y también hereda desde el Home el footer que es común a las tres pestañas(Home/Product/Store).

2. formulario-crear-producto.html
3. busqueda-producto-formulario.html
4. productos_list.html 
- Estos tres archivos (2.3.4) son necesarios para la creacion de formularios de la clase 'Producto' tanto para insertar datos, como de busquedas; los mismos tienen un 'block y endblock' con el contenido necesario para el formulario y esta insertado en el template original de producto.

5. crear-comentario-formulario.html
6. buscar_comentario_formulario.html
7. comentarios-list.html
De la misma manera que la anterior; estos archivos son utiles para la insersión de datos y busqueda en BD de la clase 'Comentario'

8. crear-categorias-formulario.html ; el mismo sirve para la insersión de datos al formulario de la clase 'CategoriaProductos'

## APP Store
Por ultimo se encuentra la App Store; en la misma se encuentra la siguiente URL
- path ('Store/', views.Store, name='Store'),

En templates
1. Store.html : se encuentra el template principal de ésta pestaña la cual tiene heredado el navbar que permite navegar gracias a los botones entre las tres pestañas y también hereda desde Home el footer que es común a las tres pestañas(Home/Product/Store).