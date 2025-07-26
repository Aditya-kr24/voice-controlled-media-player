# 🎙️ Voice-Controlled Media Player

This is a Python-based media player that allows you to control video playback using your voice. It uses **Google Speech Recognition API** to understand spoken commands and controls **VLC Media Player** via its Python bindings.

## 🛠️ Features

- 🎬 Play, pause, stop video
- 🔊 Increase/decrease volume
- ⏩ Fast forward and rewind (by 10 seconds)
- 🔇 Mute/unmute toggle
- 🎤 Real-time speech recognition with ambient noise adjustment

## 🧰 Technologies Used

- Python
- `speech_recognition` for converting speech to text
- `python-vlc` for media control
- Google Web Speech API
- `time` module for sync/playback control

## 🖥️ Requirements

- Python 3.x
- VLC Media Player (must be installed)
- Python libraries:
  ```bash
  pip install speechrecognition python-vlc
