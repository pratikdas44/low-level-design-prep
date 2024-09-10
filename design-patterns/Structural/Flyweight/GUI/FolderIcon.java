package GUI;

// Concrete Flyweight class representing a Folder Icon
public class FolderIcon implements Icon {
    private String color;  // Intrinsic state: color of the folder icon
    private String image;   // Intrinsic state: image specific to the folder icon

    public FolderIcon(String color, String image) {
        this.color = color;
        this.image = image;
    }

    @Override
    public void draw(int x, int y) {
        // Draw logic specific to folder icon using intrinsic state (image)
        System.out.println("Drawing folder icon with color " + color + " at position (" + x + ", " + y + ")");
    }
}
