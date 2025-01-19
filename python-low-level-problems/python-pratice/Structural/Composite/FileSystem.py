from abc import ABC, abstractmethod

class FileSystem:
    @abstractmethod
    def ls(self):
        pass

class File(FileSystem):
    def __init__(self, fileName: str):
        self.fileName = fileName
    
    def ls(self):
        print(f"File name is {self.fileName}")


class Directory(FileSystem):
    def __init__(self, directoryName):
        self.directoryName = directoryName
        self.fileSystemList = []

    def add(self, fileSystem: FileSystem):
        self.fileSystemList.append(fileSystem)       

    def ls(self):
        print(f"Directory name {self.directoryName}")
        for fileSystem in self.fileSystemList:
            fileSystem.ls()

movieDirectory = Directory("Movie")
border = File("Border")
movieDirectory.add(border)

comedyMovieDirectory = Directory("ComedyMovie")
dhol = File("Dhol")
comedyMovieDirectory.add(dhol)
movieDirectory.add(comedyMovieDirectory)

movieDirectory.ls()