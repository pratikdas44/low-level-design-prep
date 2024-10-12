package Checkout;

public class ShippingAddress implements Checkout{
    @Override
    public void handle(CheckoutContext checkoutContext){
        System.out.println("Shipping address entered ");
        checkoutContext.setState(new PaymentState());
    }
}
