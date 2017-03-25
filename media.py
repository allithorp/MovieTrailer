#import webbrowser for show_trailer function
import webbrowser

#instantiate class Movie
class Movie():
    """ This class provides a way to store movie instance data points"""

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    #initalize class, define attributes and arguments
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
    #function to open trailer url
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
    
    
    
