clear
close all
clc

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
Cd=eye(3);
K2=[-0.95 -0.32; -0.3 -0.91]*10e-4;
K1=[21.6 3 -5; 2.9 19 -4]*10e-4;
K=[K1 K2];

q_max=1.5*10e-4; %1.2
q_min=0;
h_max=0.62;
h_min=0;

aadis= [Ad zeros(3,3);-Cd ones(3,3)];
badis=[Bd;zeros(3,2)];
pda=[0.92 0.97 0.9 0.95 0.94];
% kt=place(aadis,badis,pda)
L=[0.9995 0.0005 
   0.0005 0.9995 
   45.0167 42.5017 ];
L= [0.9899 0.0005 
    0.0004 0.9894 
    0.0108 0.0107];
% L=[ 0.9995    0.0005
%     0.0005    0.9995
%    45.0167   42.5017];
% L=zeros(

t=0:3000;
q1=[0.4*ones(1,250) 0.45*ones(1,1250) 0.4*ones(1,1000) 0.45*ones(1,501)];
q2=[0.2*ones(1,400) 0.225*ones(1,1600) 0.2*ones(1,1001)];
t=t';
q1=q1';
q2=q2';


eig(Ad-Bd*K1);



