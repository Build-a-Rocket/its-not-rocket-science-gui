apt update
apt -y install sudo
adduser esp sudo
# sudo pam-auth-update
sudo chmod 0640 /etc/shadow
echo \"esp:esp\" | chpasswd
su esp