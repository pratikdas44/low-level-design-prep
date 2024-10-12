package DecisionMaking;

public class StrategyDemo {
    public static void main(String[] args) {
        DistanceContext distanceContext = new DistanceContext();
        DistanceStrategy fixedTraffic = new FixedTrafficSignal();
        distanceContext.setDistanceStrategy(fixedTraffic);
        distanceContext.execute();
    }
}
