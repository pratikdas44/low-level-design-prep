package UserInterface;

import java.util.ArrayList;
import java.util.List;

public class TrafficMode {
    private List<String> trafficData = new ArrayList<>();
    public List<String> getTrafficData(){
        return trafficData;
    }

    public void setTrafficData(List<String> trafficData){
        this.trafficData = trafficData;
    }
}
