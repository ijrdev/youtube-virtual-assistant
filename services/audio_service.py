from os import getcwd
from speech_recognition import AudioData, Microphone, Recognizer, UnknownValueError
from gtts import gTTS
from playsound import playsound

class AudioService():
    __cwd_audios: str = f'{getcwd()}/audios'
    
    @classmethod
    def listen_to_microphone(cls) -> str:
        microfone: Recognizer = Recognizer()

        with Microphone() as source:
            try:
                microfone.adjust_for_ambient_noise(source)

                audio: AudioData = microfone.listen(source)
                
                audio_text: str = microfone.recognize_google(audio, language = 'pt-BR')
                
                cls.create_audio(audio_text, 'listen_to')
                
                cls.__play_audio(f'{cls.__cwd_audios}/listen_to.mp3')
                
                return audio_text
            except Exception:
                cls.__play_audio(f'{cls.__cwd_audios}/unknown_microphone_audio.mp3')
                
                pass
                
    @classmethod
    def create_audio(cls, audio_text: str, file_name: str) -> None:
        tts = gTTS(str(audio_text), lang = 'pt-br')
        
        tts.save(f'{cls.__cwd_audios}/{file_name}.mp3')
        
    @classmethod
    def __play_audio(cls, audio_path: str) -> None:
        playsound(audio_path)

    @classmethod
    def execute_audio(cls, type: str = '') -> None:
        playsound(f'{cls.__cwd_audios}/{type}.mp3')