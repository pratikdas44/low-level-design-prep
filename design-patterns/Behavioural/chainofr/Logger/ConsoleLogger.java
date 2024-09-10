package Logger;

public class ConsoleLogger extends Logger{
    public ConsoleLogger(int levels) {  
        this.levels=levels;  
    }
     
    @Override  
    protected void displaylogInfo(String msg) {  
        System.out.println("CONSOLE LOGGER INFO: "+msg);  
    }  
}
