package observer.Weather;

public class Main {
    public static void main(String[] args) {
        WeatherStation weatherStation = new WeatherStation();

        IObserver phoneDisplay = new PhoneDisplay();
        IObserver tvDisplay = new TVDisplay();

        weatherStation.addObserver(phoneDisplay);
        weatherStation.addObserver(tvDisplay);

        // Simulating weather change
        weatherStation.setWeather("Sunny");
    }
}
