package DataIngestion;

public class RealTimeProcessor implements Obserer{
    @Override
    public void update(String data){
        System.out.println("Processing real time traffic data " + data);
    }
}
