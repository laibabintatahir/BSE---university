using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ObjectCollisionDetection : MonoBehaviour
{
    MeshRenderer meshRenderer;
    Color originalColor;
    private void Start()
    {
        meshRenderer = GetComponent<MeshRenderer>();
        originalColor = meshRenderer.material.color;
    }

    private void OnCollisionEnter(Collision collision)
    {
        if(collision.gameObject.CompareTag("Player"))
        {
            Debug.Log("Player collided");
            meshRenderer.material.color = Color.black;
        }
    }

    private void OnCollisionExit(Collision collision)
    {
        if (collision.gameObject.CompareTag("Player"))
        {
            Debug.Log("Player collision exit");
            meshRenderer.material.color = originalColor;
        }
    }

    private void OnCollisionStay(Collision collision)
    {
        if (collision.gameObject.CompareTag("Player"))
        {
            Debug.Log("Player colliding");
        }
    }
}
