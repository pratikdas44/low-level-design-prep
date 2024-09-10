package Builder;

public class Main {
    public static void main(String[] args) {
        Person person = new Person.PersonBuilder("ABC", "XYZ", 23).build();
        System.out.println(person);
    }
}
