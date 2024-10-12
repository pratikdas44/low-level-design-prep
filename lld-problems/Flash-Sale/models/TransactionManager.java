package models;

public class TransactionManager {
    public void beganTransaction(){
        System.out.println("Transaction started");
    }

    public void commitTransaction(){
        System.out.println("Transaction commited");
    }

    public void rollbackTransaction(){
        System.out.println("Transaction rolled back");
    }
}
