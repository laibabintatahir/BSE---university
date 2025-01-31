public class SecurityCameraProxy {
    private SecurityCamera camera;

    public SecurityCameraProxy(SecurityCamera camera) {
        this.camera = camera;
    }

    public void performAction(String action, String userRole, Object... args) {
        if (!userRole.equals("Fatima") && action.equals("record")) {
            System.out.println("Access denied for recording.");
        } else {
            camera.performAction(action, args);
        }
    }}
