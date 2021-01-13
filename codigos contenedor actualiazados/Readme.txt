///////////////////////////////////////////////////////////////////////////////
//      Title     : Readme.txt
//      Project   : control (petri - tanques)
//      Created   : Junio/8/2020
//      Author    : Apolinar González Potes
//
//      Producto desarrollado para Punta Delicia
//
//
///////////////////////////////////////////////////////////////////////////////

1. Introducción

Este documento es una base para el desarrollo de la plataforma que se instala en la planta
Punta Delicia, Colima, México.
La plataforma se basa en DDS (Data Distribution Service) y con el soporte básico de ROS2 en su versión
de Foxy, adicional a esto estamos usando lxc/lxd como contenedores para facilitar el proceso de 
desarrollo y mantenimiento.
LXC/LXD son una alternativa a Docker, que en mi opinión facilita el desarrollo con soporte Linux completo,
lo cual lo hace más fácil. Docker es una buena solución también, sin embargo el proceso de capas de actualización
hace que los contendores crezcan mucho y se facilitan bien cuando es una sola aplicación, pero en nuestro caso
es muy posible ejecutar muchos programas en un mismo contenedor. Para mi, la mejor solución seria "snapcraft", 
los snap son una forma de empaquetar las aplicaciones muy buena, elegante y fácil de instalar y administrar, 
sin embargo, dado que es un proceso nuevo y que tiene reciente soporte con ROS2, creo que es una solución a futuro. 
Usar snap con ubuntu core en mi opinión seria lo mejor a usar en las próximas versiones.

2. Instalación de LXC/LXD (listo)

LXC es el contenedor maduro de linux y LXD es un manejador. 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Instalación
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
> sudo snap install lxd   %% desde snap
> id -u apogon            %% Saber ID de mi usuario   apogon= nombre de usuario
> id -g apogon            %% Saber el GID
> sudo usermod -a -G lxd apogon    %% Para ejecutar lxd sin usar sudo newgrp lxd                       %% Validar la acción anterios
> lxd init                         %% Configurar un lxc

Una vez que se ejecuta el "lxd init" todos los valores que uso son por defecto, solamente asegurarse de 
ASIGNAR el bridge lxdbr0, en todas las ocasiones que lo usé, siempre salió por defecto, pero "creo" que una vez me propuso otra cosa.

2.1 Comandos básicos LXC/LXD

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Comandos
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
lxc launch ubuntu:20.04 foxy                               %% Crear un contenedor de nombre dashing
lxc launch ubuntu:20.04 foxy -c security.privileged=true   %%% OJO FORMA PARA TENER PRIVILEGIOS foxy=nombre del contenedor
lxc exec foxy bash                                         %% Entrar a dashing(nombre de contenedor) user root
lxc exec foxy -- sudo -iu ubuntu bash                      %% Entrar a dashing user:ubuntu /home/ubuntu
exit    					             %% Salir de contenedor

En realidad estamos trabajanod con Ubuntu Minimal en su versión 20.04 por lo que hay que activar el repositorio de descarga con la siguiente linea:

lxc remote add --protocol simplestreams ubuntu-minimal https://cloud-images.ubuntu.com/minimal/releases/

Después de eso se debe hacer:

lxc launch ubuntu-minimal:20.04 foxy
						    

2.2 Compartir carpetas host y contenedor (falta todo)

Una manera de trabajar fácilmente entre el host con todos sus servicios como editores, manejador de archivos, terminales, red, etc es compartir los datos a través de una carpeta compartida: 						     

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Crear un directorio compartido host ~/ros2_dev/foxy - > contenedor /home/ubuntu/foxy_dev
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

lxc config device add dashing share disk source=~/ros2_dev/foxy path=/home/ubuntu/foxy_dev
lxc config set dashing raw.idmap "both 1000 1001"   %% Para realmente compartir el acceso


Esta forma de compartir las carpetas entre host y contendor es muy fácil, sin embargo hemos observado que para las funciones posteriores es un lio, me refiero a copiar los contendores o para hacer backups de ellos o transferirilos a otras partes o otras computadoras. Otra forma de hacer esto y evitar el problema anterior es hacer lo siguiente:

#####################################################################
## Ruta a los contenedores
## Solo funciona como root
#####################################################################
root@apogon:/var/snap/lxd/common/mntns/var/snap/lxd/common/lxd/storage-pools/default/containers#

Esta ruta es donde están almacenada la información de los contenedores o los archivos, se pueden modificar directamente desde ahí, es decir, se pueden editar, copiar, etc, lo que hace que se pueda trabajar directamente desde el host de una manera muy fácil.
Para visualizar se puede ejecutar nautilus ditectamente en esa ruta como root (claro en ubuntu).
ejemplo: 

root@apogon:/var/snap/lxd/common/mntns/var/snap/lxd/common/lxd/storage-pools/default/containers#nautilus .

2.3 Imagenes del contenedor (informacion general para back up) (listo la primera parte hasta el comando linea 98)

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Construir una imagen base
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

lxc stop micontenedor
lxc publish micontenedor --alias mi-backup
lxc launch mi-backup prueba                      %% Se construye una nueva imagen desde milxd-backup
lxc exec prueba bash
lxc list

lxc image export milxd-backup /tmp/milxdbkp         %% Se crea un /tmp/milxdbkp.tar.gz archivo que se puede copiar
lxc delete milxd-backup                             %%  Para eliminar el backup

lxc image import /tmp/milxdbkp.tar.gz --alias newmixld-backup
lxc image delete milxd-backup

2.4 Contenedores remotos

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
MANEJO REMOTO DE CONTENEDORES
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%% En el host remoto: %%%%%%%%%%%%%%%%%%%

$ lxc config set core.https_address "[::]:8443"
# ---------------------
# configurar una contraseña
# ---------------------
$ lxc config set core.trust_password rtlinux

%%%%%%%%% En el host local: %%%%%%%%%%%%%%%%%%%%
lxc remote add host1 IP :8443

%%%%%%%%% Para copiar VM %%%%%%%%%%%%%%%%%%%%%%%
lxc copy host1:ros-1 c1  %%% Copia desde el host1 al local 
                         %%% Todavía no sé como copiar en otro sentido
                         %%% La idea por ahora es con ssh login y después copiar 
                         %%% OJO para copiar se debe tener en stop la VM
                         %%% de lo contario se puede con snaphot (ver)


###############################################################

2.5 Segmento de red en contenedores

ASIGNAR SEGMENTO DE RED al bridge lxdbr0

lxc network show lxdbr0
EDITOR=nano lxc network edit lxdbr0    %%% Cambiar la dirección

%%%%%%%%%   Después de eso ya se puede asignar una dirección dentro del segmento

$ lxc stop micontendor
$ lxc network attach lxdbr0 micontendor eth0 eth0
$ lxc config device set micontendor eth0 ipv4.address 10.99.10.42
$ lxc start micontenedor

3. Instalar ROS2 foxy en contendores (listo)

La imagen que tenemos instalada es la versión ubuntu-minimal 20.04, ROS2 foxy es para trabajar sobre ubuntu 20.04. 
%%%% Ingresar a lxc %%%%%
lxc exec foxy -- sudo -iu ubuntu bash

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
INSTALACIÓN DE foxy ros2-foxy-base
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

sudo apt update && sudo apt install curl gnupg2 lsb-release
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -

sudo sh -c 'echo "deb http://packages.ros.org/ros2/ubuntu `lsb_release -cs` main" > /etc/apt/sources.list.d/ros2-latest.list'

sudo apt update

sudo apt install ros-foxy-ros-base
sudo apt install python3-colcon-common-extensions

sudo apt-get install g++  					%%%% foxy-ros-base instala el g++ 

Ya se debe tener una instalación base de foxy. La base generalmente no incluye nada de ejemplos ni otras utilerías que son más del uso en robótica, nuestro interés no es robótica por ahora, así que tenemos una versión con DDS Fast-RTPS de EPROSIMA y las herramientas de compilación.

Hay varios ejemplos que se pueden seguir en los tutoriales de ROS2 para familiarizarce

4. Contenedores con peervpn

La idea es tener los ocntendores en un propio segmento de red, sin embargo hay que proporcionar la opción de MULTICAST para el funcionamiento de ROS2 debido al Fast-RTPS, es una necesidad de funcionamiento del DDS. Hay varias formas de hacer esto, sin embargo cuando se quiere interactuar de manera inalámbrica las cosas se complican un poco, los routers y Access Point en general no asignan direcciones o IP's a los contenedores, eso es una historia de verificación de la MAC ADDRESS y hay muchos documentos al respecto. Nosotros decidimos hacer una peervpn que enlace los contenedores y sin que se asignen las IP's por DHCP, así que implementamos la opción peervpn que permite una vpn enlazada entre los host de acuerdo a la configuración que uno desee, es decir puede usarce sin centralización.  

%%%%%
Pasos
%%%%%
Configurar que los lxc estén en el mismo segmento de red

lxc network show lxdbr0
EDITOR=nano lxc network edit lxdbr0    		       %%% Cambiar la dirección

%%%%%%%%%   Después de eso ya se puede asignar una dirección dentro del segmento

$ lxc stop ros2-1                                            %%%% ros2-1 máquina virtual
$ lxc network attach lxdbr0 ros2-1 eth0 eth0  
$ lxc config device set ros2-1 eth0 ipv4.address 10.1.1.10   %%%% IP asignada 
$ lxc start ros2-1                                           %%%% Estos pasos se hacen una vez

$ lxc network detach lxdbr0 ros-1 eth0                       %%%% en caso de que se quiera quitar la asignación 
                                                             %%%% lxdbr0 -> eth0

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
peerVPN
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%host 1  (peervpn.conf)
port 7000
networkname lxdnet
psk random-secret-value
enabletunneling yes
interface peervpn0
ifconfig4 10.1.1.1/24          /// Direcciones de los containers ( en este caso tengo dos en este host)
initpeers 192.168.2.103 7000    /// aquí va la dirección del host con el que se quiere enlazar
                                

                                
$ sudo ./peervpn peervpn.conf
$ sudo ip link set dev peervpn0 master lxdbr0  %%% En ese orden
                                
%%%%host 2  (peervpn.conf)
port 7000
networkname lxdnet
psk random-secret-value
enabletunneling yes
interface peervpn0
ifconfig4 10.1.1.20/24          /// Direcciones de los containers 
initpeers 192.168.2.83 7000    /// aquí va la dirección del host con el que se quiere enlazar
                                /// Tengo que probar cuando se quiera enlazar con más de uno (creo es posible)
%% probar OJO %%%%
initpeers 192.168.2.83 7000 192.168.2.X 7000  /// Caundo se quieran enlazar más peers 

$ sudo ./peervpn peervpn.conf
$ sudo ip link set dev peervpn0 master lxdbr0  %%% En ese orden

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

5. Cración de mensajes ROS2 para tópicos propios  (listo)

Todo esto se hace dentro del contendor con ROS2.

#https://index.ros.org/doc/ros2/Tutorials/Custom-ROS2-Interfaces/
mkdir -p ws/src
cd ws/src
source /opt/ros/foxy/setup.bash
ros2 pkg create --build-type ament_cmake my_messages_ros

cd my_messages_ros
mkdir msg
cd msg
A continuación se detallan los idl de los msg que usaremos  y de los diferentes tópicos que hemos definido para la aplicación

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
----Llenar.msg ----
string producto
int32 tanque
int32 linea
int32 columna
bool onoff
int32 estado

---Cipear.msg
int32 linea
int32 columna
int32 tanque
int32 otrotanque
int32 drenret
bool onoff
int32 estado

---Vaciar.msg
string producto
int32 tanque
int32 otrotanque
bool onoff
int32 estado

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%% En CMakeList.txt %%%
# find_package(<dependency> REQUIRED) /// Justo debajo de esta linea
                                      //  (linea no incluida)
find_package(rosidl_default_generators REQUIRED)

set(msg_files
  "msg/Llenar.msg"
  "msg/Cipear.msg"
  "msg/Vaciar.msg"
)

rosidl_generate_interfaces(${PROJECT_NAME}
  ${msg_files}
)
ament_export_dependencies(rosidl_default_runtime)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%% en package.xml %%%

  //// <buildtool_depend>ament_cmake</buildtool_depend> /// después de 
                                                        /// esta linea
  
  <buildtool_depend>rosidl_default_generators</buildtool_depend>
  <exec_depend>rosidl_default_runtime</exec_depend>
  <member_of_group>rosidl_interface_packages</member_of_group>

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%% Desde ws %%%
$colcon build --symlink-install --packages-select my_messages
$ . install/setup.bash
$ ros2 interface list
$ ros2 interface list | grep my_messages

Hasta aquí se tienen los contendores preparados para realizar las aplicaciones. Mi sugerencia hasta aquí, es hacer un backup de foxy-ros2 y colocarlo con imagen base, así cada vez que se necesita un contenedor con todo esto ya instalado, sinplemente se hace el launch del nuevo contedor y se pueden generar muchas copias cada vez que se necesite.


6. Instalación de ROS2 Bridge para javascript (listo)

En un contendor con todo la instalación de ros2-foxy e incluido los mensajes o tópicos propios a usar, se puede instalar el ros2 bridge cuando se uqieran tener opciones de uso de javascript.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Instalación
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
sudo apt-get update
sudo apt-get install gcc

sudo apt update && sudo apt install curl gnupg2 lsb-release
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
sudo sh -c 'echo "deb [arch=$(dpkg --print-architecture)] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" > /etc/apt/sources.list.d/ros2-latest.list'

sudo apt update

sudo apt install ros-foxy-ros-base
sudo apt install npm
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | bash
nvm install 12.18.1
nvm use 12.18.1
nvm use 12.18.1
sudo apt-get install git
git clone https://github.com/RobotWebTools/ros2-web-bridge.git
cd ros2-web-bridge
sudo nano package.json
"rclnodejs": "0.14.1",
source /opt/ros/foxy/setup.bash
npm install
node bin/rosbridge.js

#https://github.com/RobotWebTools/ros2-web-bridge/issues/110  10.118.215.149


PARA EL DESARROLLO DE LAS APLICACIONES NOS PONEMOS DE ACUERDO PARA PASARTE LOS ARCHIVOS Y MOSTRARTE COMO FUNCIONAN. Por ahora pueden ir instlando todo esto, que es un trabajo de vario tiempo que se encuentra aquí condensado.



