## Multiple Disease Prediction using Machine Learning and Deep Learning with the Implementation of Web Technology
### Predicting deasease using diagnosis data.
### Parkinson's Disease
Parkinson's disease is a progressive disorder of the central nervous system that affects movement. Symptoms start gradually, sometimes starting with a barely noticeable tremor in just one hand. Tremors are common, but the disorder also commonly causes stiffness or slowing of movement.

Algorithm used and its accuracy table is given below.

| Algorithm | Accuracy | K-Fold    | RMSE     |MAE        | R2       |    Recall |Precision |F1|
|-----------|----------|-----------|----------|-----------|----------|-----------|----------|--|
| QDA |0.95 |0.80 (+/- 0.41)|0.22|0.05|0.79|1.0|0.9 |0.94|
| KNN | 0.70|0.70 (+/- 0.40)|0.54|0.3|-0.21|0.66|0.66|0.66|
| SVM | 0.95 |0.72 (+/- 0.38)|0.22|0.05|0.79|0.88|1.0|0.94|
|LDA|0.825|0.75 (+/- 0.34)|0.44|0.2|0.19|0.88|0.72|0.79|
|Naive Bayes algorithm|0.80|0.75 (+/- 0.34)|0.44|0.2|0.19|0.55|1.0|0.71|
|Decision tree|0.88|0.80 (+/- 0.25)|0.44|0.2|0.19|0.66|0.85|0.75|
|Random forest algorithm|0.93|0.77 (+/- 0.43)|0.22|0.05|0.79|0.88|1.0|0.94|
|AdaBoost|0.83|0.80 (+/- 0.31)|0.44|0.2|0.19|0.88|0.72|0.79|
|k-means clustering|0.58|0.80 (+/- 0.31)|0.74|0.55|-1.2|1.0| 0.45|0.62|
|XGBoost|0.90|0.80 (+/- 0.31)|0.38|0.15|0.39|0.88|0.8|0.84|
|Gradient Boosting|0.88|0.80 (+/- 0.35)|0.38|0.15|0.39|0.88|0.8|0.84|

Best model is QDA with 95% accuracy.

### Diabetes
Diabetes is a disease that occurs when your blood glucose, also called blood sugar, is too high. Blood glucose is your main source of energy and comes from the food you eat. Insulin, a hormone made by the pancreas, helps glucose from food get into your cells to be used for energy. Sometimes your body doesn’t make enough—or any—insulin or doesn’t use insulin well. Glucose then stays in your blood and doesn’t reach your cells.

Algorithm  used and its accuracy table is given below.

| Algorithm              | Accuracy |   K-Fold   |   RMSE   |   MAE   |    R2   |  Recall | Precision |    F1    |
|------------------------|----------|------------|----------|---------|---------|---------|-----------|---------|
| Decision Tree          |   0.79   |  0.71 (+/- 0.35) |   0.44   |   0.20  |   0.19  |   0.66  |   0.85    |   0.75  |
| KNN                    |   0.74   |  0.70 (+/- 0.40) |   0.54   |   0.30  |  -0.21  |   0.66  |   0.66    |   0.66  |
| SVM                    |   0.83   |  0.72 (+/- 0.38) |   0.22   |   0.05  |   0.79  |   0.88  |   1.00    |   0.94  |
| QDA                    |   0.77   |  0.80 (+/- 0.41) |   0.22   |   0.05  |   0.79  |   1.00  |   0.90    |   0.94  |
| LDA                    |   0.83   |  0.82 (+/- 0.10) |   0.41   |   0.17  |   0.29  |   0.83  |   0.82    |   0.83  |
| Naive Bayes Algorithm  |   0.80   |  0.83 (+/- 0.09) |   0.44   |   0.19  |   0.21  |   0.78  |   0.82    |   0.80  |
| Decision Tree          |   0.88   |  0.82 (+/- 0.08) |   0.48   |   0.23  |   0.08  |   0.75  |   0.80    |   0.77  |
| Random Forest          |   0.93   |  0.86 (+/- 0.00) |   0.30   |   0.09  |   0.61  |   0.95  |   0.87    |   0.91  |
| AdaBoost               |   0.83   |  0.83 (+/- 0.08) |   0.41   |   0.17  |   0.32  |   0.85  |   0.83    |   0.84  |
| K-Means Clustering     |   0.58   |  0.82 (+/- 0.11) |   0.76   |   0.58  |  -1.32  |   0.67  |   0.46    |   0.55  |
| XGBoost                |   0.90   |  82.37 %    |   0.30   |   0.09  |   0.61  |   0.87  |   0.87    |   0.91  |
| Gradient Boosting      |   0.88   |  0.82 (+/- 0.07) |   0.35   |   0.12  |   0.52  |   0.92  |   0.86    |   0.89  |


### Heart Disease
Heart disease is a general term that describes several types of heart conditions. The most common type of heart disease is coronary artery disease, which occurs when the blood vessels that supply blood to the heart become narrowed or blocked by a buildup of plaque. This buildup of plaque is called atherosclerosis. Atherosclerosis can occur in any blood vessel, but it most commonly affects the arteries that supply blood to the heart, brain, and legs.


Dependencies
------------
* Python 3.10

Installation
-----------

command to install all the dependencies
```bash
pip install -r requirements.txt
```
Docker 
----------
```bash
docker pull imostafizur/cse498r
```
Using this you run this project in your local machine. Also you can deploy it Cloud service(AWS, Azure and Google Cloud)

Local Machine
--------------
```bash
python manage.py runserver 
```
Before execute the command make sure you are in WebApp folder.


