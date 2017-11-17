fid = fopen("adult.data");
myData = textscan(fid, '%d %s %d %s %d %s %s %s %s %s %d %d %d %s %s','delimiter', ',');


Gender = ones(size(myData{1,10}));

X = [Length Weight ClassRing];
for i=1:size(Gender)
   if(myData.textdata{i}~='I')
      Gender(i) = 0 ;   
   end
end
b = glmfit(X,[Gender ones(size(Gender,1),1)],'binomial','link','logit')
fitted = glmval(b,X,'logit');
for i=1:size(X)
%    yfit(i) = 1/(1+exp(-(b(1)+b(2)*X(i,1)+b(2)*X(i,2)+b(3)*X(i,3))));
   if(fitted(i)>=0.5)
       yfit(i) = 1;
   else
       yfit(i) = 0;
   end
end
plot(X, yfit', '.')
hold on
plot(X, Gender, 'o')
fprintf('Train Accuracy: %f\n', mean(double(yfit' == Gender)) * 100);