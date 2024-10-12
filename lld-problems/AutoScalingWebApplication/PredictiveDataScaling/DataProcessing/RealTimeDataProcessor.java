package PredictiveDataScaling.DataProcessing;

import java.util.ArrayList;
import java.util.List;

public class RealTimeDataProcessor {
    private List<Observer> observerList;

    public RealTimeDataProcessor(){
        this.observerList = new ArrayList<>();
    }

    public void addObserver(Observer o){
        this.observerList.add(o);
    }

    public void removeObserver(Observer o){
        this.observerList.remove(o);
    }

    public void ingestRealTimeData(String msg){
        System.out.println("Incoming msg");
        notifyObserver();
    }

    public void notifyObserver(){
        for(Observer o : observerList){
            o.update("Incoming data");
        }
    }
}
