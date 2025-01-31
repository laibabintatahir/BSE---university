using System;
using UnityEngine;
using UnityEngine.AI;

public class Navigate : MonoBehaviour
{
    [SerializeField]
    NavMeshAgent agent;
    [SerializeField]
    GameObject destinationObject;
    [SerializeField]
    Animator animator;
    [SerializeField]
    float detectDist, runDist, attackDist;
    [SerializeField]
    float distance;
    Vector3 originalPos;
    [SerializeField]
    Transform rayPoint;
    bool isDetected;
    [SerializeField]
    LayerMask playerLayer;

    // Audio variables
    [SerializeField]
    AudioSource audioSource; // Reference to the AudioSource component
    [SerializeField]
    AudioClip moveSound; // Sound for moving
    [SerializeField]
    AudioClip attackSound; // Sound for attacking
    [SerializeField]
    AudioClip killSound; // Sound for being killed

    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        agent = GetComponent<NavMeshAgent>();
        originalPos = transform.position;
    }

    // Update is called once per frame
    void Update()
    {
        if (Detect())
        {
            isDetected = true;
        }

        if (isDetected && CalculateDistance(transform.position, destinationObject.transform.position) < detectDist)
        {
            agent.SetDestination(destinationObject.transform.position);
            animator.SetBool("isWalking", true);

            // Play movement sound if the enemy is walking
            if (!audioSource.isPlaying && !animator.GetBool("isRunning") && !animator.GetBool("isAttacking"))
            {
                audioSource.clip = moveSound;
                audioSource.Play();
            }

            if (CalculateDistance(transform.position, agent.destination) < runDist)
            {
                animator.SetBool("isRunning", true);
                audioSource.clip = moveSound; // Ensure the move sound is set
                if (!audioSource.isPlaying)
                {
                    audioSource.Play();
                }

                if (CalculateDistance(transform.position, agent.destination) < attackDist)
                {
                    agent.ResetPath();
                    animator.SetBool("isRunning", false);
                    animator.SetBool("isWalking", false);
                    animator.SetBool("isAttacking", true);
                    
                    // Play attack sound
                    if (!audioSource.isPlaying)
                    {
                        audioSource.clip = attackSound;
                        audioSource.Play();
                    }
                }
                else
                {
                    animator.SetBool("isAttacking", false);
                    animator.SetBool("isWalking", true);
                }
            }
            else
            {
                animator.SetBool("isRunning", false);
            }
        }
        else
        {
            isDetected = false;
            agent.ResetPath();
            agent.SetDestination(originalPos);
            if (CalculateDistance(transform.position, originalPos) < 0.25)
            {
                animator.SetBool("isWalking", false);
                agent.ResetPath();
                audioSource.Stop(); // Stop moving sound when returning to original position
            }
        }
    }

    private float CalculateDistance(Vector3 from, Vector3 to)
    {
        distance = Vector3.Distance(from, to);
        return distance;
    }

    private bool Detect()
    {
        Ray ray = new Ray(rayPoint.position, rayPoint.forward);
        Debug.DrawRay(rayPoint.position, rayPoint.forward * detectDist, Color.red);
        bool isHit = Physics.Raycast(ray, detectDist, playerLayer);
        return isHit;
    }

    // Call this method when the enemy is hit (killed)
    public void OnHit()
    {
        audioSource.clip = killSound;
        audioSource.Play();
        // Additional logic for handling the enemy being hit can be added here
    }
}