package CommunicationLayer;

public class TrafficSystemFacade {
    private TrafficAPI trafficAPI;
    private WeatherAPI weatherAPI;

    public TrafficSystemFacade(TrafficAPI trafficAPI, WeatherAPI weatherAPI) {
        this.trafficAPI = trafficAPI;
        this.weatherAPI = weatherAPI;
    }

    public String getTrafficData(){
        return trafficAPI.fetchData();
    }

    public String getWeatherData(){
        return weatherAPI.fetchData();
    }
}
