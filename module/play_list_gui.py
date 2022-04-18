import tkinter as tk
from tkinter import messagebox, SUNKEN, BOTTOM, X

from module.play_list import MusicPlaylist
from module.core import *


class MyWindow:
    def __init__(self, win: tk.Tk):
        # creating the labels
        self.search_entry = None
        self.artist_label = tk.Label(win, text='Artist')
        self.song_label = tk.Label(win, text='Song')
        self.release_label = tk.Label(win, text='Release Year')

        self.music_list = MusicPlaylist()
        # creating the tables for data entry
        self.artist_table = tk.Entry(bd=3)
        self.song_table = tk.Entry()
        self.release_table = tk.Entry()

        # create the positions for the labels and tables on the x and y-axis
        self.artist_label.place(x=100, y=50)
        self.artist_table.place(x=200, y=50)
        self.song_label.place(x=100, y=100)
        self.song_table.place(x=200, y=100)
        self.release_label.place(x=100, y=50)
        self.release_table.place(x=200, y=50)
        self.release_label.place(x=100, y=150)
        self.release_table.place(x=200, y=150)

        # creating the add front button
        self.add_button = tk.Button(win, text='Add Front', command=self.add)
        self.add_button.place(x=100, y=200)

        # creating the add end button
        self.add_end_button = tk.Button(win, text='Add End', command=lambda: self.add(False))
        self.add_end_button.place(x=200, y=200)

        # creating the add at button
        self.add_at_button = tk.Button(win, text='Add Before', command=self.add_before)
        self.add_at_button.place(x=300, y=200)

        # create the listbox
        self.playlist = tk.Listbox(win, width=50, height=50)
        self.playlist.pack(padx=100, pady=300, fill=tk.BOTH, expand=True)

        # add a delete selected button
        self.front_delete_button = tk.Button(win, text='Delete selected', command=self.delete)
        self.front_delete_button.place(x=300, y=250)

        # add a delete head button
        self.end_delete_button = tk.Button(win, text='Delete head', command=self.delete_front)
        self.end_delete_button.place(x=100, y=250)

        # add a delete end button
        self.end_delete_button = tk.Button(win, text='Delete End', command=self.delete_end)
        self.end_delete_button.place(x=200, y=250)

        # add a delete all button
        self.delete_all_button = tk.Button(win, text='Delete all', command=self.delete_all)
        self.delete_all_button.place(x=400, y=250)

        # add a count button
        self.count_button = tk.Button(win, text='Count', command=self.count)
        self.count_button.place(x=400, y=200)

    # function for adding the track
    def add(self, head=True):
        artist = self.artist_table.get()
        song = self.song_table.get()
        release = int(self.release_table.get())
        track = Track(artist, song, release)
        if head:  # if head is true add the track to the list
            self.music_list.insert_head(track)
        else:  # if false add the track to the end
            self.music_list.insert_end(track)

        self.playlist.delete(0, 'end')  # Deleting the listbox playlist
        self.playlist.insert('end', *self.music_list.get())  # inserting the music

    # tab for deleting at a certain position by selection
    def delete(self):
        for item in self.playlist.curselection():  # select song to delete
            value = self.playlist.get(item)  # get the value of the song in the listbox
            askquestion = messagebox.askquestion("Delete", "Are you certain you want to delete?")
            if askquestion == "yes":  # message box for asking
                # user if they want to delete
                self.music_list.delete_selected(value)  # deleting the song in the music list object
                self.playlist.delete(item)  # deleting the selected item in the listbox

    # Function for deleting the head in the list
    def delete_front(self, head=True):
        if head:
            askquestion = messagebox.askquestion("Delete",
                                                 "Are you certain you want to delete?")  # message box for asking
            # user if they want to delete
            if askquestion == "yes":
                self.music_list.delete_head()  # delete the head in the music list object
                self.playlist.delete(0)  # deleting the head in the listbox object

    # function for deleting the last track in the list
    def delete_end(self, head=True):
        if head:
            askquestion = messagebox.askquestion("Delete",
                                                 "Are you certain you want to delete?")  # message box for asking
            # user if they want to delete
            if askquestion == "yes":
                self.music_list.delete_end()  # delete the head in the music list object
                label = self.playlist.get("end")  # getting the value of the last item in the list box
                if label is not None:
                    index = self.playlist.get(0, tk.END).index(label)  # getting the index of the last track in the
                    # listbox
                    self.playlist.delete(index)  # deleting the head in the listbox object
            else:
                messagebox.showerror("Error", "There is no track in the playlist")

    def delete_all(self):
        askquestion = messagebox.askquestion("Delete", "Are you certain you want to delete?")
        if askquestion == "yes":  # message box for asking
            # user if they want to delete
            self.music_list.delete_all()
            self.playlist.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "There is no track in the playlist")

    def add_before(self):
        artist = self.artist_table.get()
        song = self.song_table.get()
        release = int(self.release_table.get())
        track = Track(artist, song, release)
        for item in self.playlist.curselection():  # select song where you want to insert
            index = self.playlist.index(item)  # get the index of the song in the listbox we are to add before
            self.music_list.insert_at(track, index + 1)  # inserting the song in the music list object
            self.playlist.delete(0, 'end')  # Deleting the listbox playlist
            self.playlist.insert('end', *self.music_list.get())

    def count(self, head=True):
        if head is not None:
            self.music_list.count_nodes()
            messagebox.showinfo('There are the below number of tracks in the playlist ', self.playlist.size())
        else:
            messagebox.showerror("Error", "There is no track in the playlist")


# creating the root window
root = tk.Tk()

# creating an object for the class MyWindow
window = MyWindow(root)

# create the menu button
menubar = tk.Menu(root)
root.config(menu=menubar)  # set the menu to the top and makes it able to accept submenus

# creating the submenu
sub_menu = tk.Menu(menubar, tearoff=0)  # tear off removes the space in the submenu
menubar.add_cascade(label="File", menu=sub_menu)  # add the submenus
sub_menu.add_command(label="Open")  # add commands inside the submenu
sub_menu.add_command(label="Exit", command=root.destroy)  # add commands inside the submenu


# create a function for frequently asked questions so that it can display the questions
def faqs():
    messagebox.showinfo('Questions', 'Why this GUI? Its the most efficient way to create a music playlist')


# function for the website submenu
def website():
    messagebox.showinfo('Website', 'https://www.MusicPlaylist.com ')


sub_menu = tk.Menu(menubar, tearoff=0)  # tear off removes the space in the submenu
menubar.add_cascade(label="Help", menu=sub_menu)  # add the submenus
sub_menu.add_command(label="Website", command=website)  # add commands inside the submenu
sub_menu.add_command(label="FAQs", command=faqs)  # add commands inside the submenu

# creating a title for the window
root.title('Create Playlist')

# create the icon of the main root
root.iconbitmap(r'images/music_icon.ico')

# create a label for the main  root
title = tk.Label(root, text="Define your music world")
title.pack(pady=10)  # move the label to the root and add a padding of 10

# Get the current screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the geometry of frame
root.geometry("{0}x{1}".format(screen_width, screen_height))  # making the screen maximum by default

# creating the status bar
status_bar = tk.Label(root, text="Welcome", relief=SUNKEN)
status_bar.pack(side=BOTTOM, fill=X)  # Status bar set to the bottom and fill the entire x_axis


def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()


root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
