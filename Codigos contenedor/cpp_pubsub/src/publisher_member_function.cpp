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


//--------------------------------------Subscriber-------------------------------



using std::placeholders::_1;

class MinimalSubscriber : public rclcpp::Node
{
public:
  MinimalSubscriber()
  : Node("minimal_subscriber")
  {
    subscription_ = this->create_subscription<tutorial_interfaces::msg::Num>(          // CHANGE    
    "topic", 10, std::bind(&MinimalSubscriber::topic_callback, this, _1));
    
   
    //----------------------Proceso--------------------
    subscription_p = this->create_subscription<tutorial_interfaces::msg::Proceso>(          // CHANGE    
     "topic", 10, std::bind(&MinimalSubscriber::get_proceso, this, _1));

  }

private:
  //void topic_callback(const std_msgs::msg::String::SharedPtr msg) const
    void topic_callback(const tutorial_interfaces::msg::Num::SharedPtr msg) const       // CHANGE
  {
    //RCLCPP_INFO(this->get_logger(), "I heard: '%s'", msg->data.c_str());
   RCLCPP_INFO(this->get_logger(), "I heard: '%d'", msg->num);

  }


   //---------------------Callback del proceso---------------------------------
 void get_proceso(const tutorial_interfaces::msg::Proceso::SharedPtr msg) const       // CHANGE
  {
    //RCLCPP_INFO(this->get_logger(), "I heard: '%s'", msg->data.c_str());
   RCLCPP_INFO(this->get_logger(), "x1 proceso: '%d'", msg->x1);
   RCLCPP_INFO(this->get_logger(), "x3 proceso: '%d'", msg->x3);
   RCLCPP_INFO(this->get_logger(), "u1 proceso: '%d'", msg->u1);



  }

  //rclcpp::Subscription<std_msgs::msg::String>::SharedPtr subscription_;
  rclcpp::Subscription<tutorial_interfaces::msg::Num>::SharedPtr subscription_;       // CHANGE
  
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
   
    publisher_n = this->create_publisher<tutorial_interfaces::msg::Num>("topic", 10);    // CHANGE
   
    publisher_ = this->create_publisher<tutorial_interfaces::msg::Proceso>("topic", 10); 
    timer_ = this->create_wall_timer(
      500ms, std::bind(&MinimalPublisher::timer_callback, this));
  }

private:
  void timer_callback()
  {
    auto message = tutorial_interfaces::msg::Proceso();//Num();  // std_msgs::msg::String();
   
    auto message_n = tutorial_interfaces::msg::Num();   

 //message.data = "Hello, world! " + std::to_string(count_++);
   
    message_n.num=5;    
    message_n.num2=-3;    

    //---------------Proceso-------------
    message.x1=110;//this->count_++;
    message.x2=220;
    message.x3=330;
        
    //RCLCPP_INFO(this->get_logger(), "Publishing: '%s'", message.data.c_str());
  
    RCLCPP_INFO(this->get_logger(), "el numero: '%d'", message_n.num); 
    publisher_n->publish(message_n);

    RCLCPP_INFO(this->get_logger(), "el numero 2: '%d'", message_n.num2); 
    publisher_n->publish(message_n);

    //---------------Proceso----------------
    
    RCLCPP_INFO(this->get_logger(), "x1: '%d'", message.x1); 
    publisher_->publish(message);
    /* */
    RCLCPP_INFO(this->get_logger(), "x2: '%d'", message.x2); 
    publisher_->publish(message);

    RCLCPP_INFO(this->get_logger(), "x3: '%d'", message.x3); 
    publisher_->publish(message);
   
    
 
  }
  rclcpp::TimerBase::SharedPtr timer_;  
 

  rclcpp::Publisher<tutorial_interfaces::msg::Num>::SharedPtr publisher_n;         // CHANGE//rclcpp::Publisher<std_msgs::msg::String>::SharedPtr publisher_;
 //---------------------Proceso----------------- 
  rclcpp::Publisher<tutorial_interfaces::msg::Proceso>::SharedPtr publisher_; 

  size_t count_;
};


//----------------------------------Publisher------------------------------------


int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
 // rclcpp::spin(std::make_shared<MinimalSubscriber>());
  rclcpp::spin(std::make_shared<MinimalPublisher>());
  rclcpp::shutdown();
  return 0;
}
