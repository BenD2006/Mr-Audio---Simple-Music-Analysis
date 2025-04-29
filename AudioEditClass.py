from pydub import AudioSegment
class ModifyAudioFile:
    def __init__(self,audiofile):
        self.audioFile = audiofile

    def VolumeChanger(self):
        file = AudioSegment.from_wav(codeWanted)
        print(file)
