package DataIngestion;

public class DataProcessorFactory {
    public static DataProcessor getDataProcessor(String datatype){
        if("traffic".equals(datatype)){
            return new TrafficDataProcessor();
        }
        return null;
    }
}
