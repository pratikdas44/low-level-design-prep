package Search;

import Products.Product;

import java.util.List;

public class SearchManager {
    private SearchStrategy searchStrategy;
    public SearchManager(SearchStrategy searchStrategy){
        this.searchStrategy = searchStrategy;
    }

    public List<Product> performSearch(List<Product> products, String query){
        return this.searchStrategy.searchStrategy(products, query);
    }
}
