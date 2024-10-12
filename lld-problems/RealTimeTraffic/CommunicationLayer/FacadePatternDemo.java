package CommunicationLayer;

public class FacadePatternDemo {
    public static void main(String[] args) {
        TrafficSystemFacade facade = new TrafficSystemFacade(new TrafficAPI(), new WeatherAPI());
        System.out.println(facade.getWeatherData());
        System.out.println(facade.getTrafficData());
    }
}
