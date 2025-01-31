using UnityEngine;
using UnityEngine.InputSystem;

public class Movemnet : MonoBehaviour
{
    [SerializeField]
    InputAction thrust;
    [SerializeField]
    float thrustSpeed = 100f;

    [SerializeField]
    InputAction rotation;
    [SerializeField]
    float rotationSpeed = 100f;

    Rigidbody rb;
    AudioSource thrustAS;
    [SerializeField] ParticleSystem thrustParticles;

    private void Start()
    {
        rb = GetComponent<Rigidbody>();
        thrustAS = GetComponent<AudioSource>();
    }

    private void OnEnable()
    {
        thrust.Enable();
        rotation.Enable();
    }

    private void FixedUpdate()
    {
        ApplyThrust();
        ApplyRotation();
    }

    private void ApplyRotation()
    {
        float keyValue = rotation.ReadValue<float>();
        transform.Rotate(Vector3.forward * -keyValue * rotationSpeed * Time.fixedDeltaTime);
    }

    private void ApplyThrust()
    {
        if (thrust.IsPressed())
        {
            rb.AddRelativeForce(Vector3.up * thrustSpeed * Time.fixedDeltaTime);
            if(!thrustAS.isPlaying)
            {
                thrustAS.Play();
                thrustParticles.Play();
            }
        }
        else
        {
            thrustAS.Stop();
            thrustParticles.Stop();
        }
    }
}
