package Cart;

import models.LineofBusiness;

import java.util.Set;

public class CartItem {
    private String itemName;
    private double itemPrice;
    private LineofBusiness lineofBusiness;
    private Set<String> supportedPaymentMethods;

    public CartItem(String itemName, double itemPrice, LineofBusiness lineofBusiness, Set<String> supportedPaymentMethods) {
        this.itemName = itemName;
        this.itemPrice = itemPrice;
        this.lineofBusiness = lineofBusiness;
        this.supportedPaymentMethods = supportedPaymentMethods;
    }

    public String getItemName() {
        return itemName;
    }

    public void setItemName(String itemName) {
        this.itemName = itemName;
    }

    public double getItemPrice() {
        return itemPrice;
    }

    public void setItemPrice(double itemPrice) {
        this.itemPrice = itemPrice;
    }

    public Set<String> getSupportedPaymentMethods() {
        return supportedPaymentMethods;
    }

    public void setSupportedPaymentMethods(Set<String> supportedPaymentMethods) {
        this.supportedPaymentMethods = supportedPaymentMethods;
    }

    public LineofBusiness getLineofBusiness() {
        return lineofBusiness;
    }

    public void setLineofBusiness(LineofBusiness lineofBusiness) {
        this.lineofBusiness = lineofBusiness;
    }
}
