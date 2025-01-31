using UnityEngine;
using UnityEngine.SceneManagement;

public class CollisionHandler : MonoBehaviour
{
    [SerializeField]
    GameObject shipModel;
    AudioSource multipleAudioSource;
    [SerializeField]
    AudioClip[] audioClips = new AudioClip[2];
    [SerializeField] 
    ParticleSystem thrustParticles;

    int sceneIndex;
    private void Start()
    {
        multipleAudioSource = GetComponent<AudioSource>();
        sceneIndex = SceneManager.GetActiveScene().buildIndex;
    }
    private void OnCollisionEnter(Collision collision)
    {
        switch(collision.gameObject.tag)
        {
            case "Friendly":
                Debug.Log("Collided with friendly");
                break;
            case "FinishLine":
                Debug.Log("Finished");
                GetComponent<Movemnet>().enabled = false;
                Destroy(thrustParticles, 1f);
                Invoke("LoadNextLevel", 2f);
                multipleAudioSource.PlayOneShot(audioClips[0]);
                break;
            default:
                Debug.Log("You Die");
                GetComponent<Movemnet>().enabled = false;
                Destroy(shipModel, 1f);
                Destroy(thrustParticles, 1f);
                Invoke("LoadCurrentLevel", 2f);
                multipleAudioSource.PlayOneShot(audioClips[1]);
                break;
        }
    }

    private void LoadNextLevel()
    {
        sceneIndex++;
        if (sceneIndex >= SceneManager.sceneCountInBuildSettings)
        {
            sceneIndex = 0;
        }
        SceneManager.LoadScene(sceneIndex);
    }

    private void LoadCurrentLevel()
    {
        int sceneIndex = SceneManager.GetActiveScene().buildIndex;
        SceneManager.LoadScene(sceneIndex);
    }
}
