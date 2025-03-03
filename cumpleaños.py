import streamlit as st

# Configurar la página
st.set_page_config(page_title="Happy Birthday", page_icon="🎂", layout="wide")

# Estilos personalizados con CSS
st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Poppins:wght@300;700&display=swap');
        .stApp {
            background-color: #f7e1f7;
            background-image: url('https://www.transparenttextures.com/patterns/stardust.png');
        }
        .title {
            font-family: 'Pacifico', cursive;
            text-align: center;
            font-size: 50px;
            color: #8B5CF6;
        }
        .subtitle {
            font-family: 'Poppins', sans-serif;
            text-align: center;
            font-size: 35px;
            color: #6D28D9;
            font-weight: bold;
        }
        .details {
            font-family: 'Poppins', sans-serif;
            text-align: center;
            font-size: 20px;
            color: #4B0082;
        }
        .celebrate {
            font-family: 'Poppins', sans-serif;
            text-align: center;
            font-size: 25px;
            color: #D97706;
            font-weight: bold;
        }
        .button-container {
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True
)


# Menú lateral
menu = ["Inicio", "Carta de Cumpleaños", "Recordatorio", "Playlist", "Sorpresa"]
choice = st.sidebar.selectbox("🎈 Menú", menu)

if choice == "Inicio":
    st.markdown("""
    <div class='title'>Jasmany Denilson</div>
    <div class='subtitle'>Happy Birthday</div>
    <div class='details'>
        06 DE MARZO 
    </div>
    <div class='celebrate'>Celebremos</div>
    """, unsafe_allow_html=True)
    
    # Mostrar la imagen centrada
    # Mostrar imagen decorativa centrada
    col1, col2, col3 = st.columns([1, 6, 1])  
    with col2:
        st.image("primera.jpg", width=775, caption="🎂 ¡Disfruta tu día especial!")
    
    # Animaciones
    st.balloons()

elif choice == "Carta de Cumpleaños":
    st.markdown("""
    <style>
    .birthday-container {
        text-align: center;
        background: linear-gradient(to right, #ff9a9e, #fad0c4);
        padding: 40px;
        border-radius: 20px;
        box-shadow: 4px 4px 20px rgba(0, 0, 0, 0.3);
        margin-top: 30px;
    }
    
    .birthday-title {
        color: #fff;
        font-size: 55px;
        font-family: 'Dancing Script', cursive;
        font-weight: bold;
        text-shadow: 3px 3px 10px rgba(0, 0, 0, 0.5);
    }
    
    .birthday-message {
        color: #000000;
        font-size: 22px;
        font-family: 'Poppins', sans-serif;
        background: rgba(255, 255, 255, 0.2);
        padding: 25px;
        border-radius: 15px;
        box-shadow: 2px 2px 12px rgba(255, 255, 255, 0.3);
        display: inline-block;
        max-width: 80%;
        line-height: 1.6;
    }
    
    </style>
    
    <div class='birthday-container'>
        <h1 class='birthday-title'>💌 Carta de Cumpleaños</h1>
        <p class='birthday-message'>
            ¡Feliz cumpleaños! 🎉 Hoy es un día especial porque celebramos a una persona increíble (osea a ti). 
                Espero que la pases increíble, que te llenen de amor, abrazos y muchas cosas ricas de comer. 
                Me encanta compartir momentos contigo y sinceramente no hay día en el que no me alegres con
                 tu forma de ser. Ojalá este año te traiga todo lo bueno que mereces y que podamos seguir creando recuerdos juntos. 
                Disfruta mucho tu día, porque hoy todo gira alrededor de ti. 💖
            </b>
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Espacio adicional antes de la imagen
    st.markdown("<br><br>", unsafe_allow_html=True)

    # Mostrar imagen decorativa centrada
    col1, col2, col3 = st.columns([1, 6, 1])  
    with col2:
        st.image("image1.jpeg", width=1340)

    st.markdown("""
    <style>
    .birthday-container {
        text-align: center;
        background: linear-gradient(to right, #ff9a9e, #fad0c4);
        padding: 40px;
        border-radius: 20px;
        box-shadow: 4px 4px 20px rgba(0, 0, 0, 0.3);
        margin-top: 30px;
    }
    

    .birthday-message {
        color: #000000;
        font-size: 22px;
        font-family: 'Poppins', sans-serif;
        background: rgba(255, 255, 255, 0.2);
        padding: 25px;
        border-radius: 15px;
        box-shadow: 2px 2px 12px rgba(255, 255, 255, 0.3);
        display: inline-block;
        max-width: 80%;
        line-height: 1.6;
    }
    
    </style>
    
    <div class='birthday-container'>
        <p class='birthday-message'>
            Felicidades, sobreviviste otro año.Espero que sigas sumando experiencia
                 sin sentirte tan cansado en el proceso. Disfruta el día, haz locuras (pero no tantas) 
                y acuérdate de que los cumpleaños son la excusa perfecta para hacer lo que quieras.
                 Así que mínimo espero que hoy no trabajes ni te estreses. 😌💖</b>
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Espacio adicional antes de la imagen
    st.markdown("<br><br>", unsafe_allow_html=True)

    # Mostrar imagen decorativa centrada
    col1, col2, col3 = st.columns([1, 6, 1])  
    with col2:
        st.image("image3.jpeg", width=1340)
    
    st.markdown("""
    <style>
    .birthday-container {
        text-align: center;
        background: linear-gradient(to right, #ff9a9e, #fad0c4);
        padding: 40px;
        border-radius: 20px;
        box-shadow: 4px 4px 20px rgba(0, 0, 0, 0.3);
        margin-top: 30px;
    }
    

    .birthday-message {
        color: #000000;
        font-size: 22px;
        font-family: 'Poppins', sans-serif;
        background: rgba(255, 255, 255, 0.2);
        padding: 25px;
        border-radius: 15px;
        box-shadow: 2px 2px 12px rgba(255, 255, 255, 0.3);
        display: inline-block;
        max-width: 80%;
        line-height: 1.6;
    }
    
    </style>
    
    <div class='birthday-container'>
        <p class='birthday-message'>
            No sé si te diste cuenta, pero el tiempo pasa volando. 🤯 Un año más 
                y muchas cosas han cambiado, pero lo importante es que sigas avanzando. 
                Te deseo un buen cumpleaños, que este año traiga cosas nuevas y sobre todo 
                que nunca te falten buenas historias que contar. 🎂
                <br><br>
            <b>Este video es para ti😉💖</b>
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Espacio adicional antes de la imagen
    st.markdown("<br><br>", unsafe_allow_html=True)

    # Mostrar imagen decorativa centrada
    col1, col2, col3 = st.columns([1, 3, 1])  
    with col2:
     st.video("video.mp4")

# Inicializar variables en session_state si no existen
if "mensaje_guardado" not in st.session_state:
    st.session_state.mensaje_guardado = ""
if "foto_guardada" not in st.session_state:
    st.session_state.foto_guardada = None

elif choice == "Recordatorio":
    col1, col2, col3 = st.columns([1, 6, 1])
    
    mensaje = col2.text_area("💖 Escribe un mensaje especial", value=st.session_state.mensaje_guardado)
    foto = col2.file_uploader("📷 Sube una foto de ustedes juntos:", type=["jpg", "png", "jpeg"])
    
    if col2.button("Guardar Recordatorio"):
        st.session_state.mensaje_guardado = mensaje
        if foto is not None:
            st.session_state.foto_guardada = foto
        st.success("Mensaje y foto guardados con amor 💖")

    # Mostrar mensaje y foto guardados
    if st.session_state.mensaje_guardado:
        col2.write(st.session_state.mensaje_guardado)
    if st.session_state.foto_guardada:
        col2.image(st.session_state.foto_guardada, caption="Recuerdo Especial", width=700)



if choice == "Playlist":
    # Lista 1: "Nuestras Canciones"
    st.markdown("<h2>🎶 Nuestras Canciones</h2>", unsafe_allow_html=True)

    nuestras_canciones = {
        "Aprender a Quererte - Morat": "https://youtu.be/OukQDrJ7QRQ?si=bCepZ6d0T0nAPuOo",
        "Perfect - Ed Sheeran": "https://youtu.be/jb0K64SGsfc?si=MqZLZNDOhLdJyha0"
    }

    selected_song_1 = st.selectbox("💖 Escoge una canción:", list(nuestras_canciones.keys()), key="playlist_1")

    if st.button("Reproducir canción 🎶"):
        st.markdown(f"[Escuchar en YouTube ▶️]({nuestras_canciones[selected_song_1]})", unsafe_allow_html=True)

    # Separador visual
    st.markdown("---")

    # Lista 2: "Estas canciones son para ti"
    st.markdown("<h2>🎵 Estas canciones son para ti 💖</h2>", unsafe_allow_html=True)

    canciones_para_ti = {
        "Me cambiaste la vida - Río Roma": "https://youtu.be/_X3PPuF_yOE?si=AEqEwBiLGSmkW8kp",
        "Comenzar de nuevo - Jhovan Tomasebich": "https://youtu.be/JGyX0NgfvM8?si=KZzCOtREzb0aKiFo",
        "Por eso te amo - Río Roma": "https://youtu.be/9jirj0OjI-M?si=bEIe_nOCqk1LeZiW",
        "Mi persona favorita - Río Roma": "https://youtu.be/x-0KoCAV4mc?si=AwGbeJ-HjlSXt975",
        "Sabes - Reik": "https://youtu.be/lBiP5mkp0fM?si=-D_DQj1JSeXKIAlm",
        "No hay nadie más - Sebastián Yatra": "https://youtu.be/sD9_l3oDOag?si=QgCvAyiVUE6a7Akr",
        "Confieso - Humbe": "https://youtu.be/4Ja6WLrZlAE?si=GIk3UBUNtx7Gz8Br",
        "Amor de cine - Humbe": "https://youtu.be/4O1CNtVG7s8?si=rH_W0NcDAh90sGgR",
        "Y llegaste tú - Sin Bandera": "https://youtu.be/QlYdRn9FA3Q?si=L6oOIONXs8ZqQAyJ",
        "Amor de febrero - Jay Wheeler": "https://youtu.be/5r4aLNqSkyE?si=MEwh6JTXqSJ0A0ia",
        "Te encontré - Idéntico": "https://youtu.be/Xa6CpcKmoEI?si=aJE0qVQxB_MQIKNF",
        "Tus ojitos - Samanez": "https://youtu.be/ZbjWXcMwJ_k?si=ibXdltL33VGi1x38",
        "Por amarte así - CNCO": "https://youtu.be/QTzYYxJuISE?si=wh5J1LXRxS_xj6Wu",
        "Hasta el fin del mundo - Jennifer Peña": "https://youtu.be/4lwVJVBBozw?si=dMAcPJI-6-j6jQpz",
        "Say Yes To Heaven - Lana del Rey": "https://youtu.be/vdGkKoe8bRI?si=vgVvejm8w1EAjnwa",
        "Just The Way You Are - Bruno Mars": "https://youtu.be/LjhCEhWiKXk?si=reL2TH2fd9T3yJ-u",
        "Vida Mía - William Luna": "https://youtu.be/68HWYw1WVlo?si=UgMhNkOqFGGUGBtD",
        "Oye Mi Amor - Maná": "https://youtu.be/h0p8yTqj8i4?si=wL-xW56o5qXOpbNl"
    }

    selected_song_2 = st.selectbox("💖 Escoge una canción:", list(canciones_para_ti.keys()), key="playlist_2")

    if st.button("Reproducir canción 🎶 "):
        st.markdown(f"[Escuchar en YouTube ▶️]({canciones_para_ti[selected_song_2]})", unsafe_allow_html=True)




elif choice == "Sorpresa":
    col1, col2, col3 = st.columns([1, 6, 1])  

    with col2:  # Centra el contenido en la columna del medio
        st.markdown("""
        <div style='text-align: center;'>
            <h2>🎂 Sorpresa</h2>
            <p>¡Aquí tienes una torta especial para soplar! 🎂</p>
        </div>
        """, unsafe_allow_html=True)

        st.image(
            "https://www.ferrerorocher.com/es/sites/ferrerorocher20_es/files/2021-05/birthday-cake_0.jpeg?t=1739459814",
            caption="Haz un deseo y sopla las velas 🎂",
            width=775  # Ajusta el tamaño para que no se vea demasiado grande
        )

        if st.button("🎂 Soplar la vela"):
            st.balloons()
            st.markdown("""
            <div style='text-align: center;'>
                <h1 style='font-size: 80px; color: #000000;'>🎉 ¡Feliz Cumpleaños mi niño hermoso! 🎉</h1>
            </div>
            """, unsafe_allow_html=True)

# Efecto de nieve
st.snow()

