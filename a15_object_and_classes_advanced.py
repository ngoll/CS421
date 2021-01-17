#create movie class
class Movie:
    def __init__(self, name, year, songs):
        self.name = name
        self.year = year
        self.songs = songs

    def __repr__(self):
        return 'Movie(name=%s, year=%s, songs=%s)' % (self.name, self.year, self.songs)

    def __str__(self):
        return 'Movie(name=%s, year=%s, songs=%s)' % (self.name, self.year, self.songs)

#create song class
class Song:
    def __init__(self, name, lyricist, singers):
        self.name = name
        self.lyricist = lyricist
        self.singers = singers

    def __repr__(self):
        return 'Song(name=%s, lyricist=%s, singers=%s)' % (self.name, self.lyricist, self.singers)
    def __str__(self):
        return 'Song(name=%s, lyricist=%s, singers=%s)' % (self.name, self.lyricist, self.singers)

#create person class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
  
    def __repr__(self):  
       return 'Person(name=%s, age=%s)' % (self.name, self.age)
    
    def __str__(self):   
       return 'Person(name=%s, age=%s)' % (self.name, self.age)

#create people
person_1 = Person("Ananta Sriram", 36)
person_2 = Person("Damani Bhatala", 24)
person_3 = Person("Karthik", 40)
person_4 = Person("Ramajogayya Sastry", 50)
person_5 = Person("Ramya Behara", 26)
person_6 = Person("Deepu" , 34)

#print people
print("People: ")
print(person_1)
print(person_2)
print(person_3)
print(person_4)
print(person_5)
print(person_6)
print()

#create songs
singers_1 = [person_2, person_3]
song_1 = Song("Pacha Bottasi", person_1, singers_1)

singers_2 = [person_5, person_6]
song_2 = Song("Dheevara", person_4, singers_2)

#print songs
print("Songs: ")
print(song_1)
print(song_2)
print()

#create a movie
songs = [song_1, song_2]
movie_1 = Movie("Baahubali", 2015, songs)

#print movie
print("Movie: ")
print(movie_1)

