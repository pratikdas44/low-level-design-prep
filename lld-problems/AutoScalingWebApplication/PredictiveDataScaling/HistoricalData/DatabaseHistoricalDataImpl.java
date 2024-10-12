package PredictiveDataScaling.HistoricalData;

import PredictiveDataScaling.MetricsData;

import java.util.ArrayList;
import java.util.List;

public class DatabaseHistoricalDataImpl implements HistoricalData{
    @Override
    public List<MetricsData> fetchHistoricalData(){
        MetricsData metricsData = new MetricsData("ABC", 100);
        List<MetricsData> metricsDataList = new ArrayList<>();
        metricsDataList.add(metricsData);
        return metricsDataList;
    }
}
