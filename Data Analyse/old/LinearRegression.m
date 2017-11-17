myData = importdata("abalone.data")
Length = myData.data(:,1);
Gender = ones(size(myData.textdata));
Weight = myData.data(:,4);
ClassRing = myData.data(:,8);
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
% % plot(myData.data(:,1),myData.data(:,2), 'ro');
% % hold on
% % p = polyfit(myData.data(:,1),myData.data(:,2), 1);
% % plot(myData.data(:,1), polyval(p, myData.data(:,1)))
% % plot(myData.data(:,2), myData.data(:,4),  'r.')
% % xlabel('diameter')
% % ylabel('weight')
% Length = myData.data(:,1)
Diameter = myData.data(:,2)
% Weight = myData.data(:,4)
% Shucked = myData.data(:,5)
% Viscera = myData.data(:,6)
% Shell = myData.data(:,7)
% 
% Sum = Shucked + Viscera + Shell
% X = [ones(length(Weight),1), Shucked, Viscera, Shell]
% logWeight = log(Weight)
% [b, bint, r, rint, stats] = regress(Weight, X)
% rcoplot(r,rint)

