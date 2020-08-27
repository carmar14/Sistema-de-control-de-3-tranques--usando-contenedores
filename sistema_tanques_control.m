clc
clear
close all

% Parameters value of three?tank system
mu13=0.5; mu20=0.675; mu32=0.5;
S=0.0154; Sn=5e-5; W=sqrt ( 2 * 9.81 );
% Output operat ing Points (m)
Y10=0.400; Y20=0.200; Y30=0.300;
% Input operat ing Points (m3/s )
U10=0.350e-004; U20=0.375e-004;
% Matrix A
A11=-(mu13*Sn*W)/ (2*S*sqrt (Y10-Y30 ) ) ; A12=0;
A13=-A11;
A21=0;A23=(mu32*Sn*W)/ ( 2*S*sqrt(Y30-Y20 ) ) ;
A22=-A23-((mu20*Sn*W)/ ( 2*S*sqrt(Y20 ) ) ) ;
A31=-A11 ; A32=A23 ; A33=-A32-A31 ;
A=[A11 A12 A13 ; A21 A22 A23 ; A31 A32 A33 ] ;
% Matrix B
B11=1/S ; B12=0;
B21=0;B22=1/S ;
B31=0;B32=0;
B=[B11 B12 ; B21 B22 ;B31 B32 ] ;
% Continuous to d i s c r e t s t a t e space transformat ion


tm=1;
[Ad, Bd] = c2d (A,B, tm) ;
Cd=eye(3); %La salida del sistema son los tres estados
K2=[-0.95 -0.32; -0.3 -0.91]*10e-4;
K1=[21.6 3 -5; 2.9 19 -4]*10e-4;
K=[K1 K2];

q_max=1.5*10e-4; %1.2
q_min=0;
h_max=0.62;
h_min=0;


t=0:3000;
q1=[0.4*ones(1,250) 0.45*ones(1,1250) 0.4*ones(1,1000) 0.45*ones(1,501)];
q2=[0.2*ones(1,400) 0.225*ones(1,1600) 0.2*ones(1,1001)];
t=t';
q1=q1'; %vector columna ref 1
q2=q2'; %vector columna ref 2

[n m]=size(q1); % n vector de tiempos en muestras

%Estados en el tiempo k
x1=zeros(n,1);
x2=zeros(n,1);
x3=zeros(n,1);

%Estados en el tiempo k+1
x1_k1=zeros(n,1);
x2_k1=zeros(n,1);
x3_k1=zeros(n,1);

%accion integral en el tiempo k
ai1=0;
ai2=0;

%accion integral en el tiempo k-1
ai1_k1=0;
ai2_k1=0;


%Proces con controlador
for i=1:n-1
    %calculo el error
    e1=q1(i)-x1(i);
    e2=q2(i)-x2(i);
    
    %calculo la accion de control u1 y u2
    ai1=e1+ai1_k1;
    ai2=e2+ai2_k1;
    ui1=K2(1,1)*ai1+K2(1,2)*ai2;
    ui2=K2(2,1)*ai1+K2(2,2)*ai2;
    ui1=-ui1; %accion integral
    ui2=-ui2; %accion integral
    up1=K1(1,1)*x1(i)+K1(1,2)*x2(i)+K1(1,3)*x3(i); 
    up2=K1(2,1)*x1(i)+K1(2,2)*x2(i)+K1(2,3)*x3(i); 
    up1=-up1; %accion propocional
    up2=-up2; %accion propocional
    u1=ui1+up1; %accion de control
    u2=ui2+up2; %accion de control
    %Saturacion para evitar da�os en los acutadores
    if u1>q_max
        u1=q_max;
    end
    
    if u2>q_max
        u2=q_max;
    end
    
    if u1<q_min
        u1=q_min;
    end
    
    if u2<q_min
        u2=q_min;
    end
    %actualizo
    ai1_k1=ai1;
    ai2_k1=ai2;
    
    %calculo los estados
    x1_k1(i)=Ad(1,:)*[x1(i);x2(i);x3(i)]+Bd(1,:)*[u1;u2];%A11*x1(i)+A12*x2(i)+A13*x3(i)+B11*u1+B12*u2;
    x2_k1(i)=Ad(2,:)*[x1(i);x2(i);x3(i)]+Bd(2,:)*[u1;u2];%A21*x1(i)+A22*x2(i)+A23*x3(i)+B21*u1+B22*u2;
    x3_k1(i)=Ad(3,:)*[x1(i);x2(i);x3(i)]+Bd(3,:)*[u1;u2];%A31*x1(i)+A32*x2(i)+A33*x3(i)+B31*u1+B32*u2;
    
    %actualizo los estados
    x1(i+1)=x1_k1(i);
    x2(i+1)=x2_k1(i);
    x3(i+1)=x3_k1(i);
  
end


plot(t,x1,'b',t,q1,'--r')
xlabel('Tiempo (s)')
ylabel('l_{1}(m)')
legend('Level 1','q_{1}(m^{3}/s)')
title('Altura del tanque 1')
figure
plot(t,x2,'b',t,q2,'--r')
xlabel('Tiempo (s)')
ylabel('l_{2}(m)')
legend('Level 2','q_{2}(m^{3}/s)')
title('Altura del tanque 2')
figure
plot(t,x3,'b')
xlabel('Tiempo (s)')
ylabel('l_{3}(m)')
title('Altura del tanque 3')



eig(Ad-Bd*K1); %Garantizar polos dentro del circulo unitario en lazo cerrado