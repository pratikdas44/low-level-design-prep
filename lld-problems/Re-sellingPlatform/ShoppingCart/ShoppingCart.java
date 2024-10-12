package ShoppingCart;

import Products.Product;

import java.util.ArrayList;
import java.util.List;

public class ShoppingCart {
    private List<CartObserver> observers = new ArrayList<>();
    private List<Product> items = new ArrayList<>();

    public void addObserver(CartObserver cartObserver){
        this.observers.add(cartObserver);
    }

    public void removeObserver(CartObserver cartObserver){
        this.observers.remove(cartObserver);
    }

    public void addItem(Product item){
        items.add(item);
        notifyObservers();
    }

    public List<Product> getItems(){
        return items;
    }

    private void notifyObservers(){
        for(CartObserver cartObserver: observers){
            cartObserver.update(this);
        }
    }
}
