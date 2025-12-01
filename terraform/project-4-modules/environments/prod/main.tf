module "prod_vm" {
  source = "../../modules/vm"

  vm_name   = "prod-vm"
  cpus      = 4
  memory    = 4096
  disk_size = 20000
  ip        = "192.168.56.42"
}
