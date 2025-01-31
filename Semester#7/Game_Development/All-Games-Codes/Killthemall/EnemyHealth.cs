using System.Diagnostics.Contracts;
using UnityEngine;
using UnityEngine.UI;

public class EnemyHealth : MonoBehaviour
{
    [SerializeField]
    int maxHealth = 3;
    int currentHealth = 0;
    [SerializeField]
    Image healthBar;

    public int CurrentHealth
    { get { return currentHealth; } set { currentHealth = value; } }

    private void Awake()
    {
        currentHealth = maxHealth;
    }

    public void ReduceHealth(int amount)
    {
        currentHealth -= amount;
        healthBar.fillAmount = (float)currentHealth/maxHealth;
        Debug.Log("Hit");
    }

    private void Update()
    {
        Canvas hC = healthBar.transform.parent.GetComponent<Canvas>();
        Vector3 direction = hC.transform.position - Camera.main.transform.position;
        hC.transform.rotation = Quaternion.LookRotation(direction);
    }
}
