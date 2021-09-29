# Reconate

# Pre-Requisite
Make sure to have "Go" latest version is installed and paths are correctly set.

# Installation
Clone the repository
Run the following script to install necessary tools: sh install.sh
Navigate to ~/home directory and Simply run following command:
./reconate.sh scope.txt

To use it over vps for performing recon on larger set of targets perform following command:
screen -S <screen_name> ~/reconate.sh -h

This will keep Reconate running even if the SSH Connection is terminated or you turn off your local machine.
