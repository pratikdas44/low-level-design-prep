package Checkout;

public class CheckoutContext {
    private Checkout checkout;

    public CheckoutContext(){
        this.checkout = new ShippingAddress();
    }

    public void setState(Checkout checkoutStage){
        this.checkout = checkoutStage;
    }


    public void request(){
        checkout.handle(this);
    }
}
