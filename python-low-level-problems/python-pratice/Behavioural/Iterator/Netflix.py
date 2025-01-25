from abc import ABC, abstractmethod

class Iterator(ABC):
    @abstractmethod
    def hasNext(self):
        pass
    @abstractmethod
    def next(self):
        pass

class Container(ABC):
    @abstractmethod
    def createIterator(self):
        pass
        
class NetflixMove(Container):
    def __init__(self):
        self.movies = [
            "ABCD",
            "Deadpool"
        ]

    def createIterator(self):
        return self.MovieIterator(self.movies)
    
    class MovieIterator(Iterator):
        def __init__(self, movies):
            self.movies = movies
            self.index = 0

        def hasNext(self):
            return self.index < len(self.movies)
        
        def next(self):
            if self.hasNext():
                movie = self.movies[self.index]
                self.index += 1
                return movie
            return None
        
movies = NetflixMove()
iterator = movies.createIterator()

while iterator.hasNext():
    print(iterator.next())

            