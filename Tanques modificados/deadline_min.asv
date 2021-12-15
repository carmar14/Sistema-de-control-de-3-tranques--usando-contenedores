clc
close all
clear

Tm=110;
Dm=110;
Dc=110;
Da=110;
D= [Dm Dc Da];
deadline = [1.5 5 0.3];
WCET = [1.5 5 0.3];
Dmin = [0 0 0];

%----tareas adicionales----
WCETi=3;
Di=10;
Ti=10;


%-------------tareas del proyecto--------


T=Tm*[1 1 1]';
C=[1.5 5 0.3]';
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

R=Rn;
k=ceil(R./T);
j=length(0:0.1:R(1));

%------test de factibilidad Ripoll-- 
t=0;
C=[1.5 3 3]; %medicion
D=0.8*[110 10 10];
P=[110 10 10];
c=sum(C./P);
gama= sum(C.*(1-D./P));
L= gama/(1-c);
G=0;
H=0;
for i =1:3
    G=G+C(i)*ceil(t/P(i));
    H=H+C(i)*floor((t+P(i)-D(i))/P(i));
end

while (t<=min(G,L) && t>=H)         
    t=t+1;
    for i =1:3
    G=G+C(i)*ceil(t/P(i));
    H=H+C(i)*floor((t+P(i)-D(i))/P(i));
    end  
end

for t=0:0.1:R(1)
    for i=1:3
        H(j)=WCET(i)*floor((t/110));
        j=j+1;
    end
end



for i=1:3
    for s=0:k-1
        t=min(s*T(i)+D(i),R(i));
        deadline = C;
        while(t>s*T(i)+C(i))%deadline(i))
            H(t)=4;
            if(t-H(t)<C(i))
                deadline(i)=H(i)+WCET(i)-s*T(i);
            end
        t=t-1;
        end
        Dmin=max(Dmin(i),deadline(i));
    end
end