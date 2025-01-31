using System.Collections.Generic;
using System.Linq;
using TMPro;
using UnityEngine;

public class CarManager : MonoBehaviour
{
    [SerializeField]
    int numberOfCars = 50;
    [SerializeField]
    GameObject car;
    [SerializeField]
    List<GameObject> cars;
    //time for simulation
    [SerializeField]
    int generationTime = 20;
    float startTime = 0;
    [SerializeField]
    int generationNumber = 1;
    [SerializeField]
    TextMeshProUGUI text;

    private void Start()
    {
        for (int i = 0; i < numberOfCars; i++)
        {
            GameObject carChromosome = Instantiate(car, transform.position, transform.rotation);
            AIController aiController = carChromosome.GetComponent<AIController>();
            aiController.SteeringSenstivity = Random.Range(0.01f, 0.03f);
            aiController.LookAhead = Random.Range(18f, 22f);
            aiController.MaxTorque = Random.Range(180f, 220f);
            aiController.MaxSteerAngle = Random.Range(50f, 70f);
            aiController.MaxBrakeTorque = Random.Range(4500f, 5500f);
            aiController.AccelCornerMax = Random.Range(18f, 22f);
            aiController.BrakeCornerMax = Random.Range(3f, 7f);
            aiController.AccelVelocityThreshold = Random.Range(18f, 22f);
            aiController.BrakeVelocityThreshold = Random.Range(8f, 12f);
            aiController.AntiRoll = Random.Range(4500f, 5500f);
            cars.Add(carChromosome);
        }
        //Simulation time
        Time.timeScale = 5;
        text.text = "Trial " + generationNumber;
    }

    float RandomWeight() => Random.Range(0f, 1f);

    GameObject GeneSwap(AIController parentOne, AIController parentTwo)
    {
        GameObject carChromosome = Instantiate(car, transform.position, transform.rotation);
        AIController aiController = carChromosome.GetComponent<AIController>();

        float weight = RandomWeight();

        aiController.SteeringSenstivity = Blend(parentOne.SteeringSenstivity, parentTwo.SteeringSenstivity, weight);
        aiController.LookAhead = Blend(parentOne.LookAhead, parentTwo.LookAhead, weight);
        aiController.MaxTorque = Blend(parentOne.MaxTorque, parentTwo.MaxTorque, weight);
        aiController.MaxSteerAngle = Blend(parentOne.MaxSteerAngle, parentTwo.MaxSteerAngle, weight);
        aiController.MaxBrakeTorque = Blend(parentOne.MaxBrakeTorque, parentTwo.MaxBrakeTorque, weight);
        aiController.AccelCornerMax = Blend(parentOne.AccelCornerMax, parentTwo.AccelCornerMax, weight);
        aiController.BrakeCornerMax = Blend(parentOne.BrakeCornerMax, parentTwo.BrakeCornerMax, weight);
        aiController.AccelVelocityThreshold = Blend(parentOne.AccelVelocityThreshold, parentTwo.AccelVelocityThreshold, weight);
        aiController.BrakeVelocityThreshold = Blend(parentOne.BrakeVelocityThreshold, parentTwo.BrakeVelocityThreshold, weight);
        aiController.AntiRoll = Blend(parentOne.AntiRoll, parentTwo.AntiRoll, weight);

        return carChromosome;
    }

    float Blend(float value1, float value2, float weight)
    {
        return value1 * weight + value2 * (1 - weight);
    }

    void Breed()
    {
        startTime = Time.realtimeSinceStartup;
        List<GameObject> sortedCars = cars.OrderByDescending(x => x.GetComponent<AIController>().Fitness).ToList();
        int halfCars = sortedCars.Count / 2;
        cars.Clear();
        for (int i = 0; i < halfCars; i++)
        {
            cars.Add(GeneSwap(sortedCars[i].GetComponent<AIController>(), sortedCars[i + 1].GetComponent<AIController>()));
            cars.Add(GeneSwap(sortedCars[i + 1].GetComponent<AIController>(), sortedCars[i].GetComponent<AIController>()));
        }

        for (int i = 0; i < sortedCars.Count; i++)
        {
            Destroy(sortedCars[i]);
        }

        generationNumber++;
        text.text = "Trial " + generationNumber;
    }

    private void Update()
    {
        if(Time.realtimeSinceStartup > startTime + generationTime)
        {
            Breed();
        }
    }

}



   /*GameObject GeneSwap(AIController parentOne, AIController parentTwo)
    {
        GameObject carChromosome = Instantiate(car, transform.position, transform.rotation);
        AIController aiController = carChromosome.GetComponent<AIController>();
        float mutationFactor = Random.Range(-0.1f, 0.1f);
        aiController.SteeringSenstivity = (parentOne.SteeringSenstivity + parentTwo.SteeringSenstivity) / 2f;
        aiController.LookAhead = (parentOne.LookAhead + parentTwo.LookAhead) / 2f;
        aiController.MaxTorque = (parentOne.MaxTorque + parentTwo.MaxTorque) / 2f;
        aiController.MaxSteerAngle = (parentOne.MaxSteerAngle + parentTwo.MaxSteerAngle) / 2f;
        aiController.MaxBrakeTorque = (parentOne.MaxBrakeTorque + parentTwo.MaxBrakeTorque) / 2f;
        aiController.AccelCornerMax = (parentOne.AccelCornerMax + parentTwo.AccelCornerMax) / 2f;
        aiController.BrakeCornerMax = (parentOne.BrakeCornerMax + parentTwo.BrakeCornerMax) / 2f;
        aiController.AccelVelocityThreshold = (parentOne.AccelVelocityThreshold = parentTwo.AccelVelocityThreshold) / 2f;
        aiController.BrakeVelocityThreshold = (parentOne.BrakeVelocityThreshold + parentTwo.BrakeVelocityThreshold) / 2f;
        aiController.AntiRoll = (parentOne.AntiRoll + parentTwo.AntiRoll) / 2f;

        return carChromosome;
    }*/