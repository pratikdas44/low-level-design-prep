package DataStorage;

import javax.xml.crypto.Data;
import java.util.ArrayList;
import java.util.List;

public class DatabaseConnectionPool {
    private List<DatabaseConnection> databaseConnections = new ArrayList<>();
    public DatabaseConnection getConnection(){
        if(databaseConnections.isEmpty()){
            return new DatabaseConnection();
        }
        else{
            return databaseConnections.remove(0);
        }
    }

    public void releaseConnection(DatabaseConnection databaseConnection){
        databaseConnections.add(databaseConnection);
    }
}
