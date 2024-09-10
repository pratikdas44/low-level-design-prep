package Strategy.Arithmetic;

public class Context {
    private Strategy strategy;
    public void setStrategy(Strategy strategy){
        this.strategy = strategy;
    }

    public void execute(int a, int b){
        this.strategy.execute(a,b);
    }
}
