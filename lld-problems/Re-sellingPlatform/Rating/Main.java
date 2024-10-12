package Rating;

public class Main {
    public static void main(String[] args) {
        Review review1 = new Review("Good", 5);
        Review review2 = new Review("Poor", 2);
        ReviewCollection collection = new ReviewCollection();
        collection.add(review1);
        collection.add(review2);
        collection.display();
    }
}
