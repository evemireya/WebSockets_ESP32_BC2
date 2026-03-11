# Cuestionario de Evaluación: Comunicación por Sockets 📝

**Nombre del Estudiante:** Evelyn Mena
**Fecha:** 11/03/2026

*Instrucciones: Responde a las siguientes preguntas basándote en la teoría de redes y en el análisis del código de nuestro proyecto. Sube este archivo con tus respuestas a tu repositorio como evidencia de trabajo.*

1. **¿Qué es una Dirección IP y para qué sirve en nuestro proyecto?**
   > *Tu respuesta aquí*
   > Es una forma de como podemos ubicar un servicio como si tuviera una identidad.

2. **¿Qué es un Puerto de red? (Menciona qué puerto estamos usando en el código de la ESP32).**
   > *Tu respuesta aquí*
   > Es de lo que se trata el servicio que estamos dando, estamos usando el puerto 80.

3. **Define con tus propias palabras qué es un Servidor en informática.**
   > *Tu respuesta aquí*
   > Es el sistema que ofrece servicios a otros usuarios.

4. **¿Cuál es la diferencia entre un "Servidor" (Hardware/Software) y un "Servicio" (Service)?**
   > *Tu respuesta aquí*
   > El servidor es la computadora que se encarga de atender y el servidores la función que les da a los usuarios.

5. **Investigación: ¿Cuál es la diferencia técnica entre un "Socket TCP" normal y un "WebSocket"?**
   > *Tu respuesta aquí*
   > El Socket TCP es la conexión directa que hay entre dos programas y el WebSocket es la conexión entre el navegador y el servidor se envíen mensajes en tiempo real.

6. **Analizando nuestro código: ¿Quién actúa como Servidor y quién actúa como Cliente? (Justifica tu respuesta mencionando qué funciones del código lo demuestran, ej. `bind()`, `connect()`).**
   > *Tu respuesta aquí*
   > La  computadora actúa como servidor, porque tiene funciones como bind() y listen() para esperar conexiones y el dispositivo ctúa como cliente, porque usa connect() para conectarse con el servidor.

7. **En el código de la computadora (Python), importamos la librería `threading` (Hilos). ¿Qué pasaría con la ventana de Tkinter si no usáramos hilos para recibir los datos de la red?**
   > *Tu respuesta aquí*
   > La ventana se quedaría congelada porque estaría ocupando los datos de la red.

8. **¿Por qué es necesario usar bloques `try...except` cuando trabajamos con conexiones de red e Internet?**
   > *Tu respuesta aquí*
   > Porque las conexiones pueden fallar y usando los bloques evita que se cierre por error.

9. **En la función de encender el LED en Python, enviamos el comando así: `sock.send(b'ON')`. ¿Qué significa esa letra `b` antes de las comillas y por qué no enviamos un texto normal?**
   > *Tu respuesta aquí*
   > La b significa bytes y siemopre debe de enviarse en bytes no en texto normal.

10. **Describe brevemente el flujo de datos: ¿Qué camino recorre la información desde que giras el potenciómetro físicamente hasta que la barra se mueve en la pantalla de la computadora?**
    > *Tu respuesta aquí*
    > 
