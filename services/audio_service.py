from os import getcwd
from speech_recognition import AudioData, Microphone, Recognizer, UnknownValueError
from gtts import gTTS
from playsound import playsound
from consts.start import ACTION_START
from consts.play import ACTION_PLAY
from consts.pause import ACTION_PAUSE
from consts.stop import ACTION_STOP

class AudioService():
    __cwd_audios: str = f'{getcwd()}/audios'
    
    @classmethod
    def listen_to_microphone(cls) -> str:
        microfone: Recognizer = Recognizer()

        with Microphone() as source:
            try:
                microfone.adjust_for_ambient_noise(source)

                audio: AudioData = microfone.listen(source)
                
                if audio:
                    audio_text: str = microfone.recognize_google(audio, language = 'pt-BR')
                    
                    action, new_audio_text = cls.__get_action(audio_text)
                    
                    if new_audio_text:
                        cls.__create_audio(new_audio_text, 'listen_to')
                    
                        cls.__play_audio(f'{cls.__cwd_audios}/listen_to.mp3')
                        
                        return new_audio_text, action
            except UnknownValueError:
                cls.__play_audio(f'{cls.__cwd_audios}/unknown_microphone_audio.mp3')
                
                pass
            except Exception as ex:
                pass
                
    @classmethod
    def __create_audio(cls, audio_text: str, file_name: str) -> None:
        tts = gTTS(str(audio_text), lang = 'pt-br')
        
        tts.save(f'{cls.__cwd_audios}/{file_name}.mp3')
        
    @classmethod
    def __play_audio(cls, audio_path: str) -> None:
        playsound(audio_path)

    @classmethod
    def execute_audio(cls, type: str) -> None:
        playsound(f'{cls.__cwd_audios}/{type}.mp3')
        
    @classmethod
    def __get_action(cls, text: str):
        action_consts: tuple = (ACTION_START, ACTION_PLAY, ACTION_PAUSE, ACTION_STOP)
        text_lower: str = text.lower()
        
        for action_type in action_consts:
            for action in action_type:
                if action in text_lower or action == text_lower:
                    music: str = text_lower.replace(action, '')
                    
                    return action_type[0], music