class Playlist:
    def __init__(self, songs):
        self.songs = songs

    def __len__(self):
        return len(self.songs)

p = Playlist("vinay")
print(len(p))  # 3




class Playlist:
    def __init__(self):
        print("vinay")   # Runs when object is created

# create object
c = Playlist()


