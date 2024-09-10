public abstract class LivingThings {
    protected BreatheImplementor breatheImplementor;
    public LivingThings(BreatheImplementor breatheImplementor){
        this.breatheImplementor = breatheImplementor;
    }

    abstract public void breathingProcess();
}
