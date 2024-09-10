package Strategy.Arithmetic;

public class Main {
    public static void main(String[] args) {
        Context context = new Context();
        context.setStrategy(new Addition());
        context.execute(2, 3);
    }
}
