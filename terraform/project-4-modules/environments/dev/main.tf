module "dev_vm" {
  source = "../../modules/vm"

  vm_name   = "dev-vm"
  cpus      = 2
  memory    = 2048
  disk_size = 10000
  ip        = "192.168.56.40"
}
