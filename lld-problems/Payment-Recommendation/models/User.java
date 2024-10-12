package models;

import java.util.HashMap;
import java.util.Map;

public class User {
    private String userId;
    private String name;
    private Map<String, Double> paymentPreferences;

    public User(String userId, String name){
        this.userId = userId;
        this.name = name;
        this.paymentPreferences = new HashMap<>();
        paymentPreferences.put("CREDIT_CARD:VISA", 0.8);
        paymentPreferences.put("CREDIT_CARD:Mastercard", 0.9);
        paymentPreferences.put("UPI:GooglePay", 0.7);
    }

    public String getUserId() {
        return userId;
    }

    public void setUserId(String userId) {
        this.userId = userId;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Map<String, Double> getPaymentPreferences() {
        return paymentPreferences;
    }

    public void setPaymentPreferences(Map<String, Double> paymentPreferences) {
        this.paymentPreferences = paymentPreferences;
    }
}
