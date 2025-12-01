provider "aws" {
  region = "ap-south-1"
}

resource "aws_instance" "web" {
  ami           = "ami-0cda377a1b884a1bc" # Amazon Linux 2
  instance_type = "t2.micro"
  key_name      = var.keypair

  tags = {
    Name = "DevOps-Project-A"
  }
}

output "public_ip" {
  value = aws_instance.web.public_ip
}
