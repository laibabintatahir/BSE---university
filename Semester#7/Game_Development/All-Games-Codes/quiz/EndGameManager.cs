using System.Collections;
using System.Collections.Generic;
using TMPro;
using UnityEngine;
using UnityEngine.SceneManagement;

public class EndGameManager : MonoBehaviour
{
    [SerializeField]
    TextMeshProUGUI endMessage;
    // Start is called before the first frame update
    void Start()
    {
        if(ScoreKeeper.Instance != null)
        {
            if(ScoreKeeper.Instance.CalculateScore() >= 60)
            {
                endMessage.text = "You Passed!, Score is: " + ScoreKeeper.Instance.CalculateScore() + "%";
            }
            else
            {
                endMessage.text = "You Failed!, Score is: " + ScoreKeeper.Instance.CalculateScore() + "%";
            }
        }
    }

    public void OnClickPlayAgain()
    {
        SceneManager.LoadScene(0);
    }
}
