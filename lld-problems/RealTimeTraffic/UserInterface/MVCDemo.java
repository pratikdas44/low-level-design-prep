package UserInterface;

public class MVCDemo {
    public static void main(String[] args) {
        TrafficMode trafficMode = new TrafficMode();
        TrafficView trafficView = new TrafficView();
        TrafficController trafficController = new TrafficController(trafficMode, trafficView);
        trafficController.updateView();
    }
}
