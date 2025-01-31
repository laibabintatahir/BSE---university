public class SmartHome {
    public static void main(String[] args){
        CentralController controller = CentralController.getInstance();


        SmartDevice light = DeviceFactory.createDevice("SmartLight", "Dinninng Room Light", "BrandX");
        SmartDevice thermostat = DeviceFactory.createDevice("SmartThermostat", "Thermostat 1", "BrandY");
        SecurityCamera camera = (SecurityCamera) DeviceFactory.createDevice("SecurityCamera", "Main Door Camera", "BrandX");


        controller.addDevice(light);
        controller.addDevice(thermostat);
        controller.addDevice(camera);


        controller.controlDevice("Dinnig Room Light", "turn_on");
        controller.controlDevice("Thermostat 1", "set_temperature", 22);

        SecurityCameraProxy cameraProxy = new SecurityCameraProxy(camera);
        cameraProxy.performAction("record", "Dua ");
        cameraProxy.performAction("record", "Fatima");


        NotificationSystem notificationSystem = new NotificationSystem();
        User user1 = new User("Fatima");
        User user2 = new User("Dua");

        notificationSystem.subscribe(user1);
        notificationSystem.subscribe(user2);

        notificationSystem.notify("Motion detected at main door.");
    }
}
