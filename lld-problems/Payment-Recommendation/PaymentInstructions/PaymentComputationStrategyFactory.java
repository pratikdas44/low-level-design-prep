package PaymentInstructions;

public class PaymentComputationStrategyFactory {
    public PaymentComputationStrategy createComputationStrategy(String strategyType){
        switch (strategyType){
            case "common":
                return new CommonPaymentComputationStrategy();

            default:
                throw new IllegalArgumentException("INVALID strategy types" + strategyType);
        }
    }
}
