package PaymentInstructions;

public class CreditCardPayment implements Payment{
    private String type;
    private String issuer;
    private double relevanceScore;


    public CreditCardPayment(String type, String issuer, double relevanceScore) {
        this.issuer = issuer;
        this.relevanceScore = relevanceScore;
        this.type = type;
    }

    @Override
    public void pay(double amount){
        System.out.println("Payment of " + amount + " made using " + issuer + " " + type + " credit card with score " + relevanceScore);
    }
}
