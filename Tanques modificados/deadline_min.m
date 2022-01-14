clc
close all
clear

%-------Nodo medición-----
C=[15 30 30];
D=[1100 100 100];
P=[1100 100 100];

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

R=K_
for i=1:3
    k(i)=ceil(R/P(i));
end


Dmin=[0 0 0];
deadline=C;
%---------nueva minimizacion para T2----

i=1;
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

%---------nueva minimizacion para T2----
i=2;
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
D_=zeros(3,3);
D_(1,:)=D/10;

%----------Nodo medición---------

%----------Nodo control---------
C=[5 3 3];
D=[110 10 10];
P=[110 10 10];

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

R=K_
for i=1:3
    k(i)=ceil(R/P(i));
end


Dmin=[0 0 0];
deadline=C;
%---------nueva minimizacion para T2----

i=1;
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

%---------nueva minimizacion para T2----
i=2;
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
D_(2,:)=D;

%----------Nodo control---------

%----------Nodo actuación---------
C=10*[0.3 3 3];
D=10*[110 10 10];
P=10*[110 10 10];

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

R=K_
for i=1:3
    k(i)=ceil(R/P(i));
end


Dmin=[0 0 0];
deadline=C;
%---------nueva minimizacion para T2----

i=1;
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

%---------nueva minimizacion para T2----
i=2;
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
D_(3,:)=D/10;

%----------Nodo actuación---------
C=[1.5 5 0.3];
Dcgr=80;
Tsf=35;%36.6;%36.2;
Dmax(1)=Dcgr-(1.7+6.3+Tsf); %medicion
Dmax(2)=Dcgr-(7.5+6.3+Tsf); % control
Dmax(3)=Dcgr-(7.5+1.7); % actuacion

Dmax(1)=Dcgr-(C(2)+C(3)+Tsf); %medicion
Dmax(2)=Dcgr-(C(1)+C(3)+Tsf); % control
Dmax(3)=Dcgr-(C(1)+C(2)); % actuacion

