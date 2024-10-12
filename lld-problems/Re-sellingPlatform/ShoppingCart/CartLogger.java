package ShoppingCart;

public class CartLogger implements CartObserver{
    @Override
    public void update(ShoppingCart cart){
        System.out.println("Cart updated. Total items are: " + cart.getItems().size());
    }
}
