// Lazy initialization
public class Singleton {
    private static Singleton dbc = null;
    private Singleton(){

    }

    public static Singleton getInstance(){
        if(dbc == null){
            dbc = new Singleton();
        }
        return dbc;
    }
}

// Eager initialization
// public class Singleton {
//     private static Singleton dbc = new Singleton();
//     private Singleton(){

//     }

//     public static Singleton getInstance(){
//         return dbc;
//     }
// }

