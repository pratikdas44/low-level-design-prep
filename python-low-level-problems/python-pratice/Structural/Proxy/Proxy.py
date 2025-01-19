from abc import ABC, abstractmethod

# Interface
class Image(ABC):
    @abstractmethod
    def display(self) -> None:
        pass

# Real Subject
class RealImage(Image):
    def __init__(self, filename: str) -> None:
        self._filename = filename
        self._load_image_from_disk()
    
    def _load_image_from_disk(self) -> None:
        print(f"Loading image: {self._filename}")
    
    def display(self) -> None:
        print(f"Displaying image: {self._filename}")

# Proxy
class ProxyImage(Image):
    def __init__(self, filename: str) -> None:
        self._filename = filename
        self._real_image: RealImage | None = None
    
    def display(self) -> None:
        if self._real_image is None:
            self._real_image = RealImage(self._filename)
        self._real_image.display()

# Client code
def main():
    image = ProxyImage("example.jpg")
    
    # Image will be loaded from disk only when display() is called
    image.display()
    
    # Image will not be loaded again, as it has been cached in the Proxy
    image.display()

if __name__ == "__main__":
    main()