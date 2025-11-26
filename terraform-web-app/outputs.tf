output "instance_public_ip" {
  description = "Public IP of the EC2 instance"
  value       = aws_instance.web.public_ip
}

output "instance_public_dns" {
  description = "Public DNS of the EC2 instance"
  value       = aws_instance.web.public_dns
}

output "ssh_connection" {
  description = "Command to SSH into the instance"
  value       = "ssh ec2-user@${aws_instance.web.public_ip}"
}
