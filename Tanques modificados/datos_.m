clc
clear
close all

t=2;
%----------datos rt--------------
if t==2    

    lat_m_rt=[];
    a = 1;
    b = 1.175;
    datos = (b-a).*rand(1,300) + a;
    lat_m_rt = [lat_m_rt datos];

    a = 1.175;
    b = 1.575;
    datos = (b-a).*rand(1,1050) + a;
    lat_m_rt = [lat_m_rt datos];

    a = 1.575;
    b = 2.723;
    datos = (b-a).*rand(1,1240) + a;
    lat_m_rt = [lat_m_rt datos];

    a = 2.723;
    b = 3.865;
    datos = (b-a).*rand(1,210) + a;
    lat_m_rt = [lat_m_rt datos];

    a = 3.865;
    b = 4.975;
    datos = (b-a).*rand(1,100) + a;
    lat_m_rt = [lat_m_rt datos];
    
    
    
    lat_c_rt=[];
    a = 2.156;
    b = 2.275;
    datos = (b-a).*rand(1,100) + a;
    lat_c_rt = [lat_c_rt datos];

    a = 2.275;
    b = 3.475;
    datos = (b-a).*rand(1,650) + a;
    lat_c_rt = [lat_c_rt datos];

    a = 3.475;
    b = 4.523;
    datos = (b-a).*rand(1,1640) + a;
    lat_c_rt = [lat_c_rt datos];

    a = 4.523;
    b = 5.665;
    datos = (b-a).*rand(1,410) + a;
    lat_c_rt = [lat_c_rt datos];

    a = 5.665;
    b = 6.256;
    datos = (b-a).*rand(1,200) + a;
    lat_c_rt = [lat_c_rt datos]; 



    lat_a_rt=[];
    a = 0.276;
    b = 0.475;
    datos = (b-a).*rand(1,100) + a;
    lat_a_rt = [lat_a_rt datos];

    a = 0.475;
    b = 1.575;
    datos = (b-a).*rand(1,650) + a;
    lat_a_rt = [lat_a_rt datos];

    a = 1.575;
    b = 2.723;
    datos = (b-a).*rand(1,1440) + a;
    lat_a_rt = [lat_a_rt datos];

    a = 2.723;
    b = 3.765;
    datos = (b-a).*rand(1,710) + a;
    lat_a_rt = [lat_a_rt datos];

    a = 3.765;
    b = 4.175;
    datos = (b-a).*rand(1,100) + a;
    lat_a_rt = [lat_a_rt datos];

    
end

histogram(lat_a_rt)
title('actuacion')
figure
histogram(lat_c_rt)
title('control')
figure
histogram(lat_m_rt)
title('medicion')


%----------datos rt--------------

save('lat_m_rt','lat_m_rt')
save('lat_c_slave_rt','lat_c_rt')
save('lat_a_slave_rt','lat_a_rt')



% %-----------datos singularity---------------
% if t == 2
%     a = 0.623;
%     b = 0.752;
%     lat1_cm = normrnd(0.7,0.02,1, 3000);%(b-a).*rand(1,3000) + a;
%     a = 0.675;
%     b = 0.683;%+0.375;
%     lat_m_rt=normrnd(0.64,0.015,1, 3000);%(b-a).*rand(1,3000) + a;
%     a = 0.6;%+0.375;
%     b = 0.614;%+0.375+0.6;
%     lat3_cm= normrnd(0.68,0.06,1, 3000);%(b-a).*rand(1,3000) + a;
% 
%     a = 0.6;
%     b = 0.637;
%     lat1_cs = normrnd(0.7,0.07,1, 3000);%(b-a).*rand(1,3000) + a;
%     a = 0.45;
%     b = 0.58;%156+0.1;
%     lat_c_rt=normrnd(0.68,0.01,1, 3000);% (b-a).*rand(1,3000) + a;
%     a = 0.6;
%     b = 0.621;
%     lat3_cs=normrnd(0.69,0.04,1, 3000);% (b-a).*rand(1,3000) + a;
% 
%     a = 0.6;
%     b = 0.612;
%     lat1_ps = normrnd(0.69,0.02,1, 3000);%(b-a).*rand(1,3000) + a;
%     a = 0.276;
%     b = 0.476;%+0.1;
%     lat_a_rt=normrnd(0.48,0.02,1, 3000);% (b-a).*rand(1,3000) + a;
%     a = 0.6;
%     b = 0.673;
%     lat3_ps= normrnd(0.67,0.03,1, 3000);%(b-a).*rand(1,3000) + a;
% 
% end
% 
% if t == 1
%     
%     lat1_cm = normrnd(0.9,0.02,1, 3000);%(b-a).*rand(1,3000) + a;
%     
%     lat_m_rt=normrnd(1.24,0.015,1, 3000);%(b-a).*rand(1,3000) + a;
%     
%     lat3_cm= normrnd(1.68,0.06,1, 3000);%(b-a).*rand(1,3000) + a;
% 
%    
%     lat1_cs = normrnd(0.6,0.07,1, 3000);%(b-a).*rand(1,3000) + a;
%    
%     lat_c_rt=normrnd(0.78,0.01,1, 3000);% (b-a).*rand(1,3000) + a;
%     
%     lat3_cs=normrnd(1,0.04,1, 3000);% (b-a).*rand(1,3000) + a;
% 
%    
%     lat1_ps = normrnd(0.8,0.02,1, 3000);%(b-a).*rand(1,3000) + a;
%  
%     lat_a_rt=normrnd(1,0.02,1, 3000);% (b-a).*rand(1,3000) + a;
%   
%     lat3_ps= normrnd(1.15,0.03,1, 3000);%(b-a).*rand(1,3000) + a;
%     
% %     lat1_cm = normrnd(0.9,0.02,1, 3000);%(b-a).*rand(1,3000) + a;
% %     
% %     lat_m_rt=normrnd(1.24,0.015,1, 3000);%(b-a).*rand(1,3000) + a;
% %     
% %     lat3_cm= normrnd(1.68,0.06,1, 3000);%(b-a).*rand(1,3000) + a;
% % 
% %    
% %     lat1_cs = normrnd(0.6,0.07,1, 3000);%(b-a).*rand(1,3000) + a;
% %    
% %     lat_c_rt=normrnd(0.78,0.01,1, 3000);% (b-a).*rand(1,3000) + a;
% %     
% %     lat3_cs=normrnd(1,0.04,1, 3000);% (b-a).*rand(1,3000) + a;
% % 
% %    
% %     lat1_ps = normrnd(0.8,0.02,1, 3000);%(b-a).*rand(1,3000) + a;
% %  
% %     lat_a_rt=normrnd(1,0.02,1, 3000);% (b-a).*rand(1,3000) + a;
% %   
% %     lat3_ps= normrnd(1.15,0.03,1, 3000);%(b-a).*rand(1,3000) + a;
% 
% end
% save('lat_t1_cm_rt','lat1_cm')
% save('lat_t1_control_slave_rt','lat1_cs')
% save('lat_t1_proceso_slave_rt','lat1_ps')
% 
% 
% save('lat_m_rt','lat_m_rt')
% save('lat_control_slave_rt','lat_c_rt')
% save('lat_proceso_slave_rt','lat_a_rt')
% 
% save('lat_t3_cm_rt','lat3_cm')
% save('lat_t3_control_slave_rt','lat3_cs')
% save('lat_t3_proceso_slave_rt','lat3_ps')
