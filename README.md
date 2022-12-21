# Vision_artificial_GUI

Interfaz gráfica que utiliza un módulo de visión artificial para detectar manos en tiempo real a través de una webcam. Elige entre las diferentes opciones haciendo gestos con las manos

En este proyecto utilizaremos una heladería como ejemplo para crear un módulo de visión artificial que tramita sus pedidos escaneando en tiempo real los gestos que realiza el cliente con las manos. 

Cuando el cliente hace el gesto correspondiente a cualquiera de las 3 opciones, se genera una elipse alrededor de la opción seleccionada que representa el tiempo de confirmación, cuando la elipse se completa la opción se selecciona y la interfaz acctualiza de pantalla


|Seleccionar opción 1|Seleccionar opción 3|Seleccionar opción 2|
|:-:|:-:|:-:|
|![1](https://user-images.githubusercontent.com/110389988/208942986-de25bd39-d359-4a23-9de7-ec9817d74ae0.jpg)|![2](https://user-images.githubusercontent.com/110389988/208947377-623e692f-b42a-4707-90db-5b5ccb952883.jpg)|![3](https://user-images.githubusercontent.com/110389988/208947492-e1441fab-5615-4efe-9c72-8ca6b2a93c81.jpg)|

## Configuración de la interfaz gráfica

Esta dividida en 3 bloques de imágenes que se superponen entre sí dependiendo de las elecciones del cliente:

|**Imagen de fondo**| |
|:--:|:-:|
|Es la base de la interfaz gráfica, en el rectángulo grande se mostrará el reproductor de la webcam en tiempo real, en el hueco vacío de la derecha se mostraran las diferentes pantallas con las opciones y en los círculos inferiores se mostrarán los iconos de cada selección.|![fondo](https://user-images.githubusercontent.com/110389988/208949976-cd94fb0b-7165-44db-91c3-d0e642a3e7e4.png)|


|**Pantallas de opción**| |
|:--:|:-:|
|Indican las opciones disponibles, en la primera imagen son sólo 2 mientras que en las siguientes son 3. Además la segunda y la tercera imagen dependen de la primera elección y la última muestra únicamente que el pedido se ha realizado con éxito. Todas estas variaciones hay que tenerlas en cuenta a la hora de crear la lógica del código.|![opciones](https://user-images.githubusercontent.com/110389988/208950867-2b4c5fb4-037f-4a77-8fae-23c8e4fcef6e.png)|

|**Iconos**| |
|:--:|:-:|
|Indican las selecciones hechas, al igual que con las opciones el segundo icono depende de la primera elección y por lo tanto habrá que aplicar esa lógica en el código.|![iconos](https://user-images.githubusercontent.com/110389988/208953482-d472cde4-f8c4-4f6e-a112-093322794e84.png)|
