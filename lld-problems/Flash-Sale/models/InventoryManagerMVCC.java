package models;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.atomic.AtomicInteger;

public class InventoryManagerMVCC {
    private ConcurrentHashMap<Product, AtomicInteger> inventory;
    private InventoryManagerMVCC(){
        inventory = new ConcurrentHashMap<>();
    }

    public void updateInventory(Product product, int quantity){
        inventory.compute(product, (key, value) -> {
            if(value == null){
                return new AtomicInteger(quantity);
            }
            else{
                value.addAndGet(quantity);
                return value;
            }
        });
    }

    public boolean checkAvailability(Product product, int quantity){
        return inventory.getOrDefault(product, new AtomicInteger(0)).get() >= quantity;
    }
}
