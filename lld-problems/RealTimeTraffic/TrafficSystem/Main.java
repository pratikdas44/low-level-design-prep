package TrafficSystem;

import DataIngestion.RealTimeProcessor;
import DataIngestion.TrafficSensor;

public class Main {
    public static void main(String[] args) {
        TrafficSensor sensor = new TrafficSensor();
        RealTimeProcessor processor = new RealTimeProcessor();
        sensor.add(processor);
        sensor.detectTraffic();
    }
}
