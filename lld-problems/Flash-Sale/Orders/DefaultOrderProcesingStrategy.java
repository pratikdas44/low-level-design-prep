package Orders;

import models.InventoryManagement;

public class DefaultOrderProcesingStrategy implements OrderProcessing{
    @Override
    public void processOrder(Order order, InventoryManagement inventoryManagement) {
        FlashSaleOrder flashSaleOrder = (FlashSaleOrder) order;
        if(inventoryManagement.checkAvailibility(flashSaleOrder.getProduct(), flashSaleOrder.getQuantity())){
            System.out.println("Processing order for product: " + flashSaleOrder.getProduct().getId() + " Quantity " + flashSaleOrder.getQuantity());
            inventoryManagement.updateInventory(flashSaleOrder.getProduct(), -flashSaleOrder.getQuantity());
        }
        else{
            System.out.println("Insufficient stock for Product: " + flashSaleOrder.getProduct().getId());
        }
    }
}
