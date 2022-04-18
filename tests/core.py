import unittest
from unittest import TestCase

from play_list import MusicPlaylist
from module.core import *


class TestMusicPlaylist(TestCase):

    def test_insert_head(self):
        track1 = Track(artist="BTS", song="Dynamite", release=2020)
        track2 = Track(artist="BTS", song="Permission to Dance", release=2021)
        play_list = MusicPlaylist()
        play_list.insert_head(track1)
        play_list.insert_head(track2)
        self.assertEqual(play_list.head.data, track2)

    def test_insert_end(self):
        track1 = Track(artist="BTS", song="Dynamite", release=2020)
        track2 = Track(artist="BTS", song="Permission to Dance", release=2021)
        track3 = Track(artist="BTS", song="MIC Drop", release=2017)
        play_list = MusicPlaylist()
        play_list.insert_head(track1)
        play_list.insert_head(track2)

        play_list.insert_end(track3)
        temp = play_list.head
        while temp.next is not None:
            temp = temp.next
        self.assertEqual(temp.data, track3)

    def test_insert_at(self):
        track1 = Track(artist="BTS", song="Dynamite", release=2020)
        track2 = Track(artist="BTS", song="Permission to Dance", release=2021)
        track3 = Track(artist="BTS", song="MIC Drop", release=2017)
        track4 = Track(artist="BTS", song="IDOL", release=2018)
        index = 3

        play_list = MusicPlaylist()
        play_list.insert_end(track1)
        play_list.insert_end(track2)
        play_list.insert_end(track3)
        play_list.insert_at(track4, index)

        temp = play_list.head  # Initialise temp
        count = 1  # Index of current node

        # Loop while end of linked list is not reached
        while temp:
            if count == index:
                break
            count += 1
            temp = temp.next

        self.assertEqual(temp.data, track4)

    def test_count_nodes(self):

        track1 = Track(artist="BTS", song="Dynamite", release=2020)
        track2 = Track(artist="BTS", song="Permission to Dance", release=2021)
        track3 = Track(artist="BTS", song="MIC Drop", release=2017)
        track4 = Track(artist="BTS", song="IDOL", release=2018)

        play_list = MusicPlaylist()
        play_list.insert_end(track1)
        play_list.insert_end(track2)
        play_list.insert_end(track3)
        play_list.insert_end(track4)

        self.assertEqual(play_list.count_nodes(), 4)

    def test_search(self):
        track1 = Track(artist="BTS", song="Dynamite", release=2020)
        track2 = Track(artist="BTS", song="Permission to Dance", release=2021)
        track3 = Track(artist="BTS", song="MIC Drop", release=2017)
        track4 = Track(artist="BTS", song="IDOL", release=2018)

        play_list = MusicPlaylist()
        play_list.insert_end(track1)
        play_list.insert_end(track2)
        play_list.insert_end(track3)
        play_list.insert_end(track4)

        self.assertTrue(play_list.search(track1))

    def test_delete_selected(self):
        track1 = Track(artist="BTS", song="Dynamite", release=2020)
        track2 = Track(artist="BTS", song="Permission to Dance", release=2021)
        track3 = Track(artist="BTS", song="MIC Drop", release=2017)
        track4 = Track(artist="BTS", song="IDOL", release=2018)

        play_list = MusicPlaylist()
        play_list.insert_end(track1)
        play_list.insert_end(track2)
        play_list.insert_end(track3)
        play_list.insert_end(track4)

    def test_delete_head(self):
        track1 = Track(artist="BTS", song="Dynamite", release=2020)
        track2 = Track(artist="BTS", song="Permission to Dance", release=2021)
        track3 = Track(artist="BTS", song="MIC Drop", release=2017)
        track4 = Track(artist="BTS", song="IDOL", release=2018)

        play_list = MusicPlaylist()
        play_list.insert_end(track1)
        play_list.insert_end(track2)
        play_list.insert_end(track3)
        play_list.insert_end(track4)
        play_list.delete_head()

        self.assertFalse(play_list.search(track1))

    def test_delete_end(self):
        track1 = Track(artist="BTS", song="Dynamite", release=2020)
        track2 = Track(artist="BTS", song="Permission to Dance", release=2021)
        track3 = Track(artist="BTS", song="MIC Drop", release=2017)
        track4 = Track(artist="BTS", song="IDOL", release=2018)

        play_list = MusicPlaylist()
        play_list.insert_end(track1)
        play_list.insert_end(track2)
        play_list.insert_end(track3)
        play_list.insert_end(track4)

        play_list.delete_end()

        self.assertFalse(play_list.search(track4))

    def test_delete_at(self):
        track1 = Track(artist="BTS", song="Dynamite", release=2020)
        track2 = Track(artist="BTS", song="Permission to Dance", release=2021)
        track3 = Track(artist="BTS", song="MIC Drop", release=2017)
        track4 = Track(artist="BTS", song="IDOL", release=2018)

        play_list = MusicPlaylist()
        play_list.insert_end(track1)
        play_list.insert_end(track2)
        play_list.insert_end(track3)
        play_list.insert_end(track4)

        play_list.delete_at(2)

        self.assertFalse(play_list.search(track2))

    def test_delete_all(self):
        track1 = Track(artist="BTS", song="Dynamite", release=2020)
        track2 = Track(artist="BTS", song="Permission to Dance", release=2021)
        track3 = Track(artist="BTS", song="MIC Drop", release=2017)
        track4 = Track(artist="BTS", song="IDOL", release=2018)

        play_list = MusicPlaylist()
        play_list.insert_end(track1)
        play_list.insert_end(track2)
        play_list.insert_end(track3)
        play_list.insert_end(track4)

        self.assertEqual(play_list.count_nodes(), 4)
        play_list.delete_all()
        self.assertEqual(play_list.count_nodes(), 0)

    def test_get(self):
        track1 = Track(artist="BTS", song="Dynamite", release=2020)
        track2 = Track(artist="BTS", song="Permission to Dance", release=2021)
        track3 = Track(artist="BTS", song="MIC Drop", release=2017)
        track4 = Track(artist="BTS", song="IDOL", release=2018)

        play_list = MusicPlaylist()
        play_list.insert_end(track1)
        play_list.insert_end(track2)
        play_list.insert_end(track3)
        play_list.insert_end(track4)

        self.assertEqual(len(play_list.get()), 4)


if __name__ == '__main__':
    unittest.main()
