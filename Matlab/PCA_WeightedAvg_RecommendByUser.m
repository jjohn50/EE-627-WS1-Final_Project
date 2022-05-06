clear all

data=csvread('Output.csv',0);
Cols=data(:,1);

sum=0;

for i=1:1:120000
    sum=sum+Cols(i);
    if(mod(i,6)==0)
        thresh(i/6)=sum/6;
        sum=0;
    end
end

j=1;
for i=1:1:120000
    if Cols(i)>thresh(j)
        Output(:,i)=1;
    else
        Output(:,i)=0;
    end
    
    if(mod(i,6)==0)
        j=j+1;
    end
    
end

Output=rot90(Output,3);


