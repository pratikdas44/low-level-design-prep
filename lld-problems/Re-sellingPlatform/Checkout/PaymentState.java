package Checkout;

public class PaymentState implements Checkout{
    @Override
    public void handle(CheckoutContext checkoutContext){
        System.out.println("Shipping address entered ");
        checkoutContext.setState(new ReviewState());
    }
}
