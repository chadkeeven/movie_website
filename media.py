import webbrowser

class Movie():
    """ This class provides a way to store movie related information """
    # Creates the movie object, showing that it takes in 4 parameters to create the object.
    # The movie object holds the title of the movie, the storyline, the url for the movie's
    # poster image, and the url for the trailer of the movie on youtube.
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    # Uses the youtube url stored in the movie object to open a browser and play the trailer for the movie.
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
    
    
