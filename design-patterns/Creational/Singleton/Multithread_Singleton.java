public class Multithread_Singleton {
    private static Multithread_Singleton dbc = null;
    private Multithread_Singleton(){

    }

    public static Multithread_Singleton getInstance(){
        if(dbc == null){
            synchronized(dbc){
                if(dbc == null){
                    dbc = new Multithread_Singleton();
                }
            }
        }
        return dbc;
    }
}
