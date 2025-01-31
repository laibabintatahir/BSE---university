class SmartThermostat extends SmartDevice {
    public SmartThermostat(String name, String brand) {
        super(name, brand);
    }

    @Override
    public void performAction(String action, Object... args) {
        if (action.equals("set_temperature")) {
            int temperature = (int) args[0];
            System.out.println(getName() + " temperature set to " + temperature + " degrees.");
        } else {
            System.out.println("Action " + action + " not supported for " + getName() + ".");
        }
    }
}
