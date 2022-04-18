from module.core import *


class MusicPlaylist:
    #  initialising a constructor for the double linked list
    def __init__(self) -> object:
        self.head: Node = None

    # Add new element at the start of the list
    def insert_head(self, new_element: Track):
        #  creating a new node
        newNode = Node(new_element)
        #  checking if there are elements in the list
        if self.head is None:  # if empty make the new node the head
            self.head = newNode
            return
        else:  # if there are nodes in the list set the prev of the initial head to the new node
            self.head.prev = newNode
            newNode.next = self.head  # set the next of the new node to point to the previous head
            self.head = newNode  # make the new node the head
        print("The song has been successfully added to the head")

    # Add new element at the end of the list
    def insert_end(self, new_element: Track):
        #  creating a new node
        newNode = Node(new_element)
        #  checking if there are elements in the list
        if self.head is None:
            self.head = newNode  # if empty make the new node the head
            return
        else:  # if there are nodes in the list move to the last node starting from the head
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            # make the pointer of the last node to point to the newly added node
            temp.next = newNode
            newNode.prev = temp  # set the prev pointer of the new node point to the previously last node
        print("The song has been successfully added to the end")

    # Inserts a new element at the given position
    def insert_at(self, new_element: Track, position):
        # create a new node
        newNode = Node(new_element)
        # check if position is less than 1
        if position < 1:
            print("\nposition should be >= 1.")
        elif position == 1:  # if the position is 1
            newNode.next = self.head  # set the next pointer of new node is the current head
            self.head.prev = newNode  # set the previous pointer of the current head to the new node
            self.head = newNode  # make the new node the head
        else:  # if position is any other number
            temp = self.head  # make a temporal variable with its value as head
            for i in range(1, position - 1):  # loop through the list until the given index-1 to get the node before
                # where we are inserting
                if temp is not None:
                    temp = temp.next
            if temp is not None:
                newNode.next = temp.next  # set the next pointer of the new node to the next pointer of the current node
                newNode.prev = temp  # set the previous pointer of the new node to the current node
                temp.next = newNode  # set the next pointer of the current node to the new node
                if newNode.next is not None:
                    newNode.next.prev = newNode  # set the
            else:
                print("\nThe previous node is null.")

    # count nodes in the list
    def count_nodes(self):
        # create a temp node pointing to head
        temp = self.head
        # initialise the count from zeo
        count = 0
        # loop through the list until there is no other node
        while temp is not None:
            count += 1
            temp = temp.next
        print("The playlist has ", count, " songs")
        return count

    # Search an element
    def search(self, value):
        found = False  # initialise the found to false since the search hasn't begun
        index = 0  # initialise the index at zero where the search will begin

        temp = self.head  # set the temp to point at the head
        if temp is not None:  # if temp is not none run the while loop
            while temp is not None:  # while loop runs as long as temp is not none
                index += 1  # update the index
                if temp.data == value:  # if the temp is equal to the value we are searching
                    found = True  # update the found to true
                    print("The song ", value, " is in the index ", index)
                    break
                else:
                    temp = temp.next  # else update the temp to the next node
            return found
        else:
            print("Song not found")
            return False

    # delete selected element
    def delete_selected(self, value: str):
        # create a temp node pointing to head
        temp: Node = self.head

        #  if temp node is not null, loop through the list until the search value is found
        if temp is not None:
            while temp is not None:
                if str(temp.data) == value:
                    if temp.prev is not None:
                        temp.prev.next = temp.next
                        temp = None
                        break
                    else:
                        self.head = temp.next
                        temp = None
                        break
                temp = temp.next

        self.print()

    def delete_head(self):

        if self.head is not None:

            # if head is not null, create a temp node pointing to head
            temp = self.head

            #  move head to next of head
            self.head = self.head.next

            # delete temp node
            temp = None

            # If the new head is not null, then make prev of the new head as null
            if self.head is not None:
                self.head.prev = None

    # Delete last node of the list
    def delete_end(self):
        # check if we have a  node in the list
        if self.head is not None:
            # check if we have a node after the head, if not we delete the head
            if self.head.next is None:
                self.head = None
            else:  # if we have a node after the head we loop through the entire list until the last node then delete it
                temp = self.head
                while temp.next.next is not None:
                    temp = temp.next
                lastNode = temp.next
                temp.next = None  # this deletes it from the memory
                lastNode = None  # this deletes the head from the memory
        print("The song has been successfully deleted")

    # Delete an element at the given position
    def delete_at(self, position):
        # check if index is less than 1
        if position < 1:
            print("\nposition should be >= 1.")

        elif position == 1 and self.head is not None:  # if the position is 1, it means we are deleting the head
            nodeToDelete = self.head
            self.head = self.head.next  # move the head to the next node
            nodeToDelete = None
            if self.head is not None:
                self.head.prev = None  # set the previous pointer of the head to none
        else:  # if position is any other number,iterate through the list until the position
            temp = self.head
            for i in range(1, position - 1):
                if temp is not None:
                    temp = temp.next
            if temp is not None and temp.next is not None:
                nodeToDelete = temp.next
                temp.next = temp.next.next
                if temp.next.next is not None:
                    temp.next.next.prev = temp.next
                nodeToDelete = None  # this deletes the head from the memory
            else:
                print("\nThe node is already null.")

        # delete all nodes of the list

    def delete_all(self):
        # if the head is not null , move it to the next node until there is no node left
        while self.head is not None:
            temp = self.head
            self.head = self.head.next
            temp = None  # this deletes the head from the memory
        print("All nodes are deleted successfully.")

    # display the content of the list
    def print(self):
        temp = self.head
        if temp is not None:
            print("The list contains:", end="\n")
            while temp is not None:
                print(temp.data, end="\n")
                temp = temp.next
            print()
        else:
            print("The list is empty.")

    def get(self):
        result: list[Track] = []
        temp: Node = self.head
        if temp is not None:
            while temp is not None:
                result.append(temp.data)
                temp = temp.next
        return result


# Driver code
if __name__ == "__main__":
    playlist = MusicPlaylist()
    track1 = Track(artist="BTS", song="Dynamite", release=2020)
    track2 = Track(artist="BTS", song="Permission to Dance", release=2021)
    track3 = Track(artist="BTS", song="MIC Drop", release=2017)
    track4 = Track(artist="BTS", song="IDOL", release=2018)
    track5 = Track(artist="BTS", song="Watch till", release=2016)
    playlist.insert_head(track1)
    playlist.insert_end(track2)
    playlist.insert_at(track3, 2)
    playlist.insert_head(track4)
    playlist.insert_head(track5)
    playlist.print()
    playlist.count_nodes()
    playlist.search(track4)
    playlist.delete_head()
    playlist.delete_end()
    playlist.delete_at(4)
    playlist.delete_all()
