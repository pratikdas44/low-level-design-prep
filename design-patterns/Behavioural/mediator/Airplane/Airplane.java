package mediator.Airplane;

public abstract class Airplane {
    protected TrafficController trafficController;
    public abstract void requestTakeoff();
    public abstract void requestLanding();
    public abstract void notifyTrafficController(String msg);
}
