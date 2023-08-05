provider "aws" {
  region = "ap-south-1"
  access_key = "AKIAWA7AQH7HHLQ4SGUY"
  secret_key = "fLsu2+nnD9BDg9sD74/I8/GLgXwPIAW9AW96gwFV"
}

# Create a VPC
resource "aws_vpc" "terraform-example" {
  cidr_block = "10.0.0.0/16"
  tags = {
    "Name" = "terraform-dev"
  }
}

# create a subnet
resource "aws_subnet" "terraform-subnet-1" {
  vpc_id = aws_vpc.terraform-example.id
  cidr_block = "10.0.255.0/24"
  availability_zone = "ap-south-1a"
  tags = {
    "Name" = "terraform-subnet-1"
  }
}

variable "aws_vpc_id" {
  description = "passing cidr to subnet-2"
  type = list(string)
}

data "aws_vpc" "existing_vpc" {
  default = true
}

resource "aws_subnet" "terraform-subnet-2" {
  vpc_id = data.aws_vpc.existing_vpc.id
  cidr_block = var.aws_vpc_id[1]
  # cidr_block = "172.31.128.0/20"
  availability_zone = "ap-south-1a"
}

/* resource "aws_subnet" "terraform-subnet-3" {
  vpc_id = data.aws_vpc.existing_vpc.id
  cidr_block = "172.31.112.0/20"
  availability_zone = "ap-south-1a"
} 
 */

output "vpc_id" {
  value = aws_vpc.terraform-example.id
}

output "subnet-id" {
  value = aws_subnet.terraform-subnet-1.id
}



/* provider install the required plugin for the application
resource is used to create 
data is used to fetch which are present already */