#!/bin/bash
sudo ufw allow 'Apache Full'
sudo ufw delete allow 'Apache'


sudo a2enmod ssl
sudo a2enmod headers
sudo a2ensite default-ssl
sudo a2enconf ssl-params

sudo systemctl restart apache2
