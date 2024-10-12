package Search;

import Products.Product;

import java.util.List;

public class CategorySearch implements SearchStrategy{
    @Override
    public List<Product> searchStrategy(List<Product> products, String keyword){
        return products.stream().filter(product -> product.getCategory().equalsIgnoreCase(keyword)).toList();
    }
}