# VoiceAssistantTechTalk

## Descripción
VoiceAssistantTechTalk es un proyecto de código abierto diseñado para explorar y desarrollar un asistente virtual interactivo en Python. Este asistente utiliza tecnologías avanzadas como el Reconocimiento Automático de Voz (ASR), Text-to-Speech (TTS) a través de gTTS, y la API de Wikipedia para proporcionar una experiencia interactiva. Permite a los usuarios hacer preguntas en voz alta, a las cuales el asistente responde buscando información relevante en Wikipedia y leyendo los resultados en voz alta.

## Características
- **Reconocimiento de Voz:** Utiliza la biblioteca `speech_recognition` para convertir el habla del usuario en texto.
- **Síntesis de Voz:** Emplea `gTTS` (Google Text-to-Speech) para convertir texto en audio, permitiendo al asistente "hablar" las respuestas.
- **Interacción con Wikipedia:** Busca información en Wikipedia utilizando la biblioteca `wikipediaapi`, proporcionando resúmenes de artículos basados en las consultas del usuario.
- **Interfaz de Audio:** Utiliza `pygame` para manejar la reproducción de audio, ofreciendo una experiencia de usuario fluida y agradable.

## Requisitos
Para ejecutar este proyecto, necesitarás:
- Python 3.x
- Bibliotecas: `speech_recognition`, `gTTS`, `pygame`, `wikipediaapi`. Puedes instalarlas con el comando `pip install speech_recognition gtts pygame wikipedia-api`.

## Instalación
1. Clona el repositorio a tu máquina local usando `git clone https://github.com/tuUsuario/VoiceAssistantTechTalk.git`.
2. Instala las dependencias necesarias con `pip install -r requirements.txt`.
3. Ejecuta el script principal con `python virtual_assistant.py`.

## Uso
Una vez iniciado el script, el asistente virtual te pedirá que hables. Puedes hacerle preguntas o solicitar información sobre cualquier tema. El asistente procesará tu solicitud, buscará en Wikipedia y leerá en voz alta el resumen del artículo relacionado.

## Contribuciones
Las contribuciones son bienvenidas! Si tienes ideas para mejorar el proyecto o solucionar problemas, no dudes en crear un *pull request* o abrir un *issue*.

## Licencia
Este proyecto está bajo la Licencia MIT - mira el archivo `LICENSE.md` para detalles.
