class SecurityCamera extends SmartDevice {
    public SecurityCamera(String name, String brand) {
        super(name, brand);
    }

    @Override
    public void performAction(String action, Object... args) {
        if (action.equals("record")) {
            System.out.println(getName() + " is now recording.");
        } else {
            System.out.println("Action " + action + " not supported for " + getName() + ".");
        }
    }
}
