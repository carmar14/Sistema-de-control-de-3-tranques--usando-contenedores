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

//-----------------------------Variables para el proceso---------------------------

double  u1;
double  u2;

double xk1;
double xk2;
double xk3;

double x1;
double x2;
double x3;



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
     
   
   //------------------------------------------Control----------------------------
   // publisher_c = this->create_publisher<tutorial_interfaces::msg::Proceso>("topic", 10);    // CHANGE
   //------------------------------------------Proceso--------------------------
    publisher_p = this->create_publisher<tutorial_interfaces::msg::Control>("topic", 10); 

   //----------------------Proceso--------------------
    subscription_p = this->create_subscription<tutorial_interfaces::msg::Proceso>(          // CHANGE    
     "topic", 10, std::bind(&MinimalPublisher::get_proceso, this, _1));

  
    timer_ = this->create_wall_timer(
      1000ms, std::bind(&MinimalPublisher::timer_callback, this));
  }

private:
  void timer_callback()
  {
    auto message_p = tutorial_interfaces::msg::Control();//Num();  // std_msgs::msg::String();
   
   // auto message_c = tutorial_interfaces::msg::Proceso();   

 //message.data = "Hello, world! " + std::to_string(count_++);
  
    //-----------------Control--------------------
    
 
    //u1=message_c.u1/10000;    
    //u2=message_c.u2/10000;    

    //---------------Proceso-------------
    xk1=0.9888*x1+0.0001*x2+0.0112*x3+64.5687*u1+0.0014*u2;
    xk2=0.0001*x1+0.9781*x2+0.0111*x3+0.0014*u1+64.2202*u2;
    xk3=0.0112*x1+0.0111*x2+0.9776*x3+0.3650*u1+0.3637*u2;
    
    x1=xk1;
    x2=xk2;
    x3=xk3;

    message_p.x1=xk1*10000;//xk1*10000;//this->count_++;
    message_p.x2=xk2*10000;
    message_p.x3=xk3*10000;
    //message_c.x1=110;message_p.x1;
    
    //RCLCPP_INFO(this->get_logger(), "Publishing: '%s'", message.data.c_str());
  
    //---------------------Control------------
   /* 
    RCLCPP_INFO(this->get_logger(), "la accion u1: '%d'", message_c.u1); 
    publisher_c->publish(message_c);

    RCLCPP_INFO(this->get_logger(), "la accion u2: '%d'", message_c.u2); 
    publisher_c->publish(message_c);
    */

    //---------------Proceso----------------
    

    RCLCPP_INFO(this->get_logger(), "u1: '%3.4f'", u1); 

    RCLCPP_INFO(this->get_logger(), "u2: '%3.4f'", u2); 


    RCLCPP_INFO(this->get_logger(), "la salida x1: '%d'", message_p.x1); 
    publisher_p->publish(message_p);
    /* */
    RCLCPP_INFO(this->get_logger(), "la salida x2: '%d'", message_p.x2); 
    publisher_p->publish(message_p);

    RCLCPP_INFO(this->get_logger(), "la salida x3: '%d'", message_p.x3); 
    publisher_p->publish(message_p);
   
    
 
  }



//---------------------Callback del proceso---------------------------------
 void get_proceso(const tutorial_interfaces::msg::Proceso::SharedPtr msg) const       // CHANGE
  {
    //RCLCPP_INFO(this->get_logger(), "I heard: '%s'", msg->data.c_str());
  // RCLCPP_INFO(this->get_logger(), "x1 proceso: '%d'", msg->x1);
  // RCLCPP_INFO(this->get_logger(), "x2 proceso: '%d'", msg->x3);
  // RCLCPP_INFO(this->get_logger(), "x3 proceso: '%d'", msg->u1);
   u1=msg->u1;
   u1=u1/10000.0;
   u2=msg->u2;
   u2=u2/10000.0;
//    RCLCPP_INFO(this->get_logger(), "u1: '%d'", u1);
  // RCLCPP_INFO(this->get_logger(), "u2: '%d'", u2);
  // RCLCPP_INFO(this->get_logger(), "u1 proceso: '%d'", msg->u1);



  } 
  
  //-------------------------Proceso-----------------------
  rclcpp::Subscription<tutorial_interfaces::msg::Proceso>::SharedPtr subscription_p;       // CHANGE



  rclcpp::TimerBase::SharedPtr timer_;  
 
  //---------------------Control----------------

// rclcpp::Publisher<tutorial_interfaces::msg::Proceso>::SharedPtr publisher_c;         // CHANGE//rclcpp::Publisher<std_msgs::msg::String>::SharedPtr publisher_;

 //---------------------Proceso----------------- 
  rclcpp::Publisher<tutorial_interfaces::msg::Control>::SharedPtr publisher_p; 

  size_t count_;
};


//----------------------------------Publisher------------------------------------


int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  //rclcpp::spin(std::make_shared<MinimalSubscriber>());
  rclcpp::spin(std::make_shared<MinimalPublisher>());
  rclcpp::shutdown();
  return 0;
}
