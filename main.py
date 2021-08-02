from services.audio_service import AudioService
from services.youtube_service import YoutubeService

if __name__ == '__main__':
    AudioService.execute_audio('start')
    AudioService.execute_audio('audio_question')
    
    while True:
        action, audio_text = AudioService.listen_to_microphone()
        
        if action and audio_text:
            YoutubeService.execute(action, audio_text)