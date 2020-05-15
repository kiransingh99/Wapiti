"""Code for recording and playing back audio"""
from src.audio.recording import Recording
from src.plotting.plot_recording import plot_recording
from config import OUTPUT_DIR
import os


def run():
    """main loop"""
    file_name_short = input("File name to open (.wav): ")
    file_name_full = os.path.join(OUTPUT_DIR, file_name_short + ".wav")

    recording1 = Recording.from_file(file_name_full)
    recording1.play()
    
    recording1.append_recording(recording1)
    recording1.play()


if __name__ == "__main__":
    print("\nTeam Wapiti - Open Recording\n~~~~~~~~~~~~~~~~~~~\n")
    run()
