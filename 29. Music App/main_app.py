from playlist import playlist
from music_function import logo,print_playlist
print(logo)
while True:
    # Print Default list
    print_playlist()
    current_play = input("\nSelect a song to play using number:(1:1) ")
    print(f"\n{playlist[int(current_play[0])-1][0]} - {playlist[int(current_play[0])-1][1][int(current_play[2])-1][1]} playing now....")


    change = input("\nPress C to change song or any letter to quit APP: ")
    if change == "C":
        continue
    else:
        break

print("Good Bye!")



