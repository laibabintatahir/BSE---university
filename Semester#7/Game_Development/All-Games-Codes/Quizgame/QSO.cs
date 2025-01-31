using UnityEngine;

[CreateAssetMenu(fileName = "Question", menuName = "Add Question SO")]
public class QSO : ScriptableObject
{
    [TextArea(1, 5)]
    [SerializeField]
    string questionText;
    [SerializeField]
    string[] options = new string[4];
    [SerializeField]
    int correctOption;

    public string QuestionText
    {
        get { return questionText; } set { questionText = value; }
    }

    public int CorrectOption
    { 
        get { return correctOption; } set { correctOption = value; } 
    }

    public string[] Options
    {
        get { return options; }
        set { options = value; }
    }

    public string GetAnswerText(int index)
    {
        return options[index];
    }
}
