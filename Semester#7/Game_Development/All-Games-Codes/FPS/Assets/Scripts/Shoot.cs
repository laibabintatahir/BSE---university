using System.Linq;
using UnityEngine;
using UnityEngine.InputSystem;

public class Shoot : MonoBehaviour
{
    [SerializeField]
    InputAction shootAction;
    [SerializeField]
    Transform shootPoint;
    bool isFired;

    private void OnEnable()
    {
        shootAction.Enable();
    }

    private void Update()
    {
        if (shootAction.IsPressed())
        {
            isFired = true;
        }
    }
    private void FixedUpdate()
    {
        ShootAction();
    }

    private void ShootAction()
    {
        
        RaycastHit hit;
        Vector2 screenPoint = new Vector2(Screen.width / 2, Screen.height / 2);
        Ray ray = Camera.main.ScreenPointToRay(screenPoint);
        
        Debug.DrawRay(ray.origin, ray.direction * 1000f, Color.yellow);
        bool isHit = Physics.Raycast(ray, out hit, Mathf.Infinity);
        if(isHit)
        {
            if (isFired)
            {
                if(hit.rigidbody)
                {
       
                    GameObject hitGO = hit.rigidbody.gameObject;
                    Debug.Log("Info: " + hit.collider.gameObject.name);
                    Animator enemyAnimator = hitGO.GetComponentInParent<Animator>();
                    enemyAnimator.enabled = false;
                    Rigidbody[] rbs = hitGO.GetComponents<Rigidbody>();
                    Rigidbody hitRB = rbs.OrderBy(rigidbody => Vector3.Distance(rigidbody.position, hit.point)).First();
                    hitRB.AddForceAtPosition(-hitRB.gameObject.transform.forward * 100, hit.point, ForceMode.Impulse);
                    
                }
                isFired = false;
            }
        }
        
    }

}
