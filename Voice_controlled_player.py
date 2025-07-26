import speech_recognition as sr
import vlc
import time

# Initialize recognizer and microphone
r = sr.Recognizer()
m = sr.Microphone()

# Initialize VLC media player instance
player = vlc.MediaPlayer()

# Path to your video file (make sure this path is correct)
video_path = r"C:\Users\KIIT0001\Downloads\song.mp4"


# Set the media file to play
media = vlc.Media(video_path)
player.set_media(media)

# Function to control VLC based on recognized command
def control_vlc(command):
    command = command.lower()
    if "play" in command:
        print("Playing video...")
        player.play()
    elif "stop" in command:
        print("Pausing video...")
        player.pause()
    elif "break" in command:
        print("Stopping video...")
        player.stop()
    elif "forward" in command:
        print("Fast forwarding 10 seconds...")
        player.set_time(player.get_time() + 10000)  # Fast forward by 10 seconds
    elif "rewind" in command:
        print("Rewinding 10 seconds...")
        player.set_time(player.get_time() - 10000)  # Rewind by 10 seconds
    elif "volume up" in command:
        current_volume = player.audio_get_volume()
        if current_volume + 50 <= 100:  # Maximum volume is 100
            player.audio_set_volume(current_volume + 50)
            print("Increasing volume... Current volume:", current_volume + 10)
        else:
            print("Volume is already at maximum!")
    elif "volume down" in command:
        current_volume = player.audio_get_volume()
        if current_volume - 50 >= 0:  # Minimum volume is 0
            player.audio_set_volume(current_volume - 50)
            print("Decreasing volume... Current volume:", current_volume - 10)
        else:
            print("Volume is already at minimum!")
    elif "mute" in command:
        player.audio_toggle_mute()
        print("Muting/unmuting the video...")
    else:
        print("Unknown command")

# Start the VLC player (this helps to start the video before listening for commands)
print("Starting the video...")
player.play()
time.sleep(2)  # Give VLC time to start playing

try:
    print("A moment of silence, please...")
    with m as source:
        r.adjust_for_ambient_noise(source, duration=1)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))

    while True:
        print("Say something!")
        with m as source:
            audio = r.listen(source)
        print("Got it! Now to recognize it...")

        try:
            # Recognize speech using Google Speech Recognition
            value = r.recognize_google(audio)
            print("You said: {}".format(value))

            # Control VLC based on the recognized command
            control_vlc(value)

        except sr.UnknownValueError:
            print("Oops! Didn't catch that")
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))

except KeyboardInterrupt:
    print("Program terminated.")
    player.stop()
