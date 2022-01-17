clc
clear
close all

t=1;
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
    datos = (b-a).*rand(1,310) + a;
    lat_m_rt = [lat_m_rt datos];

    a = 3.865;
    b = 4.975;
    datos = (b-a).*rand(1,100) + a;
    lat_m_rt = [lat_m_rt datos];
    
    
    
    lat_c_rt=[];
    a = 2.156;
    b = 2.275;
    datos = (b-a).*rand(1,500) + a;
    lat_c_rt = [lat_c_rt datos];

    a = 2.275;
    b = 3.475;
    datos = (b-a).*rand(1,950) + a;
    lat_c_rt = [lat_c_rt datos];

    a = 3.475;
    b = 4.523;
    datos = (b-a).*rand(1,1140) + a;
    lat_c_rt = [lat_c_rt datos];

    a = 4.523;
    b = 5.665;
    datos = (b-a).*rand(1,310) + a;
    lat_c_rt = [lat_c_rt datos];

    a = 5.665;
    b = 6.256;
    datos = (b-a).*rand(1,100) + a;
    lat_c_rt = [lat_c_rt datos]; 



    lat_a_rt=[];
    a = 0.276;
    b = 0.475;
    datos = (b-a).*rand(1,400) + a;
    lat_a_rt = [lat_a_rt datos];

    a = 0.475;
    b = 1.575;
    datos = (b-a).*rand(1,1050) + a;
    lat_a_rt = [lat_a_rt datos];

    a = 1.575;
    b = 2.723;
    datos = (b-a).*rand(1,1140) + a;
    lat_a_rt = [lat_a_rt datos];

    a = 2.723;
    b = 3.765;
    datos = (b-a).*rand(1,310) + a;
    lat_a_rt = [lat_a_rt datos];

    a = 3.765;
    b = 4.175;
    datos = (b-a).*rand(1,100) + a;
    lat_a_rt = [lat_a_rt datos];

    
end



%----------datos rt--------------





% %-----------datos singularity---------------
if t == 2
    lat_m_=[];
    a = 1;
    b = 1.175;
    datos = (b-a).*rand(1,200) + a;
    lat_m_ = [lat_m_ datos];

    a = 1.175;
    b = 1.575;
    datos = (b-a).*rand(1,550) + a;
    lat_m_ = [lat_m_ datos];

    a = 1.575;
    b = 2.723;
    datos = (b-a).*rand(1,1040) + a;
    lat_m_ = [lat_m_ datos];
    

    a = 2.723;
    b = 3.865;
    datos = (b-a).*rand(1,910) + a;
    lat_m_ = [lat_m_ datos];

    a = 3.865;
    b = 4.975;
    datos = (b-a).*rand(1,300) + a;
    lat_m_ = [lat_m_ datos];
    
    
    
    lat_c_=[];
    a = 2.156;
    b = 2.275;
    datos = (b-a).*rand(1,100) + a;
    lat_c_ = [lat_c_ datos];

    a = 2.275;
    b = 3.475;
    datos = (b-a).*rand(1,950) + a;
    lat_c_ = [lat_c_ datos];

    a = 3.475;
    b = 4.523;
    datos = (b-a).*rand(1,1040) + a;
    lat_c_ = [lat_c_ datos];

    a = 4.523;
    b = 5.665;
    datos = (b-a).*rand(1,610) + a;
    lat_c_ = [lat_c_ datos];

    a = 5.665;
    b = 6.256;
    datos = (b-a).*rand(1,300) + a;
    lat_c_ = [lat_c_ datos]; 



    lat_a_=[];
    a = 0.276;
    b = 0.475;
    datos = (b-a).*rand(1,200) + a;
    lat_a_ = [lat_a_ datos];

    a = 0.475;
    b = 1.575;
    datos = (b-a).*rand(1,950) + a;
    lat_a_ = [lat_a_ datos];

    a = 1.575;
    b = 2.723;
    datos = (b-a).*rand(1,1040) + a;
    lat_a_ = [lat_a_ datos];

    a = 2.723;
    b = 3.765;
    datos = (b-a).*rand(1,610) + a;
    lat_a_ = [lat_a_ datos];

    a = 3.765;
    b = 4.175;
    datos = (b-a).*rand(1,200) + a;
    lat_a_ = [lat_a_ datos];

end

% histogram(lat_a_rt)
% hold on
% histogram(lat_a_)
% title('actuacion')
% figure
% histogram(lat_c_rt)
% hold on
% histogram(lat_c_)
% title('control')
% figure
% histogram(lat_m_rt)
% hold on
% histogram(lat_m_)
% title('medicion')
% 
% save('lat_m_rt','lat_m_rt')
% save('lat_c_rt','lat_c_rt')
% save('lat_a_rt','lat_a_rt')
% 
% save('lat_m_','lat_m_')
% save('lat_c_','lat_c_')
% save('lat_a_','lat_a_')

%----------datos rt--------------
if t==1    

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
    datos = (b-a).*rand(1,310) + a;
    lat_m_rt = [lat_m_rt datos];

    a = 3.865;
    b = 4.975;
    datos = (b-a).*rand(1,100) + a;
    lat_m_rt = [lat_m_rt datos];
    
    
    
    lat_c_rt=[];
    a = 2.156;
    b = 2.275;
    datos = (b-a).*rand(1,500) + a;
    lat_c_rt = [lat_c_rt datos];

    a = 2.275;
    b = 3.475;
    datos = (b-a).*rand(1,950) + a;
    lat_c_rt = [lat_c_rt datos];

    a = 3.475;
    b = 4.523;
    datos = (b-a).*rand(1,1140) + a;
    lat_c_rt = [lat_c_rt datos];

    a = 4.523;
    b = 5.665;
    datos = (b-a).*rand(1,310) + a;
    lat_c_rt = [lat_c_rt datos];

    a = 5.665;
    b = 6.256;
    datos = (b-a).*rand(1,100) + a;
    lat_c_rt = [lat_c_rt datos]; 



    lat_a_rt=[];
    a = 0.276;
    b = 0.475;
    datos = (b-a).*rand(1,400) + a;
    lat_a_rt = [lat_a_rt datos];

    a = 0.475;
    b = 1.575;
    datos = (b-a).*rand(1,1050) + a;
    lat_a_rt = [lat_a_rt datos];

    a = 1.575;
    b = 2.723;
    datos = (b-a).*rand(1,1140) + a;
    lat_a_rt = [lat_a_rt datos];

    a = 2.723;
    b = 3.765;
    datos = (b-a).*rand(1,310) + a;
    lat_a_rt = [lat_a_rt datos];

    a = 3.765;
    b = 4.175;
    datos = (b-a).*rand(1,100) + a;
    lat_a_rt = [lat_a_rt datos];

    
end



%----------datos rt--------------





% %-----------datos singularity---------------
if t == 1
    lat_m_=[];
    a = 1;
    b = 1.275;
    datos = (b-a).*rand(1,200) + a;
    lat_m_ = [lat_m_ datos];

    a = 1.275;
    b = 1.675;
    datos = (b-a).*rand(1,550) + a;
    lat_m_ = [lat_m_ datos];

    a = 1.675;
    b = 2.923;
    datos = (b-a).*rand(1,1040) + a;
    lat_m_ = [lat_m_ datos];
    

    a = 2.923;
    b = 3.965;
    datos = (b-a).*rand(1,910) + a;
    lat_m_ = [lat_m_ datos];

    a = 3.965;
    b = 5.975;
    datos = (b-a).*rand(1,300) + a;
    lat_m_ = [lat_m_ datos];
    
    
    
    lat_c_=[];
    a = 2.156;
    b = 2.575;
    datos = (b-a).*rand(1,100) + a;
    lat_c_ = [lat_c_ datos];

    a = 2.575;
    b = 3.875;
    datos = (b-a).*rand(1,950) + a;
    lat_c_ = [lat_c_ datos];

    a = 3.875;
    b = 4.823;
    datos = (b-a).*rand(1,1040) + a;
    lat_c_ = [lat_c_ datos];

    a = 4.823;
    b = 5.965;
    datos = (b-a).*rand(1,610) + a;
    lat_c_ = [lat_c_ datos];

    a = 5.965;
    b = 8.256;
    datos = (b-a).*rand(1,300) + a;
    lat_c_ = [lat_c_ datos]; 



    lat_a_=[];
    a = 0.276;
    b = 0.575;
    datos = (b-a).*rand(1,200) + a;
    lat_a_ = [lat_a_ datos];

    a = 0.575;
    b = 1.875;
    datos = (b-a).*rand(1,950) + a;
    lat_a_ = [lat_a_ datos];

    a = 1.875;
    b = 2.923;
    datos = (b-a).*rand(1,1040) + a;
    lat_a_ = [lat_a_ datos];

    a = 2.923;
    b = 3.965;
    datos = (b-a).*rand(1,610) + a;
    lat_a_ = [lat_a_ datos];

    a = 3.965;
    b = 6.675;
    datos = (b-a).*rand(1,200) + a;
    lat_a_ = [lat_a_ datos];

end

figure
histogram(lat_a_rt)
hold on
histogram(lat_a_)
title('actuacion')
figure
histogram(lat_c_rt)
hold on
histogram(lat_c_)
title('control')
figure
histogram(lat_m_rt)
hold on
histogram(lat_m_)
title('medicion')

save('lat_m_rt','lat_m_rt')
save('lat_c_rt','lat_c_rt')
save('lat_a_rt','lat_a_rt')

save('lat_m_','lat_m_')
save('lat_c_','lat_c_')
save('lat_a_','lat_a_')