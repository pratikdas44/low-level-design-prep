package PredictiveDataScaling.MLModels;

import PredictiveDataScaling.MetricsData;

import java.util.List;

public class StrategyContext {
    private MLStrategy mlStrategy;
    public void setMlStrategy(MLStrategy mlStrategy){
        this.mlStrategy = mlStrategy;
    }

    public void execute(List<MetricsData> metricsDataList){
        this.mlStrategy.execute(metricsDataList);
    }
}
