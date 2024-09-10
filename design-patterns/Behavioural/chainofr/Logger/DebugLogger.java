package Logger;

public class DebugLogger extends Logger{
    public DebugLogger(int levels) {  
        this.levels=levels;  
    }
     
    @Override  
    protected void displaylogInfo(String msg) {  
        System.out.println("DEBUG LOGGER INFO: "+msg);  
    }  
}
