clc
clear
close all

%Parameters value of three?tank system
mu13=0.5*10; mu20=0.675*10; mu32=0.5*10;
S=0.0154; Sn=50*5e-5; W=sqrt ( 2 * 9.81 );
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
% 
C=eye(3);
D=zeros(3,2);
ve=ss(A,B,C,D);
step(ve)
close all

tm=0.005;
tm2=0.005;
H1=tf([0.65 8],[1 0]);
H1d=c2d(H1,tm2);

% H2=tf();
[Ad, Bd] = c2d(A,B,tm) ;
Cd=eye(3); %La salida del sistema son los tres estados
Ada = [Ad zeros(3,2);
      -Cd(1:2,:) ones(2,2)];
Bda = [Bd; zeros(2,2)];
% Bd1 = [Bd(:,1); 0];
pc = [-0.0834  -0.0305  -0.0408   -100  -120];
pd= exp(pc*tm);%[0.92 0.97 0.96 0.95 0.94];
% K=acker(Ada, Bd1,pd)
% K = place(Ada,Bda,pd);
% K1= K(:,1:3);
% K2=K(:,4:5);
K2=[-0.95 -0.32; -0.3 -0.91]*10e-4;
K1=[21.6 3 -5; 2.9 19 -4]*10e-4;
K=[K1 K2];

%valore maximos y minimos para evitar daños
q_max=1.5*10e-4; %1.2
q_min=0;
h_max=0.62;
h_min=0;

%referencias
t=0:tm:3000*tm-tm;
% [m n]=size(t); 
% q1=zeros(n,1);
% q2=zeros(n,1);
q1=[0.4*ones(1,250) 0.45*ones(1,1250) 0.4*ones(1,1000) 0.45*ones(1,500)];
q2=[0.2*ones(1,400) 0.225*ones(1,1600) 0.2*ones(1,1000)];
% b = 250;
% a= 100;
% r1 = (b-a).*rand(1) + a;
% b1 = 400;
% a1= 100;
% r2 = (b1-a1).*rand(1) + a1;
% for i=1:n
%     if i < r1
%         q1(i) = r1;
%     else
%         b = 250+r1;
%         a= r1;
%         r1 = (b-a).*rand(1) + a;
%     end
%     
%     if r2 < i
%         q2(i) = r2;
%     else
%         b1 = 400+r2;
%         a1= r2;%100;
%         r2 = (b1-a1).*rand(1) + a1;
%     end
% end
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

%entradas del sistema
u11=zeros(n,1);
u22=zeros(n,1);

%accion integral en el tiempo k
ai1=0;
ai2=0;

%accion integral en el tiempo k-1
ai1_k1=0;
ai2_k1=0;

u1=0;
u2=0;

ek1=0;
ek2=0;
uk1=0;
uk2=0;

for i=1:n-1
    %calculo el error
    e1=q1(i)-x1(i);
    e2=q2(i)-x2(i);
    
    %calculo la accion de control u1 y u2
    u1 = 0.65*e1-0.61*ek1+uk1;
    u2 = 0.65*e2-0.61*ek2+uk2;
    ek1=e1;
    ek2=e2;
    uk1=u1;
    uk2=u2;
    %     ai1=e1+ai1_k1;
%     ai2=e2+ai2_k1;
%     ui1=K2(1,1)*ai1+K2(1,2)*ai2;
%     ui2=K2(2,1)*ai1+K2(2,2)*ai2;
%     ui1=-ui1; %accion integral
%     ui2=-ui2; %accion integral
%     up1=K1(1,1)*x1(i)+K1(1,2)*x2(i)+K1(1,3)*x3(i);
%     up2=K1(2,1)*x1(i)+K1(2,2)*x2(i)+K1(2,3)*x3(i);
%     up1=-up1; %accion propocional
%     up2=-up2; %accion propocional
%     u1=ui1+up1; %accion de control
%     u2=ui2+up2; %accion de control
    %Saturacion para evitar daños en los acutadores
%     if u1>q_max
%         u1=q_max;
%     end
%     
%     if u2>q_max
%         u2=q_max;
%     end
%     
%     if u1<q_min
%         u1=q_min;
%     end
%     
%     if u2<q_min
%         u2=q_min;
%     end
    
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
   
    %actualizo los estados
    x1(i+1)=x1_k1(i);
    x2(i+1)=x2_k1(i);
    x3(i+1)=x3_k1(i);
end

subplot(1,3,1)
plot(t,x1,'b',t,q1,'--r')
xlabel('Tiempo (s)')
ylabel('l_{1}(m)')
legend('Level 1','q_{1}(m)')
title('Altura del tanque 1')

subplot(1,3,2)
plot(t,x2,'b',t,q2,'--r')
xlabel('Tiempo (s)')
ylabel('l_{2}(m)')
legend('Level 2','q_{2}(m)')
title('Altura del tanque 2')


subplot(1,3,3)
plot(t,x3,'b')
xlabel('Tiempo (s)')
ylabel('l_{3}(m)')
legend('Level 3')
title('Altura del tanque 3')

% close all
