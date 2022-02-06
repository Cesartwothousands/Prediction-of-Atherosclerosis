# Prediction-of-Atherosclerosis
This repo is about code and models of the paper: **Prediction of atherosclerosis using machine learning based on operations research**. Contributed by _Zihan Chen_, _Minhui Yang_, _Yuhang Wen_, _Songyan Jiang_, _Wenjun Liu_ and _Hui Huang_.

You can import your own dataset into the paths provided by Feature Selection and Prediction Model, we've added sufficient comments to the code.

If you have any questions about our work, please feel free to contact us.

## Feature Selection
We use Python to finish the feature selection based on Dijkstra's algorithm.
***
Feature selection involves repeatedly selecting the number of features to retain, and we did not design automated function of this part.

## Prediction Model
We use R to build the Atherosclerosis prediction model based on radom forest.
***
The input to rf_prediction.R is the dataset. <br>
Te output is the ROC result of the prediction model via random forest. <br>
train_data_1 is independent variable and train_data_2 is dependent variable. <br>

## Dataset
We obtained the data from a summation study conducted from January 2016 to December 2017 at Affiliated Hospital of Nanjing University of Chinese Medicine, while the study here was approved by the hospital's ethics committee after written informed consent was obtained from all patients. 

25 features are retained after data analysis. We got 622 samples with all the features. Under the guidance of relevant experts, 304 samples are seen as atherosclerosis risk group and 318 samples are seen as a control group without atherosclerosis risk. 

## Cross Validation
In addition, the data is randomly divided into a training set of 0.7 and a test set of 0.3 in preparation for the cross-validation.
