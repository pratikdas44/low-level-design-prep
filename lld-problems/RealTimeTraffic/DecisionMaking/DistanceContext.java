package DecisionMaking;

public class DistanceContext {
    private DistanceStrategy distanceStrategy;
    public void setDistanceStrategy(DistanceStrategy distanceStrategy){
        this.distanceStrategy = distanceStrategy;
    }
    
    public void execute(){
        distanceStrategy.distance();
    }
}
