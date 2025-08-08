def make_album(artist, title, num_songs=None):
    album = {"artist": artist, "title": title}
    if num_songs:
        album["songs"] = num_songs
    return album

print("Enter 'quit' at any time to stop.")

while True:
    artist = input("Enter artist name: ")
    if artist.lower() == "quit":
        break
    
    title = input("Enter album title: ")
    if title.lower() == "quit":
        break
    
    songs = input("Enter number of songs (optional, press Enter to skip): ")
    if songs.lower() == "quit":
        break
    
    # Convert to integer if user entered a number
    if songs.isdigit():
        album_info = make_album(artist, title, int(songs))
    else:
        album_info = make_album(artist, title)
    
    print(f"Album added: {album_info}\n")