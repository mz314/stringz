# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  # Base Box
  # --------------------
  config.vm.box = "ubuntu/trusty64"
  config.vm.hostname = "stringz.local"

  # Connect to IP
  # Note: Use an IP that doesn't conflict with any OS's DHCP (Below is a safe bet)
  # --------------------
  config.vm.network :private_network, ip: "192.168.50.4"

  # Forward to Port
  # --------------------
  config.vm.network :forwarded_port, guest: 3306, host: 3306, auto_correct: true

  # Optional (Remove if desired)
  # --------------------
  config.vm.provider :virtualbox do |vb|
    vb.customize [
      "modifyvm", :id,
      "--memory", 512,             # How much RAM to give the VM (in MB)
      "--cpus", 1,                 # Muli-core in the VM
      "--ioapic", "on",
      "--natdnshostresolver1", "on",
      "--natdnsproxy1", "on"
    ]
  end

  # If true, agent forwarding over SSH connections is enabled
  # --------------------
  config.ssh.forward_agent = true

  # The shell to use when executing SSH commands from Vagrant
  # --------------------
  config.ssh.shell = "bash -c 'BASH_ENV=/etc/profile exec bash'"

  # Synced Folders
  # --------------------
  config.vm.synced_folder ".", "/vagrant/", :mount_options => [ "dmode=777", "fmode=666" ]


  # Provisioning Scripts
  # --------------------
config.vm.provision "file", source: "VagrantProvision/superuser.py", destination: "/home/vagrant/superuser.py"
config.vm.provision "shell", path: "VagrantProvision/init.sh"
config.vm.provision "shell", path: "VagrantProvision/runserver.sh", run: "always"
config.vm.provision "file", source: "VagrantProvision/nginx.conf", destination: "/home/vagrant/nginx.conf"
config.vm.provision "file", source: "VagrantProvision/uwsgi.ini", destination: "/home/vagrant/uwsgi.ini"
config.vm.provision "file", source: "VagrantProvision/uwsgi.include", destination: "/home/vagrant/uwsgi.include"
# config.vm.provision "file", source: "VagrantProvision/wsgi.py", destination: "/home/vagrant/wsgi.py"
# config.vm.provision "shell", path: "VagrantProvision/nginx.sh"
end

