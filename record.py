"""Code for decoding data"""
from packages.audio import record
from packages.audio import playback
import os

curr_dir = os.path.dirname(__file__)


def run():
    """main loop"""
    file_name_short = input("File name to save (.wav): ")
    file_name_full = os.path.join(curr_dir, "data/" + file_name_short + ".wav")

    duration = int(input("Duration of recording (seconds): "))
    
    record(5, file_name_full)
    
    playback (file_name_full)



if __name__ == "__main__":
    print("\nTeam Wapiti - Record\n~~~~~~~~~~~~~~~~~~~\n")
    run()