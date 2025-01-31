import java.util.ArrayList;
import java.util.List;

public class NotificationSystem {
    private List<User> subscribers;

    public NotificationSystem() {
        subscribers = new ArrayList<>();
    }

    public void subscribe(User user) {
        subscribers.add(user);
    }

    public void unsubscribe(User user) {
        subscribers.remove(user);
    }

    public void notify(String message) {
        for (User subscriber : subscribers) {
            subscriber.update(message);
        }
    }
}

