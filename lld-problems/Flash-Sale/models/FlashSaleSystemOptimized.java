package models;

import Orders.DefaultOrderProcesingStrategy;
import Orders.FlashSaleOrder;
import Orders.Order;
import Orders.OrderProcessing;

public class FlashSaleSystemOptimized {
    private ConcurrencyControlStrategy concurrencyControlStrategy;
    private InventoryManagement inventoryManagement;
    private OrderProcessing orderProcessing;

    public FlashSaleSystemOptimized(ConcurrencyControlStrategy concurrencyControlStrategy, OrderProcessing orderProcessing) {
        this.concurrencyControlStrategy = concurrencyControlStrategy;
        this.orderProcessing = orderProcessing;
        this.inventoryManagement = InventoryManagement.getInstance();
    }

    public void setConcurrencyControlStrategy(ConcurrencyControlStrategy strategy){
        this.concurrencyControlStrategy = strategy;
    }

    public void setOrderProcessingStrategy(OrderProcessing strategy){
        this.orderProcessing = strategy;
    }

    public void processOrder(Order order) throws InterruptedException{
        TransactionManager transactionManager = new TransactionManager();
        transactionManager.beganTransaction();
        try{
            if(concurrencyControlStrategy.validateTransaction(new Transaction(1,order))) {
                orderProcessing.processOrder(order, inventoryManagement);
                transactionManager.commitTransaction();
            }
            else {
                System.out.println("Transaction validation failed");
                transactionManager.rollbackTransaction();
            }
        } catch(Exception e){
            System.out.println("Error occured " + e);
            transactionManager.rollbackTransaction();
        }
    }

    public static void main(String[] args) throws InterruptedException{
        Product product1 = new Product(1, "Product1");
        Product product2 = new Product(2, "Product2");

        InventoryManagement inventoryManagement = InventoryManagement.getInstance();
        inventoryManagement.updateInventory(product1, 100);
        inventoryManagement.updateInventory(product2, 50);

        ConcurrencyControlStrategy concurrencyControlStrategy1 = new TwoPhaseLock();
        OrderProcessing orderProcessing = new DefaultOrderProcesingStrategy();

        FlashSaleSystem flashSaleSystem = new FlashSaleSystem(concurrencyControlStrategy1, orderProcessing);

        Order order1 = new FlashSaleOrder(product1, 80);
        Order order2 = new FlashSaleOrder(product2, 60);

        Order order3 = new FlashSaleOrder(product1, 80);
        Order order4 = new FlashSaleOrder(product2, 10);

        flashSaleSystem.processOrder(order1);
        flashSaleSystem.processOrder(order2);
        flashSaleSystem.processOrder(order3);
        flashSaleSystem.processOrder(order4);
    }
}

