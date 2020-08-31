clear 
close all
clc

q_max=1.5*10e-4; %1.2
q_min=0;
q1=0.4;q2=0.2;x1=0;x2=0;x3=0;ai1k=0;ai2k=0;
K1=[0.0216    0.0030   -0.0050;
    0.0029    0.0190   -0.0040];
K2=[-0.9500   -0.3200;
    -0.3000   -0.9100];
K2=1.0e-03 *K2;

%calculo el error
e1=q1-x1;
e2=q2-x2;
ai1=e1+ai1k;
ai2=e2+ai2k;
ui1=K2(1,1)*ai1+K2(1,2)*ai2;
ui2=K2(2,1)*ai1+K2(2,2)*ai2;
ui1=-ui1; %accion integral
ui2=-ui2; %accion integral

up1=K1(1,:)*[x1;x2;x3];%K1(1,1)*x1(i)+K1(1,2)*x2(i)+K1(1,3)*x3(i);
up2=K1(2,:)*[x1;x2;x3];%K1(2,1)*x1(i)+K1(2,2)*x2(i)+K1(2,3)*x3(i);
up1=-up1; %accion propocional
up2=-up2; %accion propocional
u1=ui1+up1; %accion de control
u2=ui2+up2; %accion de control


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