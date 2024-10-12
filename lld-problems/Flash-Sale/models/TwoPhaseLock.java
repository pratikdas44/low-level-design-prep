package models;

import java.util.concurrent.TransferQueue;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class TwoPhaseLock implements ConcurrencyControlStrategy{
    private final Lock lock = new ReentrantLock();

    @Override
    public void acquireLock(){
        lock.lock();
    }

    @Override
    public void releaseLock(){
        lock.unlock();
    }

    @Override
    public boolean validateTransaction(Transaction transaction){
        return true;
    }
}
