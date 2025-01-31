using UnityEngine;
using TMPro;
using UnityEngine.UI;
using System.Collections.Generic;
using UnityEngine.SceneManagement;

public class QuizManager : MonoBehaviour
{
    [Header("Question Info")]
    [SerializeField]
    List<QSO> questions = new List<QSO>();
    QSO currentQuestion;
    [SerializeField]
    TextMeshProUGUI questionText;

    [Header("Option Buttons Info")]
    [SerializeField]
    Button[] optionButtons = new Button[4];
    [SerializeField]
    Sprite defaultSprite, correctSprite;

    [Header("Timer Info")]
    [SerializeField]
    float timeToDisplayQuestion = 10f;
    [SerializeField]
    float timeToDisplayCorrectOption = 5f;
    [SerializeField]
    Image timerImage;
    float timerValue = 0f;
    bool isAnsweringQuestion;
    bool nextQuestionDisplay;
    bool hasAnswered;

    [Header("Scoring Info")]
    [SerializeField]
    TextMeshProUGUI scoreText;
    ScoreKeeper scoreKeeper;

    [Header("Slider Info")]
    [SerializeField]
    Slider questionSlider;
    bool isComplete;
    
    void Start()
    {
        //DisplayNextQuestion();
        scoreKeeper = FindObjectOfType<ScoreKeeper>();
        scoreText.text = "0%";
        questionSlider.maxValue = questions.Count;
        questionSlider.value = 0;
    }

    void Update()
    {
        UpdateTimer();
        if(nextQuestionDisplay)
        {
            DisplayNextQuestion();
            nextQuestionDisplay = false;
        }
        else if(!hasAnswered && !isAnsweringQuestion)
        {
            hasAnswered = false;
            DisplayAnswer(-1);
            SetButtonsState(false);
        }

        if(isComplete)
        {
            SceneManager.LoadScene(1);
        }
    }

    void DisplayNextQuestion()
    {
        if (questions.Count > 0)
        {
            SelectRandomQuestion();
            DisplayQuestion();
            SetButtonsState(true);
            SetDefaultSprites();
            questionSlider.value++;
            scoreKeeper.QuestionsSeen++;
        }
        else
        {
            isComplete = true;
        }
    }

    void DisplayQuestion()
    {
        questionText.text = currentQuestion.QuestionText;
        for (int i = 0; i < optionButtons.Length; i++)
        {
            TextMeshProUGUI buttonText = optionButtons[i].GetComponentInChildren<TextMeshProUGUI>();
            buttonText.text = currentQuestion.GetAnswerText(i);
        }
    }

    public void OnOptionSelected(int index)
    {
        hasAnswered = true;
        DisplayAnswer(index);
        SetButtonsState(false);
        ResetTimer();
        scoreText.text = scoreKeeper.CalculateScore()+"%";
    }

    void SelectRandomQuestion()
    {
        int index = Random.Range(0, questions.Count);
        currentQuestion = questions[index];
        if(questions.Contains(currentQuestion))
            questions.Remove(currentQuestion);
    }

    void DisplayAnswer(int index)
    {
        if (index == currentQuestion.CorrectOption)
        {
            questionText.text = "Correct!";
            Image buttonImage = optionButtons[index].GetComponent<Image>();
            buttonImage.sprite = correctSprite;
            scoreKeeper.CorrectAnswers++;
        }
        else
        {
            int correctIndex = currentQuestion.CorrectOption;
            questionText.text = "You are Wrong! The correct option is: " + currentQuestion.GetAnswerText(correctIndex);
            Image buttonImage = optionButtons[correctIndex].GetComponent<Image>();
            buttonImage.sprite = correctSprite;
        }
    }

    void SetButtonsState(bool state)
    {
        foreach (Button button in optionButtons)
        {
            button.interactable = state;
        }
    }

    void SetDefaultSprites()
    {
        foreach(Button button in optionButtons)
        {
            button.GetComponent<Image>().sprite = defaultSprite;
        }
    }

    void UpdateTimer()
    {
        timerValue -= Time.deltaTime;
        if(isAnsweringQuestion)
        {
            timerImage.fillAmount = timerValue / timeToDisplayQuestion;
            if (timerValue <= 0)
            {
                timerValue = timeToDisplayCorrectOption;
                isAnsweringQuestion = false;
            }
        }
        else
        {
            timerImage.fillAmount = timerValue / timeToDisplayCorrectOption;
            if (timerValue <= 0)
            {
                timerValue = timeToDisplayQuestion;
                isAnsweringQuestion = true;
                nextQuestionDisplay = true;
            }
        }
    }

    void ResetTimer()
    {
        timerValue = 0;
    }
}
