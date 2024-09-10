public class EmployeeDAO {
    private Employee employee;
    private DBConnection dbConnection;

    public EmployeeDAO(Employee employee) {
        this.employee = employee;
        this.dbConnection = new DBConnection();
    }

    public void saveEmployee(Employee employee){
        dbConnection.save();
    }

    public void deleteEmployee(Employee employee){
        dbConnection.delete();
    }
}
