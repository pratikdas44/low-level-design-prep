package models;

import java.util.concurrent.TransferQueue;
import java.util.concurrent.locks.*;
public interface ConcurrencyControlStrategy{
    void acquireLock() throws InterruptedException;
    void releaseLock();
    boolean validateTransaction(Transaction transaction);
}
