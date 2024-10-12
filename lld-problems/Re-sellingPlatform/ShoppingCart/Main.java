package ShoppingCart;

import Products.Product;

public class Main {
    public static void main(String[] args) {
        ShoppingCart cart = new ShoppingCart();
        cart.addObserver(new CartLogger());
        cart.addItem(new Product(1, "product 1", "category", 100.0));
    }
}
