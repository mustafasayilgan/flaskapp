This application has developed for macOS M1(apple silicon) to deploy a Flask app using Gunicorn, Nginx, and Ansible on an Ubuntu server via Vagrant.

For running vagrant on m1 you have to follow this steps;

1- Rosetta: Rosetta is a software compatibility layer developed by Apple that allows Mac computers with Apple Silicon processors (such as the M1 chip) to run apps designed for Intel-based Macs. Rosetta acts as a translator, enabling older software that was built for Intel-based Macs to run on the newer Apple Silicon-based Macs.

"/usr/sbin/softwareupdate --install-rosetta --agree-to-license"

2- VMware: VMware’s virtualization software allows multiple operating systems to run on a single physical machine. Click here (https://customerconnect.vmware.com/home) to create an account on vmware. Then, click here(https://customerconnect.vmware.com/downloads/get-download?downloadGroup=FUS-PUBTP-2021H1) to download the .dmg installer for VMWare Fusion Tech Preview.

3- Install Vagrant with Homebrew:

"brew install --cask vagrant"

4- Create a link: A symbolic link, also known as a symlink or a soft link, is a unique type of file that acts as a pointer to another file or directory, referred to as the target.

" ln -s /Applications/VMWare\ Fusion\ Tech\ Preview.app /Applications/VMWare\ Fusion.app"

5- Install vmware provider and install plugin(vagrant-vmware-desktop): This plugin provides support for using VMware Fusion or VMware Workstation as the virtualization provider for Vagrant on macOS and Windows. To download and install Vagrant vmware Utility click here(https://releases.hashicorp.com/vagrant-vmware-utility/1.0.21/vagrant-vmware-utility_1.0.21_x86_64.dmg), then click on “allow” to download. This will download the compatible file called ‘vagrant-vmware-utility_1.0.21_x86_64.dmg’.

Next, run the command to install plugin

"vagrant plugin install vagrant-vmware-desktop"

6- Use Ubuntu server on the VM.

To start the vm automatically run the command below

"vagrant up"

To ssh into the ubuntu server automatically run the command below

"vagrant ssh"

