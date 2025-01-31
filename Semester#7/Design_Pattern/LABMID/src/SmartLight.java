class SmartLight extends SmartDevice {
    public SmartLight(String name, String brand) {
        super(name, brand);
    }

    @Override
    public void performAction(String action, Object... args) {
        if (action.equals("turn_on")) {
            System.out.println(getName() + " is now ON.");
        } else if (action.equals("turn_off")) {
            System.out.println(getName() + " is now OFF.");
        } else {
            System.out.println("Action " + action + " not supported for " + getName() + ".");
        }
    }
}
