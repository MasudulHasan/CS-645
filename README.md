# CS-645
This is the repository for Internet Security(CS-645) project

The goal of this project is to create self signed certificate and embade the certificate to the trusted CAS list. I have divided my work plan to 3 steps.
  1. configure a apache server in local machine
  2. create a self signed certificate for the localhost 127.0.0.1
  3. Add the created certificate to trusted CAS list to make it a valid certificate 
  
## Step 1: 
  I have configured apache server in my local machine. I am using Ubuntu 18.04.02 as my local machine. This link has step by step instruction for installing and configuring apache server in ubuntu.

https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-ubuntu-18-04

## step 2:
  To create a self signed certificate we have to create a public key. This article gives step by step instruction on how to create self signed certificate.
  https://www.digitalocean.com/community/tutorials/how-to-create-a-self-signed-ssl-certificate-for-apache-in-ubuntu-18-04
  
I automated this instruction in "create_self_certificate.py" to create and put the necessary files in the right directory. To make the other necessary changes for the server "make_configuration.sh" files is used. Both files need root/sudo permission to run.

## step 3:
https://thomas-leister.de/en/how-to-import-ca-root-certificate/

This acticle gives very nice instruction on how to add the self assigned certificate in Trusted CA list. 


 
      sudo mkdir /usr/local/share/ca-certificates/extra
      sudo cp root.cert.pem /usr/local/share/ca-certificates/extra/root.cert.crt
      sudo update-ca-certificates

These code add the self signed certificate in Linux system trusted CA list. But for the browsers like Mozilla and Chrome isn't not sufficient. Web browsers like Firefox, Chromium, Google Chrome, Vivaldi and even e-mail clients like Mozilla Thunderbird don’t make use of the OS trust store, but use their own certificate trust store. These trust stores are files in the user directory, named “cert8.db” and “cert9.db” (for newer versions). 

By running the script "add_certificate_CA_list.sh" we can add the certificate to the trusted list for Chrome and Firefox. Here are the screenshots from Both firefox and chome's trusted CA list shown in the certificate list of the browser. 


![alt text](https://github.com/MasudulHasan/CS-645/blob/master/Screenshot%20from%202019-05-09%2022-57-49.png)


![alt text](https://github.com/MasudulHasan/CS-645/blob/master/Screenshot%20from%202019-05-09%2022-58-37.png)

![alt text](https://github.com/MasudulHasan/CS-645/blob/master/Screenshot%20from%202019-05-10%2022-48-50.png)


