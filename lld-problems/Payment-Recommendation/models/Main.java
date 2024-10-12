package models;
import Cart.Cart;
import Cart.CartItem;
import PaymentInstructions.Payment;
import PaymentInstructions.PaymentComputationStrategy;
import PaymentInstructions.PaymentComputationStrategyFactory;
import PaymentInstructions.PaymentRecommendationStrategyImpl;

import java.util.*;
public class Main {
    public static void main(String[] args) {
        Set<String> supportedMethods1 = new HashSet<>(Arrays.asList("CREDIT_CARD:VISA", "UPI:GooglePay"));
        CartItem cartItem1 = new CartItem("Item1", 100.0, LineofBusiness.COMMERCE_PURCHASE, supportedMethods1);

        Set<String> supportedMethods2 = new HashSet<>(Arrays.asList("CREDIT_CARD:VISA", "CREDIT_CARD:MasterCard", "UPI:GooglePay"));
        CartItem cartItem2 = new CartItem("Item1", 200.0, LineofBusiness.CREDIT_CARD_BILL, supportedMethods2);

        Cart cart = new Cart();
        cart.addItem(cartItem1);
        cart.addItem(cartItem2);

        User user = new User("user1", "PDB");
        PaymentComputationStrategyFactory paymentComputationStrategy = new PaymentComputationStrategyFactory();
        PaymentComputationStrategy computationStrategy = paymentComputationStrategy.createComputationStrategy("common");

        PaymentRecommendationStrategyImpl recommendationStrategy = new PaymentRecommendationStrategyImpl(computationStrategy);
        List<Payment> recommendInstruments = recommendationStrategy.recommendPaymentInstruction(cart, user);

        for(Payment payment: recommendInstruments){
            payment.pay(cart.getTotalAmount());
        }

    }
}
