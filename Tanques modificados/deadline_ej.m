clc
close all
clear
%----------task------
% ----tao={T1,T2,T3}
% ----T_i=(C_i,D_i,P_i)
% minimizar la secuencia T2,T1,T3
%papers:
%--H(t)=IMPROVEMENT IN FEASmILITY TESTING FOR REALTIME TASKS
%--deadlinemin: Minimum deadline calculation for periodic real-time
%               tasks in dynamic priority systems
C=[1 3 5];
D=[7 10 20];
P=[7 10 20];

K=1;

G=0;
for i=1:3
    G=G++ceil(K/P(i))*C(i);
end
K_=G;
G=0;


%--------calcular ICI-->R---

while (K_~=K)
    K=K_;
    for i=1:3
        G=G++ceil(K/P(i))*C(i);
    end
    K_=G;
    G=0;
end

R=K_;
for i=1:3
    k(i)=ceil(R/P(i));
end


Dmin=[0 0 0];
%---------nueva minimizacion para T2----
deadline=C;
i=2;
% for i=1:3
for s=0:k-1
    t=min(s*P(i)+D(i),R);
    deadline(i)=C(i);
    while t>(s*P(i)+C(i))
        H=0;
        for j=1:3
            H=H+C(j)*floor((t+P(j)-D(j))/P(j)); % calcula de H(t)
        end
        if (t-H)<C(i)
            deadline(i)=H+C(i)-s*P(i);
            break;
        end
        t=t-1;
        
    end
    Dmin(i)=max(Dmin(i),deadline(i));
    
end

D(i)=Dmin(i);

%---------nueva minimizacion para T1----
i=1;
% for i=1:3
for s=0:k-1
    t=min(s*P(i)+D(i),R);
    deadline(i)=C(i);
    while t>(s*P(i)+C(i))
        H=0;
        for j=1:3
            H=H+C(j)*floor((t+P(j)-D(j))/P(j));
        end
        if (t-H)<C(i)
            deadline(i)=H+C(i)-s*P(i);
            break;
        end
        t=t-1;
        
    end
    Dmin(i)=max(Dmin(i),deadline(i));
    
end

D(i)=Dmin(i);

%---------nueva minimizacion para T3----
i=3;
% for i=1:3
for s=0:k-1
    t=min(s*P(i)+D(i),R);
    deadline(i)=C(i);
    while t>(s*P(i)+C(i))
        H=0;
        for j=1:3
            H=H+C(j)*floor((t+P(j)-D(j))/P(j));
        end
        if (t-H)<C(i)
            deadline(i)=H+C(i)-s*P(i);
            break;
        end
        t=t-1;
        
    end
    Dmin(i)=max(Dmin(i),deadline(i));
    
end

D(i)=Dmin(i);