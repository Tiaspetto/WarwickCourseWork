adult <-read.csv(file.choose(), header = F)
Yaxis <- adult[,c(10)]
# levels(Yaxis)[levels(Yaxis) %in% c("F","M")]<-"A"
# plot(Yaxis ~adult$V10)
ms = adult$V2;
with(adult, tapply(adult$V1, adult$V10, mean))
with(adult, tapply(ms, adult$V10, mean))
X = adult$V1+adult$V2+adult$V3
lift<-glm(Yaxis ~adult$V2,family="binomial", data = adult)
summary(lift)
predict(lift, type="response")
round(predict(lift, type="response"))
pairs<-(paste(round(predict(lift, type="response")),Yaxis))
summary(Yaxis)
