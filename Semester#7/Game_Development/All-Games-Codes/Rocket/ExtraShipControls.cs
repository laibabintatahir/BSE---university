using UnityEngine;
using UnityEngine.InputSystem;

public class ExtraShipControls : MonoBehaviour
{
    [SerializeField]
    InputAction lights;
    [SerializeField]
    GameObject lightsGO;
    bool areLightsOn = false;

    private void OnEnable()
    {
        lights.Enable();
    }

    private void Update()
    {
        ToggleLights();
    }

    private void ToggleLights()
    {
        if (lights.IsPressed())
        {
            //turn lights on/off
            if (areLightsOn)
            {
                lightsGO.SetActive(false);
                areLightsOn = false;
            }
            else
            {
                lightsGO.SetActive(true);
                areLightsOn = true;
            }

        }
    }
}
