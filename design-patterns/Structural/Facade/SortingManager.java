public class SortingManager {
    private Sorter bubbleSort;
    private Sorter mergeSort;

    public SortingManager(){
        this.bubbleSort = new BubbleSort();
        this.mergeSort = new MergeSort();
    }

    public void dobubbleSort(){
        this.bubbleSort.sort();
    }

    public void domergeSort(){
        this.mergeSort.sort();
    }
}
