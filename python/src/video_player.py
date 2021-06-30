"""A video player class."""

from .video_library import VideoLibrary
from .video_playlist import Playlist
import random

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self._current_video = None
        self._playing = True

        self._playlist_list = []

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        print("Here's a list of all available videos:")

        list1 = []
        for x in self._video_library.get_all_videos():

            list0 = []
            for tag in x.tags:
                list0.append(tag)

            tags = ""
            for tag in list0:
                tags += tag + " "

            list1.append([x.title, "(" + x.video_id + ")", "[" + tags[:-1] + "]" ])
        
        list1.sort(key = lambda x: x[0])
        for video in list1:
            print(video[0], video[1], video[2])

    def play_video(self, video_id):
        """Plays the respective video.
        Args:
            video_id: The video_id to be played.
        """

        id_title_dic = {}
        for video in self._video_library.get_all_videos():
            id_title_dic[video.video_id] = video.title

        id_list = []
        for video in self._video_library.get_all_videos():
            id_list.append(video.video_id)
        
        if not video_id in id_list:
            print("Cannot play video: Video does not exist")
        elif self._current_video == None:
            self._current_video = video_id
            print("Playing video:", id_title_dic[self._current_video])
            self._playing = True
        else:
            print("Stopping video:", id_title_dic[self._current_video])
            self._current_video = video_id
            print("Playing video:", id_title_dic[self._current_video])
            self._playing = True

    def stop_video(self):
        """Stops the current video."""

        id_title_dic = {}
        for video in self._video_library.get_all_videos():
            id_title_dic[video.video_id] = video.title

        if self._current_video == None:
            print("Cannot stop video: No video is currently playing")
        else:
            print("Stopping video:", id_title_dic[self._current_video])
            self._current_video = None

    def play_random_video(self):
        """Plays a random video from the video library."""

        id_list = []
        for video in self._video_library.get_all_videos():
            id_list.append(video.video_id)

        if id_list == []:
            print("No videos avaliable")
        else:
            self.play_video(random.choice(id_list))

    def pause_video(self):
        """Pauses the current video."""

        id_title_dic = {}
        for video in self._video_library.get_all_videos():
            id_title_dic[video.video_id] = video.title

        if self._current_video == None:
            print("Cannot pause video: No video is currently playing")
        elif self._playing == False:
            print("Video already paused:", id_title_dic[self._current_video])
        else:
            print("Pausing video:", id_title_dic[self._current_video])
            self._playing = False

    def continue_video(self):
        """Resumes playing the current video."""

        id_title_dic = {}
        for video in self._video_library.get_all_videos():
            id_title_dic[video.video_id] = video.title

        if self._current_video == None:
            print("Cannot continue video: No video is currently playing")
        elif self._playing == True:
            print("Cannot continue video: Video is not paused")
        else:
            print("Continuing video:", id_title_dic[self._current_video])
            self._playing = True

    def show_playing(self):
        """Displays video currently playing."""

        if self._current_video == None:
            print("No video is currently playing")
        else:
            for video in self._video_library.get_all_videos():
                if video.video_id == self._current_video:
                    playing = video

            list0 = []
            for tag in playing.tags:
                list0.append(tag)

            tags = ""
            for tag in list0:
                tags += tag + " "

            if self._playing == True:
                print("Currently playing:", playing.title, "(" + playing.video_id + ")", "[" + tags[:-1] + "]")
            else:
                print("Currently playing:", playing.title, "(" + playing.video_id + ")", "[" + tags[:-1] + "]", "- PAUSED")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """

        name_list = []
        for playlist in self._playlist_list:
            name_list.append(playlist.name.lower())
        
        if playlist_name.lower() in name_list:
            print("Cannot create playlist: A playlist with the same name already exists")
        else:
            self._playlist_list.append(Playlist(playlist_name))
            print("Successfully created new playlist:", playlist_name)

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """

        # id_list = []
        # for video in self._video_library.get_all_videos():
        #     id_list.append(video.video_id)

        # name_list = []
        # for playlist in self._playlist_list:
        #     name_list.append(playlist.name.lower())

        # if self._playlist_list == []:
        #     print("Cannot add video to another_playlist: Playlist does not exist")
        # elif not video_id in id_list:
        #     print("Cannot add video to my_playlist: Video does not exist")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
