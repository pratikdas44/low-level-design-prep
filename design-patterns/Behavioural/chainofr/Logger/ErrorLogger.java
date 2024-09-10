package Logger;

public class ErrorLogger extends Logger{
    public ErrorLogger(int levels) {  
        this.levels=levels;  
    }
     
    @Override  
    protected void displaylogInfo(String msg) {  
        System.out.println("ERROR LOGGER INFO: "+msg);  
    }  
}
