clc
clear
close all

%Parameters value of three?tank system
mu13=0.5; mu20=0.675; mu32=0.5;
S=0.0154; Sn=5e-5; W=sqrt ( 2 * 9.81 );
%Output operat ing Points (m)
Y10=0.400; Y20=0.200; Y30=0.300;
%Input operat ing Points (m3/s )
U10=0.350e-004; U20=0.375e-004;
%Matrix A
A11=-(mu13*Sn*W)/ (2*S*sqrt (Y10-Y30 ) ) ; A12=0;
A13=-A11;
A21=0;A23=(mu32*Sn*W)/ ( 2*S*sqrt(Y30-Y20 ) ) ;
A22=-A23-((mu20*Sn*W)/ ( 2*S*sqrt(Y20 ) ) ) ;
A31=-A11 ; A32=A23 ; A33=-A32-A31 ;
A=[A11 A12 A13 ; A21 A22 A23 ; A31 A32 A33 ] ;
%Matrix B
B11=1/S ; B12=0;
B21=0;B22=1/S ;
B31=0;B32=0;
B=[B11 B12 ; B21 B22 ;B31 B32 ] ;
%Continuous to d i s c r e t s t a t e space transformat ion


tm=1;
[Ad, Bd] = c2d (A,B, tm) ;
Cd=eye(3); %La salida del sistema son los tres estados
K2=[-0.95 -0.32; -0.3 -0.91]*10e-4;
K1=[21.6 3 -5; 2.9 19 -4]*10e-4;
K=[K1 K2];

%valore maximos y minimos para evitar daños
q_max=1.5*10e-4; %1.2
q_min=0;
h_max=0.62;
h_min=0;

%Ganancia del observador de Luenberguer
L= [0.9899 0.0005
    0.0004 0.9894
    0.0108 0.0107];


%Diseños de UIOS
C1=Cd(2,:);
C2=Cd(1,:);
Fd1=[1.0e-4; 1.0; 1.0e-4];
Fd2=[1.0; 1.0e-4; 1.0e-4];

[F1,T1,K1U,H1]=uio_linear (Ad,Bd,C1,Fd1); %UIO1 usa x2 para aislar x1
[F2,T2,K2U,H2]=uio_linear (Ad,Bd,C2,Fd2); %UIO2 usa x1 para asilar x2

% F1=[0.9888 1.0000 0.0112
%     0 0.0010 0
%     0.0112 -0.9890 0.9776];
%
% F2=[0.0010 0 0
%     -1.0000 0.9781 0.0111
%     -0.9889 0.0111 0.9776];

%referencias
t=0:3000;
q1=[0.4*ones(1,250) 0.45*ones(1,1250) 0.4*ones(1,1000) 0.45*ones(1,501)];
q2=[0.2*ones(1,400) 0.225*ones(1,1600) 0.2*ones(1,1001)];
t=t';
q1=q1'; %vector columna ref 1
q2=q2'; %vector columna ref 2

ataque=1;
[n m]=size(q1); % n vector de tiempos en muestras

%Estados en el tiempo k
x1=zeros(n,1);
x2=zeros(n,1);
x3=zeros(n,1);

%Estados en el tiempo k+1
x1_k1=zeros(n,1);
x2_k1=zeros(n,1);
x3_k1=zeros(n,1);

%Estados Luebenguer en el tiempo k
x1e=zeros(n,1);
x2e=zeros(n,1);
x3e=zeros(n,1);

%Estados  Luenberguer en el tiempo k+1
x1_k1e=zeros(n,1);
x2_k1e=zeros(n,1);
x3_k1e=zeros(n,1);

%Estados UIO1 en el tiempo k
x1u1=zeros(n,1);
x2u1=zeros(n,1);
x3u1=zeros(n,1);

%Estados UIO1 en el tiempo k+1
x1_k1u1=zeros(n,1);
x2_k1u1=zeros(n,1);
x3_k1u1=zeros(n,1);

y1u1=zeros(n,1);
y2u1=zeros(n,1);
y3u1=zeros(n,1);

%Estados UIO2 en el tiempo k
x1u2=zeros(n,1);
x2u2=zeros(n,1);
x3u2=zeros(n,1);

%Estados UIO2 en el tiempo k+1
x1_k1u2=zeros(n,1);
x2_k1u2=zeros(n,1);
x3_k1u2=zeros(n,1);

y1u2=zeros(n,1);
y2u2=zeros(n,1);
y3u2=zeros(n,1);

%accion integral en el tiempo k
ai1=0;
ai2=0;

%accion integral en el tiempo k-1
ai1_k1=0;
ai2_k1=0;

u1=0;
u2=0;

%umbrales
%detección
Th_det=6e-5;
ad=zeros(n,1);

%aislamiento uio1
Th_uio1_on=6e-3;
Th_uio1_off=1e-5;
aiu11=zeros(n,1);
aiu12=zeros(n,1);

%aislamiento uio12
Th_uio2_on=1e-2;
Th_uio2_off=1e-5;
aiu21=zeros(n,1);
aiu22=zeros(n,1);

%entradas del sistema
u11=zeros(n,1);
u22=zeros(n,1);

%vectores de ataque magnitud estimada
v1=zeros(n,1);
v2=zeros(n,1);



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
    %Saturacion para evitar daños en los acutadores
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
    
    %accion de control
    u11(i)=u1;
    u22(i)=u2;
    %actualizo
    ai1_k1=ai1;
    ai2_k1=ai2;
    
    %calculo los estados
    x1_k1(i)=Ad(1,:)*[x1(i);x2(i);x3(i)]+Bd(1,:)*[u1;u2];%A11*x1(i)+A12*x2(i)+A13*x3(i)+B11*u1+B12*u2;
    x2_k1(i)=Ad(2,:)*[x1(i);x2(i);x3(i)]+Bd(2,:)*[u1;u2];%A21*x1(i)+A22*x2(i)+A23*x3(i)+B21*u1+B22*u2;
    x3_k1(i)=Ad(3,:)*[x1(i);x2(i);x3(i)]+Bd(3,:)*[u1;u2];%A31*x1(i)+A32*x2(i)+A33*x3(i)+B31*u1+B32*u2;
    
    %ataques
    if ataque==1
        if i>=600 && i<=650 || i>=1800 && i<=1900 %atques en el sensor 2
%             x_k1(i)=x2_k1(i)-0.02;
            x2(i)=x2_k1(i)+0.07;
        end
        
        if i>=800 && i<=900 || i>=2800 && i<=2870%atques en el sensor 1
%             x1_k1(i)=x1_k1(i)-0.03;
            x1(i)=x1_k1(i)+0.05;
        end
    end
    
    %actualizo los estados
    x1(i+1)=x1_k1(i);
    x2(i+1)=x2_k1(i);
    x3(i+1)=x3_k1(i);
    
    
    %Deteccion y aislamiento
    %if (i>=10)
    
    %calculo los estados estimados de Luenberguer
    x1_k1e(i)=Ad(1,:)*[x1e(i);x2e(i);x3e(i)]+Bd(1,:)*[u1;u2]+L(1,1)*(x1(i)-x1e(i))+L(1,2)*(x2(i)-x2e(i));%A11*x1(i)+A12*x2(i)+A13*x3(i)+B11*u1+B12*u2;
    x2_k1e(i)=Ad(2,:)*[x1e(i);x2e(i);x3e(i)]+Bd(2,:)*[u1;u2]+L(2,1)*(x1(i)-x1e(i))+L(2,2)*(x2(i)-x2e(i));%A21*x1(i)+A22*x2(i)+A23*x3(i)+B21*u1+B22*u2;
    x3_k1e(i)=Ad(3,:)*[x1e(i);x2e(i);x3e(i)]+Bd(3,:)*[u1;u2]+L(3,1)*(x1(i)-x1e(i))+L(3,2)*(x2(i)-x2e(i));%A31*x1(i)+A32*x2(i)+A33*x3(i)+B31*u1+B32*u2;
    
    %actualizo los estados estimados de Luenberguer
    x1e(i+1)=x1_k1e(i);
    x2e(i+1)=x2_k1e(i);
    x3e(i+1)=x3_k1e(i);
    
    %calculo los estados estimados de UIO1
    x1_k1u1(i)=F1(1,:)*[x1u1(i);x2u1(i);x3u1(i)]+T1(1,:)*Bd*[u1;u2]+K1U(1)*x2(i);%A11*x1(i)+A12*x2(i)+A13*x3(i)+B11*u1+B12*u2;
    x2_k1u1(i)=F1(2,:)*[x1u1(i);x2u1(i);x3u1(i)]+T1(2,:)*Bd*[u1;u2]+K1U(2)*x2(i);%A21*x1(i)+A22*x2(i)+A23*x3(i)+B21*u1+B22*u2;
    x3_k1u1(i)=F1(3,:)*[x1u1(i);x2u1(i);x3u1(i)]+T1(3,:)*Bd*[u1;u2]+K1U(3)*x2(i);%A31*x1(i)+A32*x2(i)+A33*x3(i)+B31*u1+B32*u2;
    
    %actualizo los estados estimados de UI1O1
    x1u1(i+1)=x1_k1u1(i);
    x2u1(i+1)=x2_k1u1(i);
    x3u1(i+1)=x3_k1u1(i);
    
    %Salidas estimadas del UIO1
    y1u1(i)=x1u1(i)+H1(1)*x2(i);
    y2u1(i)=x2u1(i)+H1(2)*x2(i);
    y3u1(i)=x3u1(i)+H1(3)*x2(i);
    
    %calculo los estados estimados de UIO2
    x1_k1u2(i)=F2(1,:)*[x1u2(i);x2u2(i);x3u2(i)]+T2(1,:)*Bd*[u1;u2]+K2U(1)*x1(i);%A11*x1(i)+A12*x2(i)+A13*x3(i)+B11*u1+B12*u2;
    x2_k1u2(i)=F2(2,:)*[x1u2(i);x2u2(i);x3u2(i)]+T2(2,:)*Bd*[u1;u2]+K2U(2)*x1(i);%A21*x1(i)+A22*x2(i)+A23*x3(i)+B21*u1+B22*u2;
    x3_k1u2(i)=F2(3,:)*[x1u2(i);x2u2(i);x3u2(i)]+T2(3,:)*Bd*[u1;u2]+K2U(3)*x1(i);%A31*x1(i)+A32*x2(i)+A33*x3(i)+B31*u1+B32*u2;
    
%     xuio(:,i)=F2*[x1u2(i);x2u2(i);x3u2(i)]+T2*Bd*[u1;u2]+K2U*x1(i);
%     xuio(:,i+1)=xuio(:,i);
%     y(:,i)=xuio(:,i)+H2*x1(i);
    
    %actualizo los estados estimados de UIO2
    x1u2(i+1)=x1_k1u2(i);
    x2u2(i+1)=x2_k1u2(i);
    x3u2(i+1)=x3_k1u2(i);
    
    %Salidas estimadas del UIO2
    y1u2(i)=x1u2(i)+H2(1)*x1(i);
    y2u2(i)=x2u2(i)+H2(2)*x1(i);
    y3u2(i)=x3u2(i)+H2(3)*x1(i);
    
    %Alarmas
    %deteccion
    rd1=x1(i)-x1e(i);
    rd2=x2(i)-x2e(i);
    
    norm_rd=sqrt(rd1.^2+rd2.^2);
    
    if norm_rd >=Th_det
        ad(i)=1;
    else
        ad(i)=0;
    end
    
    %aislamiento
    %aislamiento uio1
    
    rdu11=abs(x1(i)-y1u1(i));
    rdu12=abs(x2(i)-y2u1(i));
    if (abs(rdu11)  >= Th_uio1_on && abs(rdu12)  <= Th_uio1_off)
        aiu11(i)=1;
    else
        aiu11(i)=0;
    end
    
    
    
    %aislamiento uio12
    rdu21=abs(x1(i)-y1u2(i));
    rdu22=abs(x2(i)-y2u2(i));
    if (abs(rdu21)  <= Th_uio2_off && abs(rdu22)  >= Th_uio2_on)
        aiu22(i)=1;
    else
        aiu22(i)=0;
    end
    
    %estimacion del ataque
    %ataque primer sensor
    v1(i)=(y1u2(i)-y1u1(i))*aiu11(i)*ad(i);
    %ataque segundo sensor
    v2(i)=(y2u1(i)-y2u2(i))*aiu22(i)*ad(i);
    %end
end

subplot(3,1,1)
plot(t,x1,'b',t,q1,'--r',t,x1e,'k')
xlabel('Tiempo (s)')
ylabel('l_{1}(m)')
legend('Level 1','q_{1}(m)','level 1 est')
title('Altura del tanque 1')

subplot(3,1,2)
plot(t,x1,'b',t,y1u1,'--r')
xlabel('Tiempo (s)')
ylabel('l_{1}(m)')
legend('Level 1','level 1 uio1')
title('Altura del tanque 1')

subplot(3,1,3)
plot(t,x1,'b',t,y1u2,'--r')
xlabel('Tiempo (s)')
ylabel('l_{1}(m)')
legend('Level 1','level 1 uio2')
title('Altura del tanque 1')

figure
subplot(3,1,1)
plot(t,x2,'b',t,q2,'--r',t,x2e,'k')
xlabel('Tiempo (s)')
ylabel('l_{2}(m)')
legend('Level 2','q_{2}(m)','level 2 est')
title('Altura del tanque 2')

subplot(3,1,2)
plot(t,x2,'b',t,y2u1,'--r')
xlabel('Tiempo (s)')
ylabel('l_{2}(m)')
legend('Level 2','level 2 uio1')
title('Altura del tanque 2')

subplot(3,1,3)
plot(t,x2,'b',t,y2u2,'--r')
xlabel('Tiempo (s)')
ylabel('l_{2}(m)')
legend('Level 2','level 2 uio2')
title('Altura del tanque 2')

figure
subplot(3,1,1)
plot(t,x3,'b',t,x3e,'k')
xlabel('Tiempo (s)')
ylabel('l_{3}(m)')
legend('Level 3','level 3 est')
title('Altura del tanque 3')

subplot(3,1,2)
plot(t,x3,'b',t,y3u1,'--r')
xlabel('Tiempo (s)')
ylabel('l_{3}(m)')
legend('Level 3','level 3 uio1')
title('Altura del tanque 3')

subplot(3,1,3)
plot(t,x3,'b',t,y3u2,'--r')
xlabel('Tiempo (s)')
ylabel('l_{3}(m)')
legend('Level 3','level 3 uio2')
title('Altura del tanque 3')

rd1=x1-x1e;
rd2=x2-x2e;

norm_rd=sqrt(rd1.^2+rd2.^2);
figure
% subplot(2,1,1)
plot(t,norm_rd,'--r')
xlabel('Tiempo (s)')
ylabel('residual detection(m)')

rdu11=abs(x1-y1u1);
rdu12=abs(x2-y2u1);
figure
subplot(2,1,1)
plot(t,rdu11,'--r')
xlabel('Tiempo (s)')
ylabel('residual isolation x1_uio1(m)')
subplot(2,1,2)
plot(t,rdu12,'--r')
xlabel('Tiempo (s)')
ylabel('residual isolation x2_uio1(m)')

rdu21=abs(x1-y1u2);
rdu22=abs(x2-y2u2);
figure
subplot(2,1,1)
plot(t,rdu21,'--r')
xlabel('Tiempo (s)')
ylabel('residual isolation x1_uio2(m)')
subplot(2,1,2)
plot(t,rdu22,'--r')
xlabel('Tiempo (s)')
ylabel('residual isolation x2_uio2(m)')


% figure
% subplot(2,1,1)
% plot(t,x1-y1u1,'--r')
% xlabel('Tiempo (s)')
% ylabel('l_{1}-l_{1_{uio1}}(m)')
% subplot(2,1,2)
% plot(t,x2-y2u1,'--r')
% xlabel('Tiempo (s)')
% ylabel('l_{2}-l_{2_{uio1}}(m)')
%
% figure
% subplot(2,1,1)
% plot(t,x1-y1u2,'--r')
% xlabel('Tiempo (s)')
% ylabel('l_{1}-l_{1_{uio2}}(m)')
% subplot(2,1,2)
% plot(t,x2-y2u2,'--r')
% xlabel('Tiempo (s)')
% ylabel('l_{2}-l_{2_{uio2}}(m)')

figure
plot(t,u11,'r')
title('Accion de control u1')
xlabel('Tiempo (s)')
ylabel('u_{1}(m^{3}/s)')

figure
plot(t,u22,'r')
title('Accion de control u2')
xlabel('Tiempo (s)')
ylabel('u_{2}(m^{3}/s)')

figure
title('Alarmas')
subplot(3,1,1)
plot(t,ad,'r')
xlabel('Tiempo (s)')
title('Alarma deteccion')

subplot(3,1,2)
plot(t,aiu11,'r')
xlabel('Tiempo (s)')
title('Alarma aislamiento sensor 1')

subplot(3,1,3)
plot(t,aiu22,'r')
xlabel('Tiempo (s)')
title('Alarma aislamiento sensor 2')

figure
title('Esimacion del ataque')
subplot(2,1,1)
plot(t,v1,'r')
xlabel('Tiempo (s)')
title('Ataque sensor 1')

subplot(2,1,2)
plot(t,v2,'r')
xlabel('Tiempo (s)')
title('Ataque sensor 2')

eig(Ad-Bd*K1); %Garantizar polos dentro del circulo unitario en lazo cerrado