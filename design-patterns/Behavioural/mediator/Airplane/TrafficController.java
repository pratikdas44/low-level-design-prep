package mediator.Airplane;

public interface TrafficController {
    public void requestTakeOff(Airplane airplane);
    public void requestLanding(Airplane airplane);
}
