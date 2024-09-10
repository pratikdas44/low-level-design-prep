package Logger;

public abstract class Logger {
    public static int OUTPUTINFO=1;  
    public static int ERRORINFO=2;  
    public static int DEBUGINFO=3; 
    private Logger logger;
    protected int levels;

    public void nextLogger(Logger logger){
        this.logger = logger;
    }

    protected abstract void displaylogInfo(String msg);

    public void logMessage(int levels, String msg){
        if(this.levels <= levels){
            displaylogInfo(msg);
        }
        if(this.logger != null){
            this.logger.logMessage(levels, msg);
        }
    }
}
