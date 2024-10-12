package DataIngestion;

public class TrafficSensor extends DataSource{
    public void detectTraffic(String trafficData){
        notifyAll(trafficData);
    }
}
