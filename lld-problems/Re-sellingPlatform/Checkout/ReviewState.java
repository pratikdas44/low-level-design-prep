package Checkout;

public class ReviewState implements Checkout{
    @Override
    public void handle(CheckoutContext checkoutContext){
        System.out.println("Shipping address entered ");
    }
}