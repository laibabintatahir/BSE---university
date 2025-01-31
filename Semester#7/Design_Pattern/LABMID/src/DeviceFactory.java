class DeviceFactory {
    public static SmartDevice createDevice(String type, String name, String brand) {
        switch (type) {
            case "SmartLight":
                return new SmartLight(name, brand);
            case "SmartThermostat":
                return new SmartThermostat(name, brand);
            case "SecurityCamera":
                return new SecurityCamera(name, brand);
            default:
                throw new IllegalArgumentException("Unknown device type");
        }
    }
}
