import io
import speech_recognition as sr
from gtts import gTTS
import pygame
import wikipediaapi

def initialize_pygame():
    print("Inicializando pygame...")
    pygame.mixer.init()
    pygame.init()

def listen():
    print("Escuchando...")
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Soy su asistente virtual sobre Wikipedia, ¿qué información desea?")
        print("Procesando audio...")
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio, language="es-ES")
            print(f"Texto reconocido: {text}")
        except sr.UnknownValueError:
            speak("Lo siento, no te entendí")
            print("No se pudo entender el audio.")
            return None
        except sr.RequestError:
            speak("No se pudo obtener resultados desde el servicio de Google Speech Recognition")
            print("Error al contactar el servicio de reconocimiento de voz.")
            return None

    return text

def speak(text):
    print(f"Hablando: {text}")
    # Generate TTS audio and save it to a BytesIO object
    tts = gTTS(text=text, lang='es')
    audio_fp = io.BytesIO()
    tts.write_to_fp(audio_fp)
    audio_fp.seek(0)  # Go back to the start of the memory file

    # Initialize pygame for audio playback
    pygame.mixer.init()
    pygame.mixer.music.load(audio_fp)
    pygame.mixer.music.play()
    
    print("Reproduciendo audio...")
    # Wait for the audio to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.stop()
    pygame.mixer.quit()
    audio_fp.close()  # Close the BytesIO object
    print("Audio finalizado.")

def search_in_wikipedia(query):
    print(f"Buscando en Wikipedia: {query}")
    # Specify a custom user_agent to comply with Wikipedia's policy
    wiki_api = wikipediaapi.Wikipedia(
        language='es', 
        user_agent="miAsistenteVirtual/1.0 (https://miwebsite.com/contacto)"
    )
    page = wiki_api.page(query)

    if page.exists():
        print("Página encontrada, extrayendo resumen...")
        return page.summary[0:400]  # Return the first 400 characters of the summary
    else:
        print("Página no encontrada.")
        return "No se encontró información sobre este tema en Wikipedia."

def virtual_assistant():
    print("Asistente virtual iniciado.")
    initialize_pygame()
    user_text = listen()
    if user_text:
        speak("Dame unos segundos, estoy buscando información...")
        response = search_in_wikipedia(user_text)
        speak(response)
    print("Asistente virtual finalizado.")

# Run the assistant
virtual_assistant()
