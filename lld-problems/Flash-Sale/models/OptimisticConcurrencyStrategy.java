package models;

import Orders.FlashSaleOrder;

public class OptimisticConcurrencyStrategy implements OptimizedConcurrency{
    @Override
    public boolean validateTransaction(Transaction transaction){
        FlashSaleOrder order = (FlashSaleOrder) transaction.getOrder();
        InventoryManagement inventoryManagement = InventoryManagement.getInstance();
        return inventoryManagement.checkAvailibility(order.getProduct(), order.getQuantity());
    }
}
