# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|

  config.vm.box = "debian/jessie64"
  config.vm.box_check_update = false
  config.vm.provision :shell, path: "vagrant/bootstrap.sh"
end
