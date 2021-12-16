clc
close all
clear

T=[3 3 10000 1000 1000]';
C=[1 1 17 37 158]';
D=[3 3 500 1000 1000]';

%ceil para redondear hacia arriba

R=zeros(5,1);

Ra=C;
Rn=R;
I=0;
for i=1:5
    while (Rn(i)~=Ra(i))
        
        Ra(i) = Rn(i);
       
        for j=1:i-1
            I=I+ceil(Ra(i)/T(j))*C(j);
        end

        Rn(i) = C(i)+I;
        I=0;

    end
end


%-------------tareas del proyecto--------


% T=[1 1 1]';
% C=[0.6 0.375 0.6]';
% D=[0.75 0.47 0.75]';

C=10*[0.3 3 3];
D=10*[110 10 10];
T=10*[110 10 10];

%ceil para redondear hacia arriba

R=zeros(3,1);

Ra=C;
Rn=R;
I=0;
for i=1:3
    while (Rn(i)~=Ra(i))
        
        Ra(i) = Rn(i);
       
        for j=1:i-1
            I=I+ceil(Ra(i)/T(j))*C(j);
        end

        Rn(i) = C(i)+I;
        I=0;

    end
end