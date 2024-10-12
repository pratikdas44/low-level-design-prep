package Orders;
import models.InventoryManagement;
import models.Product;
public class FlashSaleOrder implements Order{
    private Product product;
    private int quantity;

    public FlashSaleOrder(Product product, int quantity) {
        this.product = product;
        this.quantity = quantity;
    }

    @Override
    public void execute(){
        InventoryManagement inventoryManagement = InventoryManagement.getInstance();
        if(inventoryManagement.checkAvailibility(product, quantity)){
            inventoryManagement.updateInventory(product, -quantity);
            System.out.println("Order processed for Product: " + product.getName() + " Quantity "  + quantity);
        }
        else{
            System.out.println("Insufficient inventory for Product " + product.getName());
        }
    }

    public Product getProduct(){
        return product;
    }

    public int getQuantity(){
        return quantity;
    }
}

















