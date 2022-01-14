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
deadline=C;
%---------nueva minimizacion para T2----

i=2;
n=1;
tt=[];
h=[];
% for i=1:3
for s=0:k(i)-1
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
        tt(n)=t;        
        h(n)=H;
        t=t-1;
        n=n+1;
        
    end
    Dmin(i)=max(Dmin(i),deadline(i));
    
end

D(i)=Dmin(i);

%---------nueva minimizacion para T1----
i=1;
tt=[];
h=[];
% for i=1:3
n=1;
% for i=1:3
for s=0:k(i)-1
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
        tt(n)=t;        
        h(n)=H;
        t=t-1;
        n=n+1;
        
    end
    Dmin(i)=max(Dmin(i),deadline(i));
    
end

D(i)=Dmin(i);

%---------nueva minimizacion para T3----
i=3;
n=1;
tt=[];
h=[];
% for i=1:3
for s=0:k(i)-1
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
        tt(n)=t;
        h(n)=H;
        t=t-1;
        n=n+1;
        
    end
    Dmin(i)=max(Dmin(i),deadline(i));
    
end

D(i)=Dmin(i);
%------------ejemplo sistema de pendulos-----

C=[7 7 7];
D=[20 29 35];
P=[20 29 35];

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
deadline=C;
%---------nueva minimizacion para T3----
tt=[];
h=[];
i=3;
% for i=1:3
for s=0:k(i)-1
    t=min(s*P(i)+D(i),R);
    deadline(i)=C(i);
    while t>(s*P(i)+C(i))
        tt(n)=t;
        H=0;
        for j=1:3
            H=H+C(j)*floor((t+P(j)-D(j))/P(j)); % calcula de H(t)
        end
         h(n)=H;
        if (t-H)<C(i)
            deadline(i)=H+C(i)-s*P(i);
            break;
        end
        t=t-1;
        n=n+1;
    end
    Dmin(i)=max(Dmin(i),deadline(i));
    
end

D(i)=Dmin(i);

%---------nueva minimizacion para T1----
tt=[];
h=[];
i=1;
% for i=1:3
for s=0:k(i)-1
    t=min(s*P(i)+D(i),R);
    deadline(i)=C(i);
    while t>(s*P(i)+C(i))
        tt(n)=t;
        H=0;
        for j=1:3
            H=H+C(j)*floor((t+P(j)-D(j))/P(j)); % calcula de H(t)
        end
         h(n)=H;
        if (t-H)<C(i)
            deadline(i)=H+C(i)-s*P(i);
            break;
        end
        t=t-1;
        n=n+1;
    end
    Dmin(i)=max(Dmin(i),deadline(i));
    
end

D(i)=Dmin(i);

%---------nueva minimizacion para T2----
tt=[];
h=[];
i=2;
% for i=1:3
for s=0:k(i)-1
    t=min(s*P(i)+D(i),R);
    deadline(i)=C(i);
    while t>(s*P(i)+C(i))
        tt(n)=t;
        H=0;
        for j=1:3
            H=H+C(j)*floor((t+P(j)-D(j))/P(j)); % calcula de H(t)
        end
         h(n)=H;
        if (t-H)<C(i)
            deadline(i)=H+C(i)-s*P(i);
            break;
        end
        t=t-1;
        n=n+1;
    end
    Dmin(i)=max(Dmin(i),deadline(i));
    
end

D(i)=Dmin(i);