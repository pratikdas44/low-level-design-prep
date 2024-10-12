package Orders;

import models.InventoryManagement;

public interface OrderProcessing {
    void processOrder(Order order, InventoryManagement inventoryManagement);
}
