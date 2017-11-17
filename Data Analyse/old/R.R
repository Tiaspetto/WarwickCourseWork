adults <-read.csv(file.choose(), header = F)
head(adults,2)
names(adults)<-c("Age","Workclass","FinalWeight","Education","EducationNumer","MaritalStatus","Occupation","Relationship","Race","Sex","CapitalGain","CapitalLoss","HoursWeek","NativeCountry","Income")
head(adults,2)
adults$Sex<-ifelse(adults$Sex==" Male",0,1)
str(adults)
library(caret)
dmy<-dummyVars("~.",data=adults)
adultsTrsf<-data.frame(predict(dmy,newdata=adults))
dim(adults)
dim(adultsTrsf)
head(adultsTrsf)
str(adultsTrsf)
cor.prob<-function(X,dfr=nrow(X)-2){
  R<-cor(X,use="pairwise.complete.obs")
  above<-row(R)<col(R)
  r2<-R[above]^2
  Fstat<-r2*dfr/(1-r2)
  R[above]<-1-pf(Fstat,1,dfr)
  R[row(R)==col(R)]<-NA
  R
}
flattenSquareMatrix<-function(m){
  if((class(m) !="matrix") | (nrow(m) !=ncol(m))) stop("Must be asquare matrix.")
  if(!identical(rownames(m),colnames(m))) stop("Row and column names must be equal.")
  ut<-upper.tri(m)
  data.frame(i=rownames(m)[row(m)[ut]],
             j=rownames(m)[col(m)[ut]],
             cor=t(m)[ut],
             p=m[ut])
}
corMasterList<-flattenSquareMatrix(cor.prob(adultsTrsf))
dim(corMasterList)
head(corMasterList)
corList<-corMasterList[order(-abs(corMasterList$cor)),]
head(corList)
selectedSub<-subset(corList,(abs(cor)>0.1 & j =="Sex"))
bestSub<-as.character(selectedSub$i[c(1,2,3,4,5,6,7)])
library(psych)
pairs.panels(adultsTrsf[c(bestSub,"Sex")])

glm.out<-glm(adultsTrsf$Sex~adultsTrsf$Relationship..Husband+adultsTrsf$MaritalStatus..Married.civ.spouse+adultsTrsf$Relationship..Unmarried+adultsTrsf$Relationship..Wife+adultsTrsf$Occupation..Adm.clerical+adultsTrsf$MaritalStatus..Divorced+adultsTrsf$Occupation..Craft.repair+adultsTrsf$MaritalStatus..Widowed,family="binomial")
summary(glm.out)
logit.predictions <- ifelse(predict(glm.out) > 0.5,1, 0)
table(adultsTrsf$Sex,logit.predictions)
pairs<-(paste(round(predict(glm.out, type="response")),adultsTrsf$Sex))
summary(pairs)
