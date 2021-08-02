from os import getcwd
from speech_recognition import AudioData, Microphone, Recognizer, UnknownValueError
from gtts import gTTS
from playsound import playsound
from consts.start import ACTION_START, START
from consts.play import ACTION_PLAY, PLAY
from consts.pause import ACTION_PAUSE, PAUSE
from consts.stop import ACTION_STOP, STOP

class AudioService():
    __cwd_audios: str = f'{getcwd()}/audios'
    
    @classmethod
    def listen_to_microphone(cls) -> str:
        microfone: Recognizer = Recognizer()

        with Microphone() as source:
            try:
                microfone.adjust_for_ambient_noise(source)

                audio: AudioData = microfone.listen(source)
                
                listen_to: str = ''
                action: str = ''
                
                if audio:
                    audio_text: str = microfone.recognize_google(audio, language = 'pt-BR')
                    
                    if audio_text:
                        action, listen_to  = cls.__get_action(audio_text)
                        
                        if action and listen_to:
                            if action == START:
                                cls.__create_audio(listen_to, 'listen_to')
                        
                                cls.__play_audio(f'{cls.__cwd_audios}/listen_to.mp3')
            except UnknownValueError:
                # cls.__play_audio(f'{cls.__cwd_audios}/unknown_microphone_audio.mp3')
                
                pass
            except Exception:
                pass
            finally:
                return action, listen_to
                
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
        action_consts: tuple[dict] = (
            {
                "name": ACTION_START,
                "value": START
            }, 
            {
                "name": ACTION_PLAY,
                "value": PLAY
            }, 
            {
                "name": ACTION_PAUSE,
                "value": PAUSE
            }, 
            {
                "name": ACTION_STOP,
                "value": STOP
            }
        )
        text_lower: str = text.lower()
        
        choosen_action: int = 0
        listen_to: str = ''
        
        for action in action_consts:
            if action['name'] in text_lower:
                choosen_action = action['value']
                listen_to = text_lower.replace(action['name'], '')
                    
        return choosen_action, listen_to