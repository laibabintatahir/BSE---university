using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ScoreKeeper : MonoBehaviour
{
    int correctAnswers = 0;
    int questionsSeen = 0;

    public static ScoreKeeper Instance;

    public int CorrectAnswers
    {
        get { return correctAnswers; }
        set { correctAnswers = value; }
    }

    public int QuestionsSeen
    {
        get { return questionsSeen; }
        set { questionsSeen = value; }
    }

    public int CalculateScore()
    {
        return Mathf.RoundToInt(correctAnswers/(float)questionsSeen * 100);
    }

    void Awake()
    {
        Instance = this;
        DontDestroyOnLoad(gameObject);
    }

}
