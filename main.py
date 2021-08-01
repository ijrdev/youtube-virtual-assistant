from sys import exit
from services.audio_service import AudioService
from services.youtube_service import YoutubeService

if __name__ == '__main__':
    running: bool = True
    
    try:
        AudioService.execute_audio('start')
        
        while running:
            audio_text: str = AudioService.listen_to_microphone()
            
            print('----->', audio_text)
            
            # find how to ignore a exception error
            # error: UnknownValueError
            
            YoutubeService.execute(audio_text)
    except Exception as ex:
        AudioService.execute_audio('error')
        
        exit(0)