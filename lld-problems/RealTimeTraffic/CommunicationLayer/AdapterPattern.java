package CommunicationLayer;

public class AdapterPattern {
    public static void main(String[] args) {
        ExternalDataConverter converter = new ExternalDataConverter("Internal data");
        System.out.println(converter.convertToExternalFormat());
    }
}
