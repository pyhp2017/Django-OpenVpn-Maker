import os

from django.contrib.auth.models import AbstractUser
import pexpect
from django.db import models

# ==== DOCKER COMMANDS
# docker run -v $PWD/vpn-data:/etc/openvpn --rm -it myownvpn easyrsa build-client-full user nopass
# docker run -v $PWD/vpn-data:/etc/openvpn --rm myownvpn ovpn_getclient <USERNAME> > "username".ovpn


class User(AbstractUser):
    config = models.FileField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            # Create User Config
            # TODO: Change Path here:
            vpn_data_path = '/home/user/vpn-data'
            
            child = pexpect.spawn(
                'docker run -v ' + vpn_data_path + ':/etc/openvpn --rm -it myownvpn easyrsa build-client-full ' + self.username + ' nopass')
            child.expect('Enter pass phrase for /etc/openvpn/pki/private/ca.key:')
            
            # TODO: Change CA key here:
            child.sendline('pyhp2017@gmail.com')
            
            i = child.expect(['Data Base Updated', pexpect.EOF])

            if i == 0:
                print("Certificate Created")
                super().save(*args, **kwargs)
            else:
                print("BAD REQUEST")
                return -1

            # Create VPN CONFIG WITH USERNAME
            # TODO:Change Path here:
            output_path = "/home/user/Django-OpenVpn-Maker/static/configs/"
            os.system(
                "docker run -v " + vpn_data_path + ":/etc/openvpn --rm myownvpn ovpn_getclient " + self.username + " > " + output_path +
                self.username + ".ovpn")
            print("CONFIG CREATED")
            self.config = '/static/configs/' + self.username + '.ovpn'
            
        super().save(*args, **kwargs)
