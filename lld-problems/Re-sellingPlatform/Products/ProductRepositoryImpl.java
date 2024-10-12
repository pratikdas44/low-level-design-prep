package Products;

import java.util.List;

public class ProductRepositoryImpl implements ProductsRepository{
    @Override
    public Product findbyId(long id){
        return new Product(id, " Product " + id, "Category", 100.0);
    }

    @Override
    public List<Product> findByCategory(String category){
        return List.of(new Product(1, "proudct 1", category, 100.0));
    }

    @Override
    public void addProduct(Product product){

    }

    @Override
    public void updateProduct(Product product){

    }

    @Override
    public void deleteProduct(long id){

    }
}
