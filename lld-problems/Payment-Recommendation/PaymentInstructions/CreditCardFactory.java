package PaymentInstructions;

public class CreditCardFactory implements PaymentInstructionFactory{
    @Override
    public Payment createPaymentInstrument(String type, String issuer, double relevanceScore){
        return new CreditCardPayment(type, issuer, relevanceScore);
    }
}
