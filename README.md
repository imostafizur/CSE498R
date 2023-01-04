## CSE498R
### Predicting deasease using diagnosis data.
### Parkinson's Disease
Parkinson's disease is a progressive disorder of the central nervous system that affects movement. Symptoms start gradually, sometimes starting with a barely noticeable tremor in just one hand. Tremors are common, but the disorder also commonly causes stiffness or slowing of movement.

Algorithm used and its accuracy table is given below.

| Algorithm | Accuracy |
|-----------|----------|
| QDA |0.95 |
| KNN | 0.70|
| SVM | 0.95 |
| Decision tree| 0.80 |
|LDA|0.80|
|Naive Bayes algorithm|0.80|
|K-means|0.45|
|Random forest algorithm|0.95|
|AdaBoost|0.85|
|LSTM|0.70|
|XGBoost|0.85|
|Gradient Boosting|0.85|

Best model is QDA and Random forest algorithm. Those model other parameters :

#### SVM

| Metric      | Score       |
|-------------|-------------|
| RMSE        | 0.2236068   |
| MAE         | 0.05        |
| Recall      | 0.8888889   |
| Precision   | 1.0         |
| F1          | 0.9411765   |
| R2          | 0.7979798   |
| k-fold Accuracy | 0.72 (+/- 0.38) |

#### QDA

| Metric      | Score       |
|-------------|-------------|
| RMSE        | 0.2236068   |
| MAE         | 0.05        |
| Recall      | 1.0         |
| Precision   | 0.9         |
| F1          | 0.9473684   |
| R2          | 0.7979798   |
| k-fold Accuracy | 0.80 (+/- 0.41) |

So the model is QDA.

### Diabetes
Diabetes is a disease that occurs when your blood glucose, also called blood sugar, is too high. Blood glucose is your main source of energy and comes from the food you eat. Insulin, a hormone made by the pancreas, helps glucose from food get into your cells to be used for energy. Sometimes your body doesn’t make enough—or any—insulin or doesn’t use insulin well. Glucose then stays in your blood and doesn’t reach your cells.

Algorithm used and its accuracy table is given below.

| Algorithm | Accuracy |
|-----------|----------|
| Decision Tree | 0.79 |
| KNN | 0.74 |
| SVM | 0.83 |
| QDA | 0.77 |
|LDA|0.825|
|Naive Bayes algorithm|0.80|
| Decision tree|0.88|
|Random forest algorithm|0.93|
|AdaBoost|0.83|
|k-means clustering|0.58|
|XGBoost|0.90|
|Gradient Boosting|0.88|


### Heart Disease
Heart disease is a general term that describes several types of heart conditions. The most common type of heart disease is coronary artery disease, which occurs when the blood vessels that supply blood to the heart become narrowed or blocked by a buildup of plaque. This buildup of plaque is called atherosclerosis. Atherosclerosis can occur in any blood vessel, but it most commonly affects the arteries that supply blood to the heart, brain, and legs.

Algorithm used and its accuracy table is given below.

| Algorithm | Accuracy |
|-----------|----------|
| Decision Tree | 0.79 |
| KNN | 0.74 |
| SVM | 0.83 |
| QDA | 0.84 |
|LDA|0.84|
|Naive Bayes algorithm|0.81|
|LSTM |0.81|
|Random forest algorithm|0.82|
|AdaBoost|0.79|
|k-means clustering|0.80|
|XGBoost|0.80|
|Gradient Boosting|0.80|
### LUNG Cancer
Lung cancer is a type of cancer that starts in the lungs. The lungs are two spongy organs in the chest that take in oxygen when you breathe and release carbon dioxide when you exhale. Lung cancer can start in different parts of the lungs. The most common type of lung cancer is non-small cell lung cancer (NSCLC). NSCLC is divided into two main types: squamous cell carcinoma and adenocarcinoma. The other main type of lung cancer is small cell lung cancer (SCLC).

| Algorithm | Accuracy |
|-----------|----------|
| QDA |0.91 |
| KNN | 0.95|
| SVM | 0.96 |
| Decision tree| 0.95 |
|LDA|0.96|
|Naive Bayes algorithm|0.95|
|K-means|0.46|
|Random forest algorithm|0.96|
|AdaBoost|0.98|
|Neural-Network|0.95|
|XGBoost|0.98|
|Gradient Boosting|0.96|

### Brain stroke 
A stroke occurs when blood flow to an area of the brain is interrupted or reduced, depriving brain tissue of oxygen and nutrients. Brain cells begin to die within minutes. A stroke is a medical emergency, and prompt treatment is crucial. Early action can reduce brain damage and other complications.

| Algorithm | Accuracy |
|-----------|----------|
| QDA |0.55 |
| KNN | 0.97|
| SVM | 0.77 |
| Decision tree| 0.97 |
|LDA|0.77|
|Naive Bayes algorithm|0.64|
|K-means|0.62|
|Random forest algorithm|0.99|
|AdaBoost|0.82|
|LSTM|0.76|
|XGBoost|0.97|
|Gradient Boosting|0.84|

Dependencies
------------
* Python 3.10

Installation
-----------

command to install all the dependencies
```bash
pip install -r requirements.txt
```

