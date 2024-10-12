package PredictiveDataScaling.MLModels;

import PredictiveDataScaling.MetricsData;
import java.util.List;
public interface MLStrategy {
    public void execute(List<MetricsData> metricsDataList);
}
