package Builder;

public class Person {
    private String name;
    private String university;
    private int age;

    public Person(PersonBuilder builder){
        this.name = builder.name;
        this.university = builder.university;
        this.age = builder.age;
    }

    public static class PersonBuilder{
        private String name;
        private String university;
        private int age;

        public PersonBuilder(String name, String university, int age){
            this.name = name;
            this.university = university;
            this.age = age;
        }

        public Person build(){
            return new Person(this);
        }
    }

    @Override
    public String toString(){
        return (this.name + " " + this.university + " " + this.age);
    }
}
