from sys import exit
from services.audio_service import AudioService
from services.youtube_service import YoutubeService
from models.StopException import StopException

if __name__ == '__main__':
    try:
        AudioService.execute_audio('start')
        AudioService.execute_audio('audio_question')
        
        while True:
            audio_text, action = AudioService.listen_to_microphone()
            
            if audio_text and action:
                YoutubeService.execute(audio_text, action)
    except StopException:
        AudioService.execute_audio('stop')
        
        YoutubeService.close_browser()
        
        exit(0)
    except  Exception as ex:
        AudioService.execute_audio('error')
        
        YoutubeService.close_browser()
        
        exit(0)