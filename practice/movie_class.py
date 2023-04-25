

class Movie:
    # Default constructor
    def __init__(self):
        self.name = ""
        self.year_of_release = -1
        self.genre = ""

    #  Parameterised constructor of the Movie class
    def __init__(self, n, y, g):
        self.name = n
        self.year_of_release = y
        self.genre = g

    def get_movie_name(self):
        return self.name

    def get_year_of_release(self):
        return self.year_of_release

    def get_movie_genre(self):
        return self.genre

    def print_movie_details(self):
        print("Movie name: ", self.name)
        print("Year: ", self.year_of_release)
        print("Genre: ", self.genre)


def main():
    movie = Movie("Lagaan", 2002, "Family")

    movie.print_movie_details()


if __name__ == "__main__":
    main()
