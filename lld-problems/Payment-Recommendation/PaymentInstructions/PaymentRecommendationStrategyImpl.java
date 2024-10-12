package PaymentInstructions;
import java.util.*;
import models.User;
import Cart.Cart;

public class PaymentRecommendationStrategyImpl implements PaymentRecommendationStrategy{
    private PaymentComputationStrategy computationStrategy;
    public PaymentRecommendationStrategyImpl(PaymentComputationStrategy paymentComputationStrategy){
        this.computationStrategy = paymentComputationStrategy;
    }

    @Override
    public List<Payment> recommendPaymentInstruction(Cart cart, User user){
        Set<String> commonPaymentMethods = computationStrategy.computePaymentMethods(cart.getCartItemList());

        List<Payment> recommendedInstruments = new ArrayList<>();
        PaymentInstructionFactory factory = new CreditCardFactory();
        for(String method: commonPaymentMethods){
            String[] parts = method.split(":");
            String types = parts[0];
            String issuer = parts[1];
            double relevanceScore = 0.9;

            recommendedInstruments.add(factory.createPaymentInstrument(types, issuer, relevanceScore));
        }
        return recommendedInstruments;
    }
}
