package PaymentInstructions;

import Cart.CartItem;
import java.util.List;
import java.util.Set;

public interface PaymentComputationStrategy {
    Set<String> computePaymentMethods(List<CartItem> cartItemList);
}
