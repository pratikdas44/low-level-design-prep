public class Main {
    public static void main(String[] args) {
        LivingThings fish = new Fish(new WaterBreatheImplementor());
        fish.breathingProcess();
    }
}
