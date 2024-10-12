package CostOptimization.CostAnalysis;

public class CostCalculatorAdapter implements CostCalculatorInterface{
    private ThirdPartyCostCalculator thirdPartyCostCalculator;
    public CostCalculatorAdapter(ThirdPartyCostCalculator thirdPartyCostCalculator){
        this.thirdPartyCostCalculator = thirdPartyCostCalculator;
    }

    @Override
    public void calculate(){
        this.thirdPartyCostCalculator.calculate();
    }
}
