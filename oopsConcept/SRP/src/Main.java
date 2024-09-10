public class Main {
    public static void main(String[] args) {
        Employee employee = new Employee(1, "pratik", "IT", true);
        EmployeeDAO employeeDAO = new EmployeeDAO(employee);
        employeeDAO.saveEmployee(employee);
        EmployeeReportFormatter employeeReportFormatter = new EmployeeReportFormatter(employee, "CSV");
        employeeReportFormatter.getFormattedEmployee("CSV");
    }
}