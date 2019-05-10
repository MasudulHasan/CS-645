#!/bin/bash
#Need root privileges 

#add certificate to linux root CAs
sudo apt-get install ca-certificates
sudo cp apache-selfsigned.crt /usr/local/share/ca-certificates/apache-selfsigned.crt
sudo update-ca-certificates


#sudo apt install libnss3-tools
certfile="apache-selfsigned.crt"
certname="My Root CA"

#add to mozilla firefox
for certDB in $(find ~/ -name "cert8.db")
do
	certdir=$(dirname ${certDB});
	certutil -A -n "${certname}" -t "TCu,Cu,Tu" -i ${certfile} -d dbm:${certdir}
done
#add to chrome
for certDB in $(find ~/ -name "cert9.db")
do
	certdir=$(dirname ${certDB});
	certutil -A -n "${certname}" -t "TCu,Cu,Tu" -i ${certfile} -d sql:${certdir}
done

