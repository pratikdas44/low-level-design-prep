package mediator.Airplane;

public class Client {
    public static void main(String[] args) {
        TrafficController controlTower = new TrafficControllerImpl();
 
        // Instantiate Concrete Colleagues (Commercial Airplanes)
        Airplane airplane1 = new AirplaneImpl(controlTower);
        Airplane airplane2 = new AirplaneImpl(controlTower);
 
        // Set up the association between Concrete Colleagues and the Mediator
        airplane1.requestTakeoff();
        airplane2.requestLanding();
    }
}
