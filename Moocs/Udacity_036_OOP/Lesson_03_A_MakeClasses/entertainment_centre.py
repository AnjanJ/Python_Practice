import fresh_tomatoes
import media

#toy_story = media.Movie()

avatar = media.Movie("Avatar","A paraplegic Marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.","http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg","http://youtu.be/cRdxXPV9GNQ")

movie_300 = media.Movie("300","300 is a 2007 American fantasy war film based on the 1998 comic series of the same name by Frank Miller and Lynn Varley. Both are fictionalized retellings of the Battle of Thermopylae within the Persian Wars.","http://upload.wikimedia.org/wikipedia/en/5/5c/300poster.jpg","http://youtu.be/wDiUG52ZyHQ")

nebraska = media.Movie("Nebraska","An aging, booze-addled father makes the trip from Montana to Nebraska with his estranged son in order to claim a million-dollar Mega Sweepstakes Marketing prize.","http://upload.wikimedia.org/wikipedia/en/7/76/Nebraska_Poster.jpg","http://youtu.be/aA98dqgJBgQ")


movies = [avatar,movie_300,nebraska]
fresh_tomatoes.open_movies_page(movies)
