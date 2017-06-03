import fresh_tomatoes
import media

#creating multiple instance of class Movie.
wall_e = media.Movie("Wall_E", "Wall E is a Love story of 2 robots",
                          "https://upload.wikimedia.org/wikipedia/en/c/c2/WALL-Eposter.jpg",
                          "https://www.youtube.com/watch?v=8-_9n5DtKOc&ab_channel=YOKID37")


dark_knight = media.Movie("The Dark Knight", "Batman vs Joker",
                          "https://a.ltrbxd.com/resized/sm/upload/78/y5/zg/ej/oefdD26aey8GPdx7Rm45PNncJdU-0-230-0-345-crop.jpg?k=582b0428f7",
                          "https://www.youtube.com/watch?v=_PZpmTj1Q8Q&ab_channel=WarnerBros.")

my_name_is_khan = media.Movie("My Name is Khan", "All Muslims are not terrorists",
                          "http://www.doobeedoobeedoo.info/wp-content/uploads/2010/01/OST-My-Name-Is-Khan-CD-cover.jpg",
                          "https://www.youtube.com/watch?v=_uNDm6YfN2k&ab_channel=obbmusic")

i_robot = media.Movie("I Robot", "Year 2035, Robots go rougue",
                          "http://www.gstatic.com/tv/thumb/movieposters/34586/p34586_p_v8_ap.jpg",
                          "https://www.youtube.com/watch?v=rL6RRIOZyCM&ab_channel=VikiTrailers")

civil_war = media.Movie("Civil War", "Iron Man vs Captain America",
                          "https://images-na.ssl-images-amazon.com/images/M/MV5BMjQ0MTgyNjAxMV5BMl5BanBnXkFtZTgwNjUzMDkyODE@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
                          "https://www.youtube.com/watch?v=dKrVegVI0Us&ab_channel=MarvelEntertainment")

piper = media.Movie("Piper", "Bird learns to catch it's prey",
                          "http://vignette2.wikia.nocookie.net/pixar/images/5/58/Piper_billboards_head2.jpg/revision/latest?cb=20160622154808",
                          "https://www.youtube.com/watch?v=Bz8aUBXV1_w&ab_channel=KinoCheckInternational")

#store the instances of movies in a list.
movies_list = [wall_e, dark_knight, my_name_is_khan, i_robot, civil_war, piper]

#calling open_movies_page method from resh_tomatoes.py file to un the program.
fresh_tomatoes.open_movies_page(movies_list)




