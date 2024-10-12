package PredictiveDataScaling.HistoricalData;

import PredictiveDataScaling.MetricsData;

import java.util.List;

public interface HistoricalData {
    List<MetricsData> fetchHistoricalData();
}
