package DynamicScaling.PolicyBuilder;

public class PolicyBuilder {
    private int threshold;
    private int cooldownPeriod;

    public PolicyBuilder(PolicyBuilderImpl policyBuilder){
        this.threshold = policyBuilder.threshold;
        this.cooldownPeriod = policyBuilder.cooldownPeriod;
    }

    public static class PolicyBuilderImpl{
        private int threshold;
        private int cooldownPeriod;

        public PolicyBuilderImpl(int threshold, int cooldownPeriod){
            this.cooldownPeriod = cooldownPeriod;
            this.threshold = threshold;
        }

        public PolicyBuilder build(){
            return new PolicyBuilder(this);
        }
    }
}
