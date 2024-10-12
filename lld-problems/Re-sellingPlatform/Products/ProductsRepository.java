package Products;
import java.util.List;
public interface ProductsRepository {
    Product findbyId(long id);
    List<Product> findByCategory(String category);
    void addProduct(Product product);
    void updateProduct(Product product);
    void deleteProduct(long id);
}
