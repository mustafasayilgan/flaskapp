Vagrant.configure("2") do |config|
  config.vm.box = "spox/ubuntu-arm"
  config.vm.box_version = "1.0.0"
  config.vm.network "private_network", ip: "192.168.56.11"
  config.vm.provider "vmware_desktop" do |vmware|
    vmware.gui = true
    vmware.allowlist_verified = true
  end
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "provision.yml"
  end
  # Forward port 6789 on host to port 5000 on guest
  config.vm.network :forwarded_port, host: 6789, guest: 5000
end
