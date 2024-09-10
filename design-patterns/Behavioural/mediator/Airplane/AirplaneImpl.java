package mediator.Airplane;

public class AirplaneImpl extends Airplane {
    public AirplaneImpl(TrafficController trafficController){
        this.trafficController = trafficController;
    }

    @Override
    public void requestTakeoff() {
        trafficController.requestTakeOff(this);
    }
 
    @Override
    public void requestLanding() {
        trafficController.requestLanding(this);
    }
 
    @Override
    public void notifyTrafficController(String message) {
        System.out.println("Commercial Airplane: " + message);
    }
}
