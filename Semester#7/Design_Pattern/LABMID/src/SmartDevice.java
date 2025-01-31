abstract class SmartDevice {
    private String name;
    private String brand;

    public SmartDevice(String name, String brand) {
        this.name = name;
        this.brand = brand;
    }

    public String getName() {
        return name;
    }

    public String getBrand() {
        return brand;
    }

    public abstract void performAction(String action, Object... args);
}

