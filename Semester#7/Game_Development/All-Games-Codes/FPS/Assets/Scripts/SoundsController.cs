using UnityEngine;

public class PlayerSoundController : MonoBehaviour
{
    public AudioSource footstepAudioSource;
    public AudioClip jumpSound;
    public AudioClip[] footstepSounds; // Array to hold footstep sounds if varying by surface or speed

    private CharacterController characterController;

    private void Start()
    {
        characterController = GetComponent<CharacterController>();
    }

    private void Update()
    {
        HandleFootsteps();
    }

    void HandleFootsteps()
    {
        if (characterController.isGrounded && characterController.velocity.magnitude > 0.1f && !footstepAudioSource.isPlaying)
        {
            footstepAudioSource.clip = footstepSounds[Random.Range(0, footstepSounds.Length)];
            footstepAudioSource.Play();
        }
    }

    public void Jump()
    {
        if (characterController.isGrounded)
        {
            // Code to make the player jump
            footstepAudioSource.PlayOneShot(jumpSound);
        }
    }
}
