import streamlit as st
import google.generativeai as genai
import requests
import key
import photo

genai.configure(api_key=key.clave)

model = genai.GenerativeModel(model_name="gemini-1.0-pro")

PHOTO_ACCESS_KEY = photo.clave

def get_unsplash_image(query):
    url = f"https://api.unsplash.com/search/photos?query={query}&client_id={PHOTO_ACCESS_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'results' in data and data['results']:
            return data['results'][0]['urls']['regular']
    return None

nombre = st.text_input("¿Cómo te llamas?")
ciudad = st.text_input("¿Sobre qué ciudad deseas consultar?")

context = (f'Como un guía turístico experto, recomiéndale a {nombre} sobre la ciudad de {ciudad}, solo lo que te pregunta específicamente. Ofrecele tus opciones con información detallada e incluir precio de entradas si correspondiese, y también como llegar en transporte público, su precio, y horarios. Al final, preguntale si ha podido visitar alguna de tus recomendaciones, y si necesita más sugerencias.')

# Inicializar el historial de chat en el estado de sesión
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Función para agregar un mensaje al historial de chat
def add_message(role, content):
    st.session_state.chat_history.append({"role": role, "content": content})

# Función para obtener la experiencia del usuario
def obtener_experiencia():
    if st.session_state.chat_history:
        ultimo_tema = st.session_state.chat_history[-1]["content"]
        return f"{nombre}, ¿cómo fue tu experiencia con {ultimo_tema}?"

# Función para dar feedback sobre las preferencias del usuario
def feedback_preferencias(preferencias):
    return f"{nombre}, tus preferencias son {preferencias}. Aquí tienes algunas recomendaciones basadas en ellas:"

# Título
st.title("Recomendador de Lugares de Interés para Viajes")

# Descripción
st.write("""
## Descripción
Esta aplicación ofrece recomendaciones personalizadas de lugares de interés para tus viajes basadas en tus preferencias y necesidades. Puedes interactuar con nuestro sistema para obtener información detallada, hacer preguntas y recibir feedback personalizado.
""")



if nombre:
    st.write(f"¡Hola {nombre}! ¿En qué puedo ayudarte a planificar tu viaje?")

# Mostrar el historial de chat en la barra lateral
st.sidebar.title("Chat History")
selected_message = st.sidebar.selectbox("Selecciona un mensaje", range(len(st.session_state.chat_history)), format_func=lambda i: st.session_state.chat_history[i]["content"])

# Mostrar el chat seleccionado en el área principal
st.title("Chat")
for i, message in enumerate(st.session_state.chat_history):
    with st.chat_message(message["role"]):
        st.write(message["content"])
        if i == selected_message:
            break

# Aceptar entrada del usuario
prompt = st.chat_input("Escribe tu consulta")
if prompt:
    add_message("user", prompt)

    with st.spinner("Obteniendo recomendaciones..."):
        response = model.generate_content(context + prompt)
        
    add_message("assistant", response.text)

    with st.chat_message("assistant"):
        st.write(response.text)

    # Obtener imagen del lugar sugerido
    lugar_sugerido = response.text.split("\n")[0]
    imagen_url = get_unsplash_image(lugar_sugerido)
    if imagen_url:
        st.image(imagen_url, caption=lugar_sugerido)
    else:
        st.write("No se pudo obtener una imagen para el lugar sugerido.")

# Sección de experiencia del usuario
st.write("### Experiencia del Usuario")
experiencia = obtener_experiencia()
if experiencia:
    st.write(experiencia)

# Sección de preferencias del usuario
st.write("### Tus Preferencias")
preferencias = st.text_area("Ingresa tus preferencias de viaje aquí")
if preferencias:
    feedback = feedback_preferencias(preferencias)
    st.write(feedback)
    
    # Generar nuevas recomendaciones basadas en las preferencias
    with st.spinner("Obteniendo recomendaciones basadas en tus preferencias..."):
        response_preferencias = model.generate_content(f"{context} Aquí tienes algunas recomendaciones basadas en las preferencias de {nombre}: {preferencias}.")
    
    add_message("assistant", response_preferencias.text)
    
    with st.chat_message("assistant"):
        st.write(response_preferencias.text)
        
        # Obtener imagen del lugar sugerido
        lugar_sugerido = response_preferencias.text.split("\n")[0]
        imagen_url = get_unsplash_image(lugar_sugerido)
        if imagen_url:
            st.image(imagen_url, caption=lugar_sugerido)
        else:
            st.write("No se pudo obtener una imagen para el lugar sugerido.")

# Sección de preguntas frecuentes
st.write("### Preguntas Frecuentes")
st.write("""
1. **¿Cómo obtengo recomendaciones personalizadas?**
   - Ingresa tu nombre y la ciudad sobre la que deseas consultar, luego escribe tu consulta en el chat.
2. **¿Cómo ingreso mis preferencias de viaje?**
   - Usa la sección "Tus Preferencias" para ingresar lo que te gusta y obtener feedback y recomendaciones basadas en ello.
3. **¿Puedo ver mi historial de chat?**
   - Sí, tu historial de chat está disponible en la barra lateral.
4. **¿Qué tipo de información puedo obtener sobre los lugares de interés?**
   - Puedes obtener detalles sobre horarios, precios de entradas, cómo llegar en transporte público, entre otros.
""")

