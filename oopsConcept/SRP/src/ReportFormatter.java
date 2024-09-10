public abstract class ReportFormatter {
    public void converttoXML(){

    }

    public void converttoCSV(){

    }

    public void getFormattedEmployee(String formatType){
        if(formatType.equals("CSV")){
            converttoCSV();
        }
        else if(formatType.equals("XML")){
            converttoXML();
        }
        else{
            System.out.println("invalid type");
        }
    }
}
