library(DAAG)
library(randomForest)
library(readxl)
library(readxl)
#train_data <- read_excel("the path of the dataset")

train_data_1<-train_data[,2:21]#independent variable
train_data_2<-train_data[,1]#dependent variable
train_data<-cbind(train_data_1,train_data_2)
View(train_data)
n<-ncol(train_data)

set.seed(100)
ind<-sample(2,nrow(train_data),replace=TRUE,prob=c(0.7,0.3))#70% training set, 30% test set
traindata<-train_data[ind==1,]
testdata<-train_data[ind==2,]

for(i in 1:(n-1))
{
  as.rf=randomForest(Species~.,train_data[ind==1,],ntree=50,nPerm=10,mtry=i,proximity=TRUE,importance=TRUE)
  print(as.rf)
}
as.rf$importance

ROCR_simple<-cbind(as.pred,testdata[,n])

library(ROCR)
pred <- prediction(ROCR_simple[,1], ROCR_simple[,2]) 
perf <- performance(pred,"tpr","fpr")
auc <- performance(pred,'auc')
sensspec<-performance(pred,"sens","spec")
precrec <- performance(pred, "prec", "rec")
plot(precrec)
plot(sensspec)
auc = unlist(slot(auc,"y.values"))
plot(perf,
     xlim=c(0,1), ylim=c(0,1),col='red',
     main=paste("ROC curve (", "AUC = ",auc,")"),
     lwd = 4, cex.main=1.5, cex.lab=1.5, cex.axis=2, font=2)
abline(0,1)
write.csv(perf@x.values,file="D:/The path where the file is saved/rocx.csv")
write.csv(perf@y.values,file="D:/The path where the file is saved/rocy.csv")
write.csv(sensspec@x.values,file="D:/The path where the file is saved/sensx.csv")
write.csv(sensspec@y.values,file="D:/The path where the file is saved/sensy.csv")
write.csv(precrec@x.values,file="D:/The path where the file is saved/precx.csv")
write.csv(precrec@y.values,file="D:/The path where the file is saved/precy.csv")
auc











