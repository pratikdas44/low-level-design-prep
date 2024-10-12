package DataIngestion;

public class FactoryImpl {
    public static void main(String[] args) {
        DataProcessor trafficProcessor = DataProcessorFactory.getDataProcessor("traffic");
        if(trafficProcessor != null){
            trafficProcessor.process("Traffic data to process ");
        }
    }
}
