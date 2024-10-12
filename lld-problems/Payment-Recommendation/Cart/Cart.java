package Cart;

import java.util.ArrayList;
import java.util.List;

public class Cart {
    private List<CartItem> cartItemList;
    private double totalAmount;

    public Cart(){
        cartItemList = new ArrayList<>();
        totalAmount = 0.0;
    }

    public List<CartItem> getCartItemList() {
        return cartItemList;
    }

    public void setCartItemList(List<CartItem> cartItemList) {
        this.cartItemList = cartItemList;
    }

    public double getTotalAmount() {
        return totalAmount;
    }

    public void setTotalAmount(double totalAmount) {
        this.totalAmount = totalAmount;
    }

    public void addItem(CartItem cartItem){
        cartItemList.add(cartItem);
        totalAmount += cartItem.getItemPrice();
    }
}
