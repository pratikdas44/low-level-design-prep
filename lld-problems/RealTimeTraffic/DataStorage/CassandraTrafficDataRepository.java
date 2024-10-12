package DataStorage;

public class CassandraTrafficDataRepository implements TrafficDataRepository{
    @Override
    public void storeData(String trafficData){
        System.out.println("Data stored in Cassandra " + trafficData);
    }
}
