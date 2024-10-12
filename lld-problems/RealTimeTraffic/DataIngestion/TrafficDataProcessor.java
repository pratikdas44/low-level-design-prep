package DataIngestion;

public class TrafficDataProcessor implements DataProcessor{
    @Override
    public void process(String data){
        System.out.println("Traffic data processed " + data);
    }
}
