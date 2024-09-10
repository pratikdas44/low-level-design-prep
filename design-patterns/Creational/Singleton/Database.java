public enum Database {
    INSTANCE;
    public void connect(){
        System.out.println("DB Connected");
    }

    public void disconnect(){
        System.out.println("DB Dis-Connected");
    }
}
