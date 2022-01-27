import simpleaudio as sa
import random

# load the sound files
_audio_map = {
    # "active-sound": sa.WaveObject.from_wave_file("../assets/audio/Turret_active.wav"),
    "deploy-sound": sa.WaveObject.from_wave_file("../assets/audio/Turret_deploy.wav"),
    "retract-sound": sa.WaveObject.from_wave_file("../assets/audio/Turret_retract.wav"),

    "active-line-1": sa.WaveObject.from_wave_file("../assets/audio/Turret_turret_active_1.wav"),
    "active-line-2": sa.WaveObject.from_wave_file("../assets/audio/Turret_turret_active_2.wav"),
    "active-line-4": sa.WaveObject.from_wave_file("../assets/audio/Turret_turret_active_4.wav"),
    "active-line-5": sa.WaveObject.from_wave_file("../assets/audio/Turret_turret_active_5.wav"),
    "active-line-6": sa.WaveObject.from_wave_file("../assets/audio/Turret_turret_active_6.wav"),
    "active-line-7": sa.WaveObject.from_wave_file("../assets/audio/Turret_turret_active_7.wav"),
    "active-line-8": sa.WaveObject.from_wave_file("../assets/audio/Turret_turret_active_8.wav"),

    "autosearch-line-1": sa.WaveObject.from_wave_file("../assets/audio/Turret_turret_autosearch_1.wav"),
    "autosearch-line-2": sa.WaveObject.from_wave_file("../assets/audio/Turret_turret_autosearch_2.wav"),
    "autosearch-line-4": sa.WaveObject.from_wave_file("../assets/audio/Turret_turret_autosearch_4.wav"),
    "autosearch-line-5": sa.WaveObject.from_wave_file("../assets/audio/Turret_turret_autosearch_5.wav"),
    "autosearch-line-6": sa.WaveObject.from_wave_file("../assets/audio/Turret_turret_autosearch_6.wav"),

    "deploy-line-1": sa.WaveObject.from_wave_file("../assets/audio/Turret_turret_deploy_1.wav"),
    "deploy-line-2": sa.WaveObject.from_wave_file("../assets/audio/Turret_turret_deploy_2.wav"),
    "deploy-line-4": sa.WaveObject.from_wave_file("../assets/audio/Turret_turret_deploy_4.wav"),
    "deploy-line-5": sa.WaveObject.from_wave_file("../assets/audio/Turret_turret_deploy_5.wav"),
    "deploy-line-6": sa.WaveObject.from_wave_file("../assets/audio/Turret_turret_deploy_6.wav"),

    "retire-line-1": sa.WaveObject.from_wave_file("../assets/audio/Turret_turret_retire_1.wav"),
    "retire-line-2": sa.WaveObject.from_wave_file("../assets/audio/Turret_turret_retire_2.wav"),
    "retire-line-4": sa.WaveObject.from_wave_file("../assets/audio/Turret_turret_retire_4.wav"),
    "retire-line-5": sa.WaveObject.from_wave_file("../assets/audio/Turret_turret_retire_5.wav"),
    "retire-line-6": sa.WaveObject.from_wave_file("../assets/audio/Turret_turret_retire_6.wav"),
    "retire-line-7": sa.WaveObject.from_wave_file("../assets/audio/Turret_turret_retire_7.wav"),

    "search-line-1": sa.WaveObject.from_wave_file("../assets/audio/Turret_turret_search_1.wav"),
    "search-line-2": sa.WaveObject.from_wave_file("../assets/audio/Turret_turret_search_2.wav"),
    "search-line-4": sa.WaveObject.from_wave_file("../assets/audio/Turret_turret_search_4.wav")
}

_active_lines = [
    "active-line-1",
    "active-line-2",
    "active-line-4",
    "active-line-5",
    "active-line-6",
    "active-line-7",
    "active-line-8",
]

_autosearch_lines = [
    "autosearch-line-1",
    "autosearch-line-2",
    "autosearch-line-4",
    "autosearch-line-5",
    "autosearch-line-6",
]

_deploy_lines = [
    "deploy-line-1",
    "deploy-line-2",
    "deploy-line-4",
    "deploy-line-5",
    "deploy-line-6",
]

_retire_lines = [
    "retire-line-1",
    "retire-line-2",
    "retire-line-4",
    "retire-line-5",
    "retire-line-6",
    "retire-line-7",
]

_search_lines = [
    "search-line-1",
    "search-line-2",
    "search-line-4"
]


def getDeploySound():
    return _audio_map["deploy-sound"]


def getRetractSound():
    return _audio_map["retract-sound"]


def getActiveVoiceLine():
    return _audio_map[random.choice(_active_lines)]


def getAutosearchVoiceLine():
    return _audio_map[random.choice(_autosearch_lines)]


def getDeployVoiceLine():
    return _audio_map[random.choice(_deploy_lines)]


def getRetireVoiceLine():
    return _audio_map[random.choice(_retire_lines)]


def getSearchVoiceLine():
    return _audio_map[random.choice(_search_lines)]


def playAsyncSound(sound):
    sound.play()


def playSyncSound(sound):
    play_obj = sound.play()
    play_obj.wait_done()
