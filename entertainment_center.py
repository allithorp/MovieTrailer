"""Movie instances and their data points live in this file"""

#import relevant files
import fresh_tomatoes
import media

#list of Movie instances with data points as arguments
the_royal_tenenbaums = media.Movie("The Royal Tenenbaums",
                                   "An estranged family of former child prodigies"
                                   " reunites when their father announces he is"
                                   " terminally ill.",
                                   "https://images-na.ssl-images-amazon.com/images/M/MV5BYzc3ODYwNDUtNmJmMC00OWJjLWIzYzctNTJjMzY0Mzc4ZDI5XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_CR0,0,620,1000_AL_.jpg",  # NOQA
                                   "https://www.youtube.com/watch?v=8Eg6yIwP2vs")
                                   
requiem_for_a_dream = media.Movie("Requiem for a Dream",
                                  "The drug-induced utopias of four Coney Island"
                                  " people are shattered when their addictions run deep.",
                                  "https://images-na.ssl-images-amazon.com/images/M/MV5BOTdiNzJlOWUtNWMwNS00NmFlLWI0YTEtZmI3YjIzZWUyY2Y3XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,666,1000_AL_.jpg",  # NOQA
                                  "https://www.youtube.com/watch?v=jzk-lmU4KZ4")
return_of_the_king = media.Movie("Lord of the Rings: Return of the King",
                                "Gandalf and Aragorn lead the World of Men"
                                " against Sauron's army to draw his gaze from"
                                " Frodo and Sam as they approach Mount Doom with"
                                " the One Ring.",
                                "https://images-na.ssl-images-amazon.com/images/M/MV5BYWY1ZWQ5YjMtMDE0MS00NWIzLWE1M2YtODYzYTk2OTNlYWZmXkEyXkFqcGdeQXVyNDUyOTg3Njg@._V1_SY1000_SX668_AL_.jpg",  # NOQA
                                "https://www.youtube.com/watch?v=r5X-hFf6Bwo")
crazy_stupid_love = media.Movie("Crazy, Stupid, Love.",
                                "A middle-aged husband's life changes dramatically"
                                " when his wife asks him for a divorce. He seeks to"
                                " rediscover his manhood with the help of a newfound"
                                " friend, Jacob, learning to pick up girls at bars.",
                                "https://images-na.ssl-images-amazon.com/images/M/MV5BMTg2MjkwMTM0NF5BMl5BanBnXkFtZTcwMzc4NDg2NQ@@._V1_SY1000_SX675_AL_.jpg",  # NOQA
                                "https://www.youtube.com/watch?v=aDLhjm-0rJQ")
airplane = media.Movie("Airplane!",
                       "A man afraid to fly must ensure that a plane lands safely"
                       " after the pilots become sick.",
                       "https://images-na.ssl-images-amazon.com/images/M/MV5BNDU2MjE4MTcwNl5BMl5BanBnXkFtZTgwNDExOTMxMDE@._V1_.jpg",
                       "https://www.youtube.com/watch?v=HMnVs287AJ4")
spinal_tap = media.Movie("This is Spinal Tap",
                         "Spinal Tap, one of England's loudest bands, is chronicled "
                         " by film director Marty DeBergi on what proves to be a"
                         " fateful tour.",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BMTQ2MTIzMzg5Nl5BMl5BanBnXkFtZTgwOTc5NDI1MDE@._V1_.jpg",
                         "https://www.youtube.com/watch?v=N63XSUpe-0o")

#array to reference all Movie instances
movies = [the_royal_tenenbaums, requiem_for_a_dream, return_of_the_king, crazy_stupid_love, airplane, spinal_tap]

#function to open webpage - argument references array of all instances
fresh_tomatoes.open_movies_page(movies)


