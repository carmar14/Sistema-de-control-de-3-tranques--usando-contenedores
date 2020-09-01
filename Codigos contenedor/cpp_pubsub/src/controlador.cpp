// Copyright 2016 Open Source Robotics Foundation, Inc.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#include <chrono>
//#include <functional>
#include <memory>
//#include <string>

#include "rclcpp/rclcpp.hpp"
//#include "std_msgs/msg/string.hpp"

#include "tutorial_interfaces/msg/num.hpp"     // CHANGE
#include "tutorial_interfaces/msg/proceso.hpp"     // CHANGE
#include "tutorial_interfaces/msg/control.hpp"     // CHANGE


using namespace std::chrono_literals;

/* This example creates a subclass of Node and uses std::bind() to register a
 * member function as a callback from the timer. */

//--------------------------Variables para controlador--------------------
//-----Ganancia del proporcional
double k11=0.0216;
double k12=0.003;
double k13=-0.005;
double k21=0.0029;
double k22=0.019;
double k23=-0.004;

//------Ganancia del integrador
double ki11=-0.001*0.95;
double ki12=-0.001*0.32;
double ki21=-0.001*0.3;
double ki22=-0.001*0.91;

//--------------------------

double e1;
double e2;
double q1;
double q2;

double ai1;
double ai2;
double ai1k;
double ai2k;

double ui1;
double ui2;

double up1;
double up2;


double x1;
double x2;
double x3;

double t=0.0;

//--------------------------------------Subscriber(envio de datos)-------------------------------

using std::placeholders::_1;

class MinimalSubscriber : public rclcpp::Node
{
public:
  MinimalSubscriber()
  : Node("minimal_subscriber")
  {

   //-----------------------Control-------------------------
    subscription_c = this->create_subscription<tutorial_interfaces::msg::Control>(          // CHANGE    
    "topic", 10, std::bind(&MinimalSubscriber::get_control, this, _1));
    //-----------------------Control-------------------------

   
    //----------------------Proceso--------------------
    
    subscription_p = this->create_subscription<tutorial_interfaces::msg::Proceso>(          // CHANGE    
     "topic", 10, std::bind(&MinimalSubscriber::get_proceso, this, _1));

    //----------------------Proceso--------------------

  }

private:

 //------------------Callback del control------------------------- 

  //void topic_callback(const std_msgs::msg::String::SharedPtr msg) const
    void get_control(const tutorial_interfaces::msg::Control::SharedPtr msg) const       // CHANGE
  {
    //RCLCPP_INFO(this->get_logger(), "I heard: '%s'", msg->data.c_str());
   RCLCPP_INFO(this->get_logger(), "x1: '%d'", msg->x1);
   RCLCPP_INFO(this->get_logger(), "x2: '%d'", msg->x2);
   RCLCPP_INFO(this->get_logger(), "x3: '%d'", msg->x3);
   
  
  }

  


   //---------------------Callback del proceso---------------------------------
 void get_proceso(const tutorial_interfaces::msg::Proceso::SharedPtr msg) const       // CHANGE
  {
    //RCLCPP_INFO(this->get_logger(), "I heard: '%s'", msg->data.c_str());
  // RCLCPP_INFO(this->get_logger(), "x1 proceso: '%d'", msg->x1);
  // RCLCPP_INFO(this->get_logger(), "x2 proceso: '%d'", msg->x3);
  // RCLCPP_INFO(this->get_logger(), "x3 proceso: '%d'", msg->u1);
   RCLCPP_INFO(this->get_logger(), "u1: '%d'", msg->u1);
   RCLCPP_INFO(this->get_logger(), "u2: '%d'", msg->u2);
  // RCLCPP_INFO(this->get_logger(), "u1 proceso: '%d'", msg->u1);



  }

  //rclcpp::Subscription<std_msgs::msg::String>::SharedPtr subscription_;
  //---------------------------Control------------------
  rclcpp::Subscription<tutorial_interfaces::msg::Control>::SharedPtr subscription_c;       // CHANGE
  
  //-------------------------Proceso-----------------------
  rclcpp::Subscription<tutorial_interfaces::msg::Proceso>::SharedPtr subscription_p;       // CHANGE

};

//--------------------------------------Subscriber-------------------------------






//----------------------------------Publisher------------------------------------

class MinimalPublisher : public rclcpp::Node
{
public:
  MinimalPublisher()
  : Node("minimal_publisher"), count_(0)
  {
   // publisher_ = this->create_publisher<std_msgs::msg::String>("topic", 10);
     
//-----------------------Control-------------------------
    subscription_c = this->create_subscription<tutorial_interfaces::msg::Control>(          // CHANGE    
    "topic", 10, std::bind(&MinimalPublisher::get_control, this, _1));
    //-----------------------Control-------------------------

    //------------------------------------------Control----------------------------
    publisher_c = this->create_publisher<tutorial_interfaces::msg::Proceso>("topic", 10);    // CHANGE
   
    //------------------------------------------Proceso--------------------------
    //publisher_p = this->create_publisher<tutorial_interfaces::msg::Control>("topic", 10); 
   
    timer_ = this->create_wall_timer(
      1000ms, std::bind(&MinimalPublisher::timer_callback, this));
  }

private:
  void timer_callback()
  {
//    auto message_p = tutorial_interfaces::msg::Control();//Num();  // std_msgs::msg::String();
   
    auto message_c = tutorial_interfaces::msg::Proceso();   
    
 //message.data = "Hello, world! " + std::to_string(count_++);
  
    if (t<=250){
    	q1=0.4;
    }

    if (t>250 && t<=1500){
        q1=0.45;
    }
   
    if (t>1500 && t<=2500 ){
        q1=0.4;
    }
    if (t>2500){
        q1=0.45;
    }

    if (t<=400){
        q2=0.2;
    }

    if (t>400 && t<=2000){
        q2=0.225;
    }
   
    if (t>2000){
        q2=0.2;
    }
   
    if  (t>3000){
    	t=0.0;
    }

   t=t+1.0;

   //---------------Proceso-------------
  /* 
    x1=message_p.x1;//10000.0;//this->count_++;
    x2=message_p.x2/10000.0;//=220;
    x3=message_p.x3/10000.0;//=330;
    */
   //------Calculo el error----------------
    e1=q1-x1;
    e2=q2-x2;
   
    //------------Calculo las acciones de control u1 y u2
    ai1=e1+ai1k;
    ai2=e2+ai2k;
    ai1k=ai1;
    ai2k=ai2;
    ui1=ki11*ai1+ki12*ai2;
    ui2=ki21*ai1+ki22*ai2;
    ui1=-ui1;
    ui2=-ui2;
    up1=k11*x1+k12*x2+k13*x3;
    up2=k21*x1+k22*x2+k23*x3;
    up1=-up1;
    up2=-up2;
    
   // int u1=(ui1+up1)*100000;

    //-----------------Control--------------------
    message_c.u1=(ui1+up1)*10000;    
    message_c.u2=(ui2+up2)*10000;
   
    if (message_c.u1>15) message_c.u1=15;
    if (message_c.u2>15) message_c.u2=15;    

    if (message_c.u1<0) message_c.u1=0;    
    if (message_c.u2<0) message_c.u2=0;    

    

       
    //RCLCPP_INFO(this->get_logger(), "Publishing: '%s'", message.data.c_str());
  
    //---------------------Control------------
    RCLCPP_INFO(this->get_logger(), "tiempo: '%3.2f'", t); 


    RCLCPP_INFO(this->get_logger(), "la accion u1: '%d'", message_c.u1); 
    publisher_c->publish(message_c);

    RCLCPP_INFO(this->get_logger(), "la accion u2: '%d'", message_c.u2); 
    publisher_c->publish(message_c);



   RCLCPP_INFO(this->get_logger(), "x1: '%3.4f'", x1); 
   RCLCPP_INFO(this->get_logger(), "x2: '%3.4f'", x2); 
   RCLCPP_INFO(this->get_logger(), "x3: '%3.4f'", x3); 




    //---------------Proceso----------------
   /*      
    RCLCPP_INFO(this->get_logger(), "la salida x1: '%d'", message_p.x1); 
    publisher_p->publish(message_p);
    
    RCLCPP_INFO(this->get_logger(), "la salida x2: '%d'", message_p.x2); 
    publisher_p->publish(message_p);

    RCLCPP_INFO(this->get_logger(), "la salida x3: '%d'", message_p.x3); 
    publisher_p->publish(message_p);
   
    */
 
  }


  //------------------Callback del control------------------------- 

  //void topic_callback(const std_msgs::msg::String::SharedPtr msg) const
    void get_control(const tutorial_interfaces::msg::Control::SharedPtr msg) const       // CHANGE
  {
    //RCLCPP_INFO(this->get_logger(), "I heard: '%s'", msg->data.c_str());
 
   x1=msg->x1;
   x1=x1/10000.0;
   x2=msg->x2;
   x2=x2/10000.0;
   x3=msg->x3;
   x3=x3/10000.0;

  // RCLCPP_INFO(this->get_logger(), "x1: '%d'", msg->x1);
  // RCLCPP_INFO(this->get_logger(), "x2: '%d'", msg->x2);
  // RCLCPP_INFO(this->get_logger(), "x3: '%d'", msg->x3);
   
  
  }

  
//---------------------------Control------------------
  rclcpp::Subscription<tutorial_interfaces::msg::Control>::SharedPtr subscription_c;       // CHANGE
  


  rclcpp::TimerBase::SharedPtr timer_;  
 
  //---------------------Control----------------
  rclcpp::Publisher<tutorial_interfaces::msg::Proceso>::SharedPtr publisher_c;         // CHANGE//rclcpp::Publisher<std_msgs::msg::String>::SharedPtr publisher_;
 //---------------------Proceso----------------- 
  //rclcpp::Publisher<tutorial_interfaces::msg::Control>::SharedPtr publisher_p; 

  size_t count_;
};


//----------------------------------Publisher------------------------------------


int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  
  rclcpp::spin(std::make_shared<MinimalPublisher>());
//  rclcpp::spin(std::make_shared<MinimalSubscriber>());
  rclcpp::shutdown();
  return 0;
}
