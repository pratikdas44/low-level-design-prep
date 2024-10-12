package models;

import java.util.*;
public class TransactionLimitManager {
    private static TransactionLimitManager instance;
    private Map<String, Double> transactionLimits;

    private TransactionLimitManager(){
        transactionLimits = new HashMap<>();
        transactionLimits.put("CREDIT_CARD",5000.00);
        transactionLimits.put("DEBIT_CARD", 2000.00);
        transactionLimits.put("UPI", 3999.00);
    }

    public static synchronized TransactionLimitManager getInstance(){
        if(instance == null){
            instance = new TransactionLimitManager();
        }
        return instance;
    }

    public double getTransactionLimit(String paymentType){
        return transactionLimits.getOrDefault(paymentType, 0.0);
    }

    public void setTransactionLimits(String paymentType, double limit){
        transactionLimits.put(paymentType, limit);
    }


}
