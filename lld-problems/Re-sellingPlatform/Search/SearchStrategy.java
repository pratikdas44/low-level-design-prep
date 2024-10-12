package Search;

import Products.Product;

import java.util.List;

public interface SearchStrategy {
    List<Product> searchStrategy(List<Product> products, String keyword);
}
