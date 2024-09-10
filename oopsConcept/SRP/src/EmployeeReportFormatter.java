public class EmployeeReportFormatter extends ReportFormatter{
    private Employee employee;
    private String formatType;

    public EmployeeReportFormatter(Employee employee, String formatType) {
        this.employee = employee;
        this.formatType = formatType;
    }
}
