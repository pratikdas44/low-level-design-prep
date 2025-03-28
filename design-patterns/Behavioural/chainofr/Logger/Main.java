package Logger;

public class Main {
    private static Logger doChaining(){  
        Logger consoleLogger = new ConsoleLogger(Logger.OUTPUTINFO);  
          
        Logger errorLogger = new ErrorLogger(Logger.ERRORINFO);  
        consoleLogger.nextLogger(errorLogger);  
          
        Logger debugLogger = new DebugLogger(Logger.DEBUGINFO);  
        errorLogger.nextLogger(debugLogger);  
          
        return consoleLogger;   
        }  
        public static void main(String args[]){  
        Logger chainLogger= doChaining();  

            chainLogger.logMessage(Logger.OUTPUTINFO, "Enter the sequence of values ");  
            chainLogger.logMessage(Logger.ERRORINFO, "An error is occured now");  
            chainLogger.logMessage(Logger.DEBUGINFO, "This was the error now debugging is compeled");  
            }  
}
