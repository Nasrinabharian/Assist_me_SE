# a regression model for COVID-19 prediction  
## steps:  
1. preprocessing  
2. balancing the training data  
3. training and testing logestic regression model  
4. fine-tuning the result with input filtering  
5. defining a function which predicts COVID based on symptoms  
  
base model evaluation on test dataset:  
              precision,    recall,  f1-score,   support  
           0:       0.11,      0.23,      0.15,       800  
           1:       0.87,      0.74,      0.80,      5536  
    accuracy:                           0.68,      6336  
   macro avg:       0.49,      0.49,      0.48,      6336  
weighted avg:       0.77,      0.68,      0.72,      6336  
(data related to Iran is used.)

