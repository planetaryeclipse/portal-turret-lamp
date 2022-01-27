import detect_in_video
import turret_audio
import threading
import time

_SEARCH_TIME_SECS = 5


class Turret:
    def __init__(self):
        self.deployed = False
        self.target_found = False

        self.video_detector = detect_in_video.VideoDetector(
            self.face_enter, self.face_lost)
        self._thr = None

    def start(self):
        self.video_detector.start()

    def face_enter(self):
        if (not self.deployed):
            self.deployed = True
            self.target_found = True
            turret_audio.playAsyncSound(turret_audio.getDeploySound())
            turret_audio.playSyncSound(turret_audio.getDeployVoiceLine())
        elif (not self.target_found):
            self.target_found = True
            turret_audio.playSyncSound(turret_audio.getActiveVoiceLine())

    def face_lost(self):
        if (self.target_found):
            self.target_found = False
            turret_audio.playSyncSound(turret_audio.getSearchVoiceLine())

            self._thr = threading.Thread(target=self._search_timeout, args=())
            self._thr.start()

    def _search_timeout(self):
        start_time = time.time()

        while (not self.target_found):
            current_time = time.time()
            if(current_time - start_time >= _SEARCH_TIME_SECS):
                self.deployed = False
                turret_audio.playAsyncSound(turret_audio.getRetractSound())
                turret_audio.playSyncSound(turret_audio.getRetireVoiceLine())
                break


turret = Turret()
turret.start()
