class RentMovies:
    def __init__(self,movie_list):
        self.avaliable_movies = movie_list
    
    def show_avaliable_movies(self):
        for movie in self.avaliable_movies:
            print(movie)

    def rent_movie(self,requested_movie):
        if requested_movie in self.avaliable_movies:
            print('Ok, Movie was rented for you :)')
            self.avaliable_movies.remove(requested_movie)
        else:
            print('Sorry we don\'t have this movie')

    def add_movie(self,returned_movie):
        self.avaliable_movies.append(returned_movie)
        print('Thanks, the movie was returned with success')

class Costumer:
    
    def request_movie(self):
        print('Input the movie\'s name you want to rent: ')
        self.movie_name = input()
        return self.movie_name
   
        
    def return_movie(self):
        print('Input the movie\'s name you will return: ')
        self.movie_name = input()
        return self.movie_name

movie_list  = ['It','SuperMan','Batman']
rent_movies = RentMovies(movie_list)
costumer = Costumer()

print('Welcome . \n')
print('Choose one of the options bellow:')

print('Enter 1 to show the avaliable movies ')
print('Enter 2 to request for a movie')
print('Enter 3 to return a movie')
print('Enter 4 to exit')


while True:
    user_option = int(input())
    if user_option is 1:
        rent_movies.show_avaliable_movies()
    elif user_option is 2:
        requested_movie = costumer.request_movie()
        rent_movies.rent_movie(requested_movie)
    elif user_option is 3:
        returned_movie = costumer.return_movie()
        rent_movies.add_movie(returned_movie)
    elif user_option is 4:
        quit()

