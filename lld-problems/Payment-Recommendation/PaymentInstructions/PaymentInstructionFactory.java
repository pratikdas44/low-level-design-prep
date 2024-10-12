package PaymentInstructions;

public interface PaymentInstructionFactory {
    Payment createPaymentInstrument(String type, String issuer, double relevanceScore);
}
