using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerMovement : MonoBehaviour
{
    [SerializeField]
    float moveSpeed = 0.25f;

    // Start is called before the first frame update
    void Start()
    {
        Debug.Log("In Start");
    }

    // Update is called once per frame
    void Update()
    {
        Move();
    }

    void Move()
    {
        float vertA = Input.GetAxis("Vertical");
        float horiA = Input.GetAxis("Horizontal");

        float frameIndMoveSpeed = moveSpeed * Time.deltaTime;

        transform.Translate(frameIndMoveSpeed*horiA, 0, frameIndMoveSpeed*vertA);
    }
}
