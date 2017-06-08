import media
import fresh_tomatoes

# import media to make Movie objects, each movie object includes
# title, storyline, movie poster, and trailer
dark_knight = media.Movie("The Dark Knight",
                          "A guy running around in a bat costume.",
                          "https://images-na.ssl-images-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_UY1200_CR90,0,630,1200_AL_.jpg",  # noqa
                          "https://www.youtube.com/watch?v=kmJLuwP3MbY")

the_matrix = media.Movie("The Matrix",
                         "A documentary about a man who is peer pressured \
                         into taking a pill. \
                         Afterwards, thinking he has superpowers.",
                         "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",  # noqa
                         "https://www.youtube.com/watch?v=vKQi3bBA1y8")

star_wars_i = media.Movie("Star Wars: Episode I - The Phantom Menace",
                          "A man with a colorful light wand kidnaps a child, \
                          because he believes he'"'s "the chosen one".',
                          "https://images-na.ssl-images-amazon.com/images/"
                          "M/MV5BM2FmZGIwMzAtZTBkMS00M2JiLTk2MDctM2FlNTQ2OWYwZDZkXkEyXkFqcGdeQXVyNDYyMDk5MTU@._V1_UX182_CR0,0,182,268_AL_.jpg",  # noqa
                          "https://www.youtube.com/watch?v=bD7bpG-zDJQ")

# makes a list of movies and then calls the open_movies_page in
# fresh_tomatoes to open a web page in browser.
movies = [dark_knight, the_matrix, star_wars_i]
fresh_tomatoes.open_movies_page(movies)
