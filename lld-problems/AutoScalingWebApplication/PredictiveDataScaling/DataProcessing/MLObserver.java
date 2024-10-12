package PredictiveDataScaling.DataProcessing;

public class MLObserver implements Observer{
    @Override
    public void update(String msg){
        System.out.println(msg);
    }
}
