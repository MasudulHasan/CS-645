# CS-645
This is the repository for Internet Security(CS-645) project

The goal of this project is to create self signed certificate and embade the certificate to the trusted CAS list. I have divided my work plan to 4 steps.
  1. configure a apache server in local machine
  2. create a self signed certificate for the localhost 127.0.0.1
  3. Add the created certificate to trusted CAS list to make it a valid certificate
  4. combine the whole process in a single program and automate the whole embading step. 
  
  04-16-19
  Step 1: 
  I have configured apache server in my local machine. I am using Ubuntu 18.04.02 as my local machine. This link has step by step instruction for installing and configuring apache server in ubuntu.

https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-ubuntu-18-04

# step 2:
  To create a self signed certificate we have to create a public key. This article gives step by step instruction on how to create self signed certificate.
  https://www.digitalocean.com/community/tutorials/how-to-create-a-self-signed-ssl-certificate-for-apache-in-ubuntu-18-04
  
