import re
def song_decoder(song):
    song = song.replace("WUB", " ")
    return " ".join(song.split())

song_decoder("WUBAWUBBWUBCWUB")