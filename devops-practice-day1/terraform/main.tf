variable "project_name" {
    type = string
}

resource "local_file" "practice" "{
    content = "Project: ${var.project_name}"
    filename = "${path.module}/info.txt"
}

output "file_output" {
    value = local_file.practice.filename
}