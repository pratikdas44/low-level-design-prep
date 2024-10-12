package DataStorage;

public class RepositoryPatternImpl {
    public static void main(String[] args) {
        TrafficDataRepository trafficDataRepository = new CassandraTrafficDataRepository();
        trafficDataRepository.storeData("Traffic data to store");
    }
}
