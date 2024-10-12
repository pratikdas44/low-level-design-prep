package DataStorage;

public class DatabaseConnectionImpl {
    public static void main(String[] args) {
        DatabaseConnectionPool databaseConnectionPool = new DatabaseConnectionPool();
        DatabaseConnection databaseConnection = databaseConnectionPool.getConnection();
        databaseConnection.executeQuery("SELET * from Traffic_data");
        databaseConnectionPool.releaseConnection(databaseConnection);
    }
}
