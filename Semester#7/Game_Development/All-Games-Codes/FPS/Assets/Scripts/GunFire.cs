using UnityEngine;
using UnityEngine.InputSystem;

public class GunFire : MonoBehaviour
{
    Camera cam;
    [SerializeField]
    InputAction fire;
    [SerializeField]
    ParticleSystem muzzleFlash; // Reference to the Muzzle Flash particle system
    [SerializeField]
    ParticleSystem bloodSplatterPrefab; // Reference to the Blood Splatter prefab
    [SerializeField]
    AudioSource gunAudioSource; // Reference to the AudioSource component
    [SerializeField]
    float muzzleFlashDuration = 0.1f; // Time to stop the muzzle flash
    bool isFired;

    private void OnEnable()
    {
        fire.Enable();
    }

    private void OnDisable()
    {
        fire.Disable();
    }

    private void Start()
    {
        cam = Camera.main;
    }

    private void Update()
    {
        if (fire.WasPressedThisFrame()) // Fire only when the button is pressed this frame
        {
            isFired = true;
        }
    }

    private void FixedUpdate()
    {
        Vector2 screenPos = new Vector2(Screen.width / 2, Screen.height / 2);
        Ray ray = cam.ScreenPointToRay(screenPos);
        RaycastHit hit;
        bool isHit = Physics.Raycast(ray, out hit, Mathf.Infinity);

        if (isHit)
        {
            if (isFired)
            {
                // Trigger muzzle flash and gun sound
                PlayMuzzleFlash();
                PlayGunSound();

                // Show blood splatter at the hit location if enemy is hit
                if (hit.collider.gameObject.CompareTag("Enemy"))
                {
                    SpawnBloodSplatter(hit.point, hit.normal);
                    Rigidbody rb = hit.rigidbody;
                    if (rb != null)
                    {
                        rb.gameObject.GetComponentInParent<Animator>().enabled = false;
                        rb.AddForceAtPosition(-rb.transform.forward * 400f, hit.point, ForceMode.Impulse);
                    }
                }

                isFired = false;
            }
        }
    }

    private void PlayMuzzleFlash()
    {
        if (muzzleFlash != null)
        {
            muzzleFlash.Play(); // Play the muzzle flash particle effect
            StartCoroutine(StopMuzzleFlashAfterDelay());
        }
        else
        {
            Debug.LogWarning("Muzzle Flash particle system is not assigned!");
        }
    }

    private void PlayGunSound()
    {
        if (gunAudioSource != null)
        {
            gunAudioSource.Play(); // Play the gun sound
        }
        else
        {
            Debug.LogWarning("Gun AudioSource is not assigned!");
        }
    }

    private void SpawnBloodSplatter(Vector3 position, Vector3 normal)
    {
        if (bloodSplatterPrefab != null)
        {
            // Instantiate the blood splatter effect at the hit location
            ParticleSystem bloodSplatter = Instantiate(bloodSplatterPrefab, position, Quaternion.LookRotation(normal));
            bloodSplatter.Play();

            // Destroy the blood splatter effect after it finishes
            Destroy(bloodSplatter.gameObject, bloodSplatter.main.duration + bloodSplatter.main.startLifetime.constantMax);
        }
        else
        {
            Debug.LogWarning("Blood Splatter prefab is not assigned!");
        }
    }

    private System.Collections.IEnumerator StopMuzzleFlashAfterDelay()
    {
        yield return new WaitForSeconds(muzzleFlashDuration); // Wait for the specified duration
        if (muzzleFlash != null)
        {
            muzzleFlash.Stop(); // Stop the muzzle flash particle effect
        }
    }
}
