package UserInterface;

public class TrafficController {
    private TrafficMode trafficMode;
    private TrafficView trafficView;

    public TrafficController(TrafficMode trafficMode, TrafficView trafficView) {
        this.trafficMode = trafficMode;
        this.trafficView = trafficView;
    }

    public void updateView(){
        trafficView.displayTrafficData(trafficMode.getTrafficData());
    }
}
