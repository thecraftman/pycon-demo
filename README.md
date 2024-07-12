# pycon-demo

Deploy a WSGI APP with Ansible, Python, and Terraform

- Update the developer key in your TF code.

- Deploy the TF code and replace your EC2 instance in the nginx conf file using `terraform apply`

- Deploy your ansible code to deploy the frontend and backend in the playbook.yml and inventory file using `ansible-playbook -i inventory.ini playbook.yml`
