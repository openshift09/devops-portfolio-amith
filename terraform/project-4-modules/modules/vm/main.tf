resource "null_resource" "vm" {
  provisioner "local-exec" {
    command = <<EOF
VBoxManage createvm --name ${var.vm_name} --ostype Ubuntu_64 --register

VBoxManage modifyvm ${var.vm_name} --memory ${var.memory} --cpus ${var.cpus} --nic1 nat --nic2 hostonly --hostonlyadapter2 "VirtualBox Host-Only Ethernet Adapter"

VBoxManage createhd --filename "${path.module}/${var.vm_name}.vdi" --size ${var.disk_size}

VBoxManage storagectl ${var.vm_name} --name "SATA" --add sata --controller IntelAhci

VBoxManage storageattach ${var.vm_name} --storagectl "SATA" --port 0 --device 0 --type hdd --medium "${path.module}/${var.vm_name}.vdi"

VBoxManage storageattach ${var.vm_name} --storagectl "SATA" --port 1 --device 0 --type dvddrive --medium "${path.module}/../../iso/ubuntu.iso"

VBoxManage startvm ${var.vm_name} --type headless
EOF
  }
}
