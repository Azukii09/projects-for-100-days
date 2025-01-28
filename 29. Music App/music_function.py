from playlist import playlist

logo = """  
███    ███ ██    ██ ███████ ██  ██████      █████  ██████  ██████  
████  ████ ██    ██ ██      ██ ██          ██   ██ ██   ██ ██   ██ 
██ ████ ██ ██    ██ ███████ ██ ██          ███████ ██████  ██████  
██  ██  ██ ██    ██      ██ ██ ██          ██   ██ ██      ██      
██      ██  ██████  ███████ ██  ██████     ██   ██ ██      ██   
"""

def print_playlist():
    for artist_index, t_song in enumerate(playlist,1):
        artist, songs = t_song
        for song_num,song in songs:
            print(f"{artist_index}:{song_num} {artist} - {song}")