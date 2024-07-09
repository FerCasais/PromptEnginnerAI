# PromptEnginnerAI
Aquí tienes el archivo README en formato Markdown:

# Recomendador de Lugares de Interés para Viajes

Esta aplicación de Streamlit ofrece recomendaciones personalizadas de lugares de interés para tus viajes basadas en tus preferencias y necesidades. Puedes interactuar con el sistema para obtener información detallada, hacer preguntas y recibir feedback personalizado.

## Características

- Recomendaciones de lugares de interés basadas en tu nombre y la ciudad que ingreses
- Opción para ingresar tus preferencias de viaje y obtener recomendaciones específicas
- Historial de chat disponible en la barra lateral para revisar las recomendaciones anteriores
- Sección de preguntas frecuentes con información útil sobre cómo usar la aplicación

## Requisitos

- Python 3.7 o superior
- Bibliotecas necesarias: `streamlit`, `google.generativeai`, `requests`, `python-dotenv`

## Configuración

1. Clona el repositorio de GitHub en tu máquina local.
2. Crea un archivo `.env` en la raíz del proyecto y agrega tus claves de API:

   ```plaintext
   API_KEY=TU_API_KEY
   PHOTO_ACCESS_KEY=TU_PHOTO_ACCESS_KEY
   ```

3. Asegúrate de agregar `.env` a tu archivo `.gitignore` para mantener tus claves seguras.
4. Instala las dependencias necesarias:

   ```bash
   pip install -r requirements.txt
   ```

5. Ejecuta la aplicación de Streamlit:

   ```bash
   streamlit run app.py
   ```

6. Abre tu navegador y visita `http://localhost:8501` para acceder a la aplicación.

## Uso

1. Ingresa tu nombre en el campo correspondiente.
2. Escribe el nombre de la ciudad sobre la que deseas consultar.
3. Interactúa con el chat para obtener recomendaciones sobre lugares de interés.
4. Usa la sección "Tus Preferencias" para ingresar tus preferencias de viaje y obtener recomendaciones personalizadas.
5. Revisa el historial de chat en la barra lateral para ver las recomendaciones anteriores.

## Contribución

Si deseas contribuir a este proyecto, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama para tu contribución.
3. Realiza los cambios y pruébalo localmente.
4. Envía un pull request con tus cambios.

## Licencia

https://github.com/FerCasais

¡Disfruta de tus viajes con nuestras recomendaciones personalizadas!
