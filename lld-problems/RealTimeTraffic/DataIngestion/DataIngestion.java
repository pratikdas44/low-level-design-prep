package DataIngestion;

public class DataIngestion {
    public static void main(String[] args) {
        TrafficSensor trafficSensor = new TrafficSensor();
        RealTimeProcessor realTimeProcessor = new RealTimeProcessor();
        trafficSensor.add(realTimeProcessor);
        trafficSensor.detectTraffic("Traffic data from sensor");
    }
}
