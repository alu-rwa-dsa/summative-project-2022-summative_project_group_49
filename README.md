#SOLUTION

# PROJECT NAME: Music Playlist Management.
** VERSION 1.0.0
####About: It demonstrates a music playlist using a double linked list so that transversing can be easy

Data Structure used: Double linked list

The IDE used is Pycharm

##In Pycharm

MusicPlaylist Management has four major operations:
###1.Adding
This is sub_divided into three other sub_operations
1. Adding a song to the beginning of the playlist
2. Adding a song to the end of the playlist
3. Adding a song in between existing songs
###2.Deleting
This is sub_divided into four other sub_operations
1. Deleting the song in the beginning of the playlist
2. Deleting a song in the end of the playlist
3. Deleting a selected song
4. Deleting the entire playlist
### 3.Counting
Count the number of songs in the playlist

###4. Searching
Searching for a particular song in the playlist

### Displaying
This displays the songs in the playlist

Data Structure used: Double linked list because it allows one to add the head, or between nodes, delete the head or any of the selected nodes. 
It also keeps track of the previous node and the next node. This allows access to the list from both directions 
#Time complexities in O
1. Searching O(n)
2. Inserting head O(1)
3. Inserting the tail O(1)
4. Inserting between nodes O(n) where n is the number of items in the list
5. Deleting head O(1)
6. Deleting tail O(1)
7. Deleting between nodes o(n) where n is the number of items in the list
8. Counting the nodes O(n)

# Output: in Pycharm
Running the playlist methods:
if __name__ == "__main__":
  * playlist = MusicPlaylist()
  * track1 = Track(artist="BTS", song="Dynamite", release=2020)
  * track2 = Track(artist="BTS", song="Permission to Dance", release=2021)
  * track3 = Track(artist="BTS", song="MIC Drop", release=2017)
  * track4 = Track(artist="BTS", song="IDOL", release=2018)
  * track5 = Track(artist="BTS", song="Watch till", release=2016)
  * playlist.insert_head(track1)
  * playlist.insert_end(track2)
  * playlist.insert_at(track3, 2)
  * playlist.insert_head(track4)
  * playlist.insert_head(track5)
  * playlist.print()
  * playlist.count_nodes()
  * playlist.search(track4)
  * playlist.delete_head()
  * playlist.delete_end()
  * playlist.delete_at(4)
  * playlist.delete_all()
  * 
Running the play_list.py file  give the following output:

  * The list contains:
  * Artist: BTS, Song: Watch till, Release: 2016
  * Artist: BTS, Song: IDOL, Release: 2018
  * Artist: BTS, Song: Dynamite, Release: 2020
  * Artist: BTS, Song: MIC Drop, Release: 2017
  * Artist: BTS, Song: Permission to Dance, Release: 2021

  * The playlist has  5  songs
  * The song  Artist: BTS, Song: IDOL, Release: 2018  is in the index  2
  * The song has been successfully deleted

  * The node is already null.
  * All nodes are deleted successfully.
# Community benefits 
First it offers additional operations than those in a convectional playlist. For example in convectional playlist for example Spotify, the 
music is added to the end only. For one to move a song to the beginning you have to drag the song to the very top which is very inconvenient. In 
this project I have addressed this issue by giving the user the option to insert the song wherever they want, at the beginning, at the end, at a certain position by a simple button click. For example you already have a playlist and you want to add the song to the top
you simply click on add to the top.
One can also delete the song in the beginning and end of the playlist in an instance without the need of selecting the song. Furthermore the user can see the
total number of the songs in the playlist.




