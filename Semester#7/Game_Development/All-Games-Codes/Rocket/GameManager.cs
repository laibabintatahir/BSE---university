using UnityEngine;
using UnityEngine.InputSystem;

public class GameManager : MonoBehaviour
{
    [SerializeField]
    InputAction quitAction;

    private void OnEnable()
    {
        quitAction.Enable();
    }

    private void Update()
    {
        if(quitAction.IsPressed())
        {

            Debug.Log("Game Quit");
            Application.Quit();
        }
    }
}
