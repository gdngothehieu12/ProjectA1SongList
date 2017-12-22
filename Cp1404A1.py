#Name:Ngô Thế Hiếu
#Date:21/12/2017
#Brief program details : Listing the songs that you can keep track if you have or haven't learned
#Github:https://github.com/gdngothehieu12/ProjectA1SongList


""'Program displays a list of songs of user which is either marked as learned or unlearned'
"User can add songs to list or mark songs as completed based on preference "
''''''''''''''''''''''''''

"Pseudocode"
#open csv file songs.csv
#return songs
def load_songs():
    songs=open("songs.csv","r+")
    return songs
''''''
"Pseudocode"
"Function: Main"
#Output the welcoming message
#Activate function load_songs()
#Output the number of songs loaded from songs.csv
#Activate function menu
#Output the number of songs saved to csv
#Display a farewell message
def main():
    print("Songs to learn 1.0 - by Ngô Thế Hiếu")
    list = load_songs()
    songs = list.readlines()
    print("{} songs loaded ".format(len(songs)))
    songs = sortSongs(songs)
    newSong = menu(songs)
    print("{} songs saved to songs.csv ".format(len(songs)))
    newSong = listToString(newSong)
    list.seek(0)
    list.truncate()
    list.write(newSong)
    list.close()
    print("Have a nice day :)")
''''''''''''''
"Function: Main"
"Usage: In this function , the program displays the menu table for the user to choose whether to list songs, add songs or complete songs."

def menu(songs):
    while True:
        print("Menu:")
        print("L - List songs")
        print("A - Add new song")
        print("C - Complete a song")
        print("Q - Quit")
        choice = input().upper()
        if choice == "L":
            songs = list_songs(songs)
        elif choice == "A":
            songs = add_song(songs)
        elif choice == "C":
            songs = complete_songs(songs)
        elif choice == "Q":
            return songs
        else:
            print("Invalid menu choice")
''''''''
"Function:list_songs"
"Usage:In this function , the program calculates the number of learned song and unlearned song from songs.csv and display the song list from songs.csv"

def list_songs(songs):
    count = -1
    songnumCount = 0
    songCount = 0
    for each in songs:
        count += 1
        if each[3]=="n":
            print("{:2}.   {:50}-by {:30}({:3}) ".format(count, each[0], each[1], each[2]))
        else:
            print("{:2}.*  {:50}-by {:30}({:3}) ".format(count, each[0], each[1], each[2]))
        if each[3] == 'y':
            songnumCount += 1
        songCount += 1
        learned_count = songCount - songnumCount
    print(" {} marked as learned , {} still more to learn".format(learned_count, songnumCount))
    return songs
''
"Function add_song"
"Usage: Adding songs to the list song in songs csv"
def add_song(songs):
    learned_count=2
    while True:
        title = input("Title: ")
        if title == "":
            print("Input cannot be blank")
        else:
            break
    while True:
        artist = input("Artist: ")
        if artist == "":
            print("Input cannot be blank")
        else:
            break
    while True:
        try:
            year = int(input("Year: "))
            if year < 0:
                print("Number must be >= 0")
            else:
                break
        except ValueError:
            print("Invalid input; enter a valid number")


    print(title, "by ",artist,"(", year, ") added to song list ")
    songs.append([title, artist, year,"y",])
    songs = sortSongs(songs)
    return songs
''
"Function complete_songs"
"Pseudocode:"
"Check whether every songs in songs.csv is completed if there is song required to complete continue"
"Using for loop to check each in songs has yet been learned all"
"Activate function list_songs() and load list of songs"
"output message that asks for the song number user wants to complete"
"User input song number"
"Program check whether that song is learnt to either display a proper message for user"
"If song is learnt already , display a message telling user that song is learnt"
"If song hasn't been learned , continue and display a message telling user that song has been learnt "
"Return songs"
def complete_songs(songs):
    required=0
    for each in songs:
        if each[3]=="y":
            required=1
        if required==0:
            print("No song required completed")
            return songs
    list_songs(songs)
    print("Enter the number of song marked as learned")
    while True:
        song_num=int(input(""))
        try:
            if songs[song_num][3]=="n":
                print("That song is already learned")
                break
            else:
                print("{} by {} marked as learned".format(songs[song_num][0],songs[song_num][1]))
                songs[song_num][3]="n"
                break
        except ValueError:
            print("Invalid input; enter a valid number")
    return songs
'Function sortSongs'
"Usage:Sorted the list of songs so it will follow in an alphabet order"
def sortSongs(songs):
    sortedList = []
    for each in songs:
        try:
            each = each.strip().split(",")
        except AttributeError:
            pass
        sortedList.append(each)
    newList = sorted(sortedList, key=lambda x:int(x[2]))
    newList = sorted(newList, key=lambda x:x[1])
    return newList
def listToString(songs):
    newString = ""
    for each in songs:
        for word in each:
            newString += str(word)+","
        newString = newString[:-1]
        newString += "\n"
    return newString

main()
