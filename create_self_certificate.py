import shutil
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes
import subprocess
import time,sys
import shlex

import datetime
import os

# Generate our key
key = rsa.generate_private_key(
	public_exponent=65537,
	key_size=2048,
	backend=default_backend()
)

with open("apache-selfsigned.key", "wb") as f:
 	f.write(key.private_bytes(
 		encoding=serialization.Encoding.PEM,
 		format=serialization.PrivateFormat.TraditionalOpenSSL,
 		encryption_algorithm=serialization.BestAvailableEncryption(b"6901"),
 	))


subject = issuer = x509.Name([
	x509.NameAttribute(NameOID.COUNTRY_NAME, u"US"),
	x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"Nevada"),
	x509.NameAttribute(NameOID.LOCALITY_NAME, u"Reno"),
	x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"Masud.Inc"),
	x509.NameAttribute(NameOID.COMMON_NAME, u"test-site.com"),
])

cert = x509.CertificateBuilder().subject_name(subject).issuer_name(issuer).\
	public_key(key.public_key()).\
	serial_number(x509.random_serial_number()).\
	not_valid_before(datetime.datetime.utcnow()).\
	not_valid_after(
	datetime.datetime.utcnow() + datetime.timedelta(days=365)).\
	add_extension(x509.SubjectAlternativeName([x509.DNSName(u"localhost")]),
	critical=False,).\
	sign(key, hashes.SHA256(), default_backend())

# Write our certificate out to disk.
with open("apache-selfsigned.crt", "wb") as f:
	f.write(cert.public_bytes(serialization.Encoding.PEM))

# command = "cp " + "apache-selfsigned.key" + " /etc/ssl/private/apache-selfsigned.key"
#
# a = subprocess.Popen(shlex.split(command))  # notice stderr
# a.communicate()

shutil.copy2("apache-selfsigned.key", "/etc/ssl/private/apache-selfsigned.key")
shutil.copy2("apache-selfsigned.crt", "/etc/ssl/certs/apache-selfsigned.crt")
