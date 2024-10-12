package models;

import java.util.*;
public class InventoryManagement {
    private static InventoryManagement inventoryManagement;
    private Map<Product, Integer> inventory;
    private InventoryManagement(){
        inventory = new HashMap<>();
    }

    public static synchronized InventoryManagement getInstance(){
        if(inventoryManagement == null){
            inventoryManagement = new InventoryManagement();
        }
        return inventoryManagement;
    }

    public synchronized void updateInventory(Product product, int quantity){
        int curr = inventory.getOrDefault(product, 0);
        inventory.put(product, curr + quantity);
    }

    public synchronized boolean checkAvailibility(Product product, int quantity){
        return inventory.getOrDefault(product, 0) >= quantity;
    }

}
