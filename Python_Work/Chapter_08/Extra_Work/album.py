def make_album(artist, title, num_songs=None):
    album = {"artist": artist, "title": title}
    if num_songs:  # Only add if provided
        album["songs"] = num_songs
    return album

# Make three albums without song count
print(make_album("Michael Jackson", "Thriller"))
print(make_album("Adele", "21"))
print(make_album("Coldplay", "Parachutes"))

# Make an album with song count
print(make_album("Taylor Swift", "1989", 13))