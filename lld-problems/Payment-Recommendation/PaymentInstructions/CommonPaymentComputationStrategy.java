package PaymentInstructions;

import Cart.CartItem;

import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class CommonPaymentComputationStrategy implements PaymentComputationStrategy{
    @Override
    public Set<String> computePaymentMethods(List<CartItem> cartItemList){
        if(cartItemList.isEmpty()){
            return new HashSet<>();
        }
        Set<String> commonPaymentMethods = new HashSet<>(cartItemList.get(0).getSupportedPaymentMethods());
        for(int i=1;i<cartItemList.size();i++){
            commonPaymentMethods.retainAll(cartItemList.get(i).getSupportedPaymentMethods());
        }
        return commonPaymentMethods;
    }
}
