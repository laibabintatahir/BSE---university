using UnityEngine;
using UnityEngine.InputSystem;

public class VehicleController : MonoBehaviour
{
    [SerializeField]
    WheelCollider frontLeftWC;
    [SerializeField]
    WheelCollider frontRightWC;
    [SerializeField]
    WheelCollider backLeftWC;
    [SerializeField]
    WheelCollider backRightWC;

    [SerializeField]
    Transform frontLeftW;
    [SerializeField] 
    Transform frontRightW;
    [SerializeField] 
    Transform backLeftW;
    [SerializeField] 
    Transform backRightW;

    [SerializeField]
    InputAction accelerationAction;
    [SerializeField]
    InputAction brakeAction;
    [SerializeField]
    InputAction steerAction;

    [SerializeField]
    float maxAcceleration = 500f;
    [SerializeField]
    float maxBrakeForce = 300f;
    [SerializeField]
    float maxSteerAngle = 25f;

    float currentAcceleration;
    float currentBrakeForce;
    float currentSteerAngle;

    private void OnEnable()
    {
        accelerationAction.Enable();
        brakeAction.Enable();
        steerAction.Enable();
    }
    private void FixedUpdate()
    {
        VehicleMovement();
    }

    private void VehicleMovement()
    {
        //Acceleration
        currentAcceleration = accelerationAction.ReadValue<float>() * maxAcceleration;
        backLeftWC.motorTorque = currentAcceleration;
        backRightWC.motorTorque = currentBrakeForce;

        //Braking
        currentBrakeForce = brakeAction.ReadValue<float>() * maxBrakeForce;
        frontLeftWC.brakeTorque = currentBrakeForce;
        frontRightWC.brakeTorque = currentBrakeForce;
        backLeftWC.brakeTorque = currentBrakeForce;
        backRightWC.brakeTorque = currentBrakeForce;

        //Steering
        currentSteerAngle = steerAction.ReadValue<float>() * maxSteerAngle;
        frontLeftWC.steerAngle = currentSteerAngle;
        frontRightWC.steerAngle = currentSteerAngle;

        UpdateWheelTransform(frontLeftWC, frontLeftW);
        UpdateWheelTransform(frontRightWC, frontRightW);
        UpdateWheelTransform(backLeftWC, backLeftW);
        UpdateWheelTransform(backRightWC, backRightW);
    }

    void UpdateWheelTransform(WheelCollider wheelCollider, Transform wheelTransform)
    {
        Vector3 pos;
        Quaternion rot;

        wheelCollider.GetWorldPose(out pos, out rot);
        wheelTransform.position = pos;
        wheelTransform.rotation = rot;
    }
}
