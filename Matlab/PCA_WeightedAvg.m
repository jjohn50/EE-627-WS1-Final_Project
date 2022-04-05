clear all

data=csvread('82_features.csv',1.0);
Cols=data(:,[4 5 6 7 8 9 10 11]);
[coeff,score,latent] = pca(Cols);
figure(1);
bar(latent)
xlabel('Principal Component');
ylabel('Value');

figure(2);
labels = {'Component 1','Component 2','Component 3','Component 4','Component 5','Component 6','Component 7','Component 8'};
pie(latent)
legend(labels,'Location','south','Orientation','horizontal');

%mapcaplot(Cols)

figure(3)
scatter(score(:,[1]),score(:,[2]))

for i=4:1:11
    
    weights(i-3)=latent(i-3)/sum(latent);
    
end


for i=1:1:8
    
    Cols(:,i)=Cols(:,i)*weights(i);

end

for i=1:1:120000
    %names=strcat(string(data(:,3)),'_',string(data(:,2)));
    Output(i)=sum(Cols(i,:));
    
end
Output=rot90(Output,3);

%Output=vertcat(names,Output);

csvwrite('Output.csv', Output);
