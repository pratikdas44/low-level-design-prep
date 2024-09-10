package mediator.Airplane;

public class TrafficControllerImpl implements TrafficController {

    @Override
    public void requestTakeOff(Airplane airplane){
        airplane.notifyTrafficController("Request takeoff");
    }

    @Override
    public void requestLanding(Airplane airplane){
        airplane.notifyTrafficController("Request Landing");
    }
}
