

from abc import ABC, abstractmethod
from typing import Dict

# Interface for Icon
class Icon(ABC):
    @abstractmethod
    def draw(self, x: int, y: int) -> None:
        pass

# Concrete Flyweight for File Icons
class FileIcon(Icon):
    def __init__(self, type_: str, image: str) -> None:
        self._type = type_  # Intrinsic state
        self._image = image  # Intrinsic state
    
    def draw(self, x: int, y: int) -> None:
        # Draw logic specific to file icon using intrinsic state
        print(f"Drawing {self._type} icon at position ({x}, {y})")

# Concrete Flyweight for Folder Icons
class FolderIcon(Icon):
    def __init__(self, color: str, image: str) -> None:
        self._color = color  # Intrinsic state
        self._image = image  # Intrinsic state
    
    def draw(self, x: int, y: int) -> None:
        # Draw logic specific to folder icon using intrinsic state
        print(f"Drawing {self._color} folder icon at position ({x}, {y})")

# Flyweight Factory
class IconFactory:
    def __init__(self):
        self._icon_cache: Dict[str, Icon] = {}
    
    def get_icon(self, key: str) -> Icon:
        # Check if the icon already exists in the cache
        if key in self._icon_cache:
            return self._icon_cache[key]
        
        # Create a new icon based on the key (type of icon)
        if key == "file":
            icon = FileIcon("document", "document.png")
        elif key == "folder":
            icon = FolderIcon("blue", "folder.png")
        else:
            raise ValueError(f"Unsupported icon type: {key}")
        
        # Store the created icon in the cache
        self._icon_cache[key] = icon
        return icon

# Client code
def main():
    icon_factory = IconFactory()

    # Draw file icons at different positions
    file_icon1 = icon_factory.get_icon("file")
    file_icon1.draw(100, 100)

    file_icon2 = icon_factory.get_icon("file")
    file_icon2.draw(150, 150)

    # Draw folder icons at different positions
    folder_icon1 = icon_factory.get_icon("folder")
    folder_icon1.draw(200, 200)

    folder_icon2 = icon_factory.get_icon("folder")
    folder_icon2.draw(250, 250)

if __name__ == "__main__":
    main()