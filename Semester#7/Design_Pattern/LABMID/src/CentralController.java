import java.util.ArrayList;

public class CentralController {
    private static CentralController instance;
    private ArrayList<SmartDevice> devices;

    private CentralController() {
        devices = new ArrayList<SmartDevice>();
    }

    public static synchronized CentralController getInstance() {
        if (instance == null) {
            instance = new CentralController();
        }
        return instance;
    }

    public void addDevice(SmartDevice device) {
        devices.add(device);
    }

    public void removeDevice(SmartDevice device) {
        devices.remove(device);
    }

    public void controlDevice(String deviceName, String action, Object... args) {
        for (SmartDevice device : devices) {
            if (device.getName().equals(deviceName)) {
                device.performAction(action, args);
                return;
            }
        }
        System.out.println("Device " + deviceName + " not found.");
    }
}
