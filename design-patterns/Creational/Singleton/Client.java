public class Client {
    public static void main(String[] args) {
        Database d1 = Database.INSTANCE;
        Database d2 = Database.INSTANCE;

        System.out.println(d1);
        System.out.println(d2);
    }
}
