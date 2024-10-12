package PaymentInstructions;

import models.User;
import Cart.Cart;
import java.util.List;
public interface PaymentRecommendationStrategy {
    List<Payment> recommendPaymentInstruction(Cart cart, User user);
}
