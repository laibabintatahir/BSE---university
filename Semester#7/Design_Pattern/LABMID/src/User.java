public class User {
    private String name;

    public User(String name) {
        this.name = name;
    }

    public void update(String message) {
        System.out.println("Notification for " + name + ": " + message);
    }
}

