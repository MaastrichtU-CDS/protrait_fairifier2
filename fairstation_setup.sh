#!/usr/bin/env sh
# Before running the script, make it executable chmod +x command
# method to download and setup environment
ubuntu_env_setup(){
	sudo apt update && sudo apt install apt-transport-https git ca-certificates curl gnupg lsb-release -y 
	sudo mkdir -p /etc/apt/keyrings 
	curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
	echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
	sudo apt update
	sudo apt install docker-ce docker-ce-cli containerd.io docker-compose-p -y
	# sudo usermod -aG docker $USER -- if permission becomes an issue
	# If this docker install fails, can install docker compose through pip. Using the latest version, hopefully does not break anything else.
	sudo curl -L https://github.com/docker/compose/releases/download/v2.10.0/docker-compose-linux-x86_64  -o /usr/local/bin/docker-compose
	sudo chmod +x /usr/local/bin/docker-compose
	sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
	sudo service docker start
	docker-compose --version
}

redhat_env_setup(){
	sudo dnf config-manager --add-repo=https://download.docker.com/linux/centos/docker-ce.repo
	sudo yum update && sudo yum install -y yum-utils git curl wget #device-mapper-persistent-data lvm2
	sudo yum install docker-ce --allowerasing # if dependency issues with podman
	sudo yum install -y docker-ce-cli containerd.io 
	sudo systemctl enable --now docker
	#systemctl status docker
	sudo usermod -aG docker $USER
	source ~/.bash_profile
	#newgrp docker
	id -nG
	docker version
	curl -s https://api.github.com/repos/docker/compose/releases/latest | grep browser_download_url  | grep docker-compose-linux-x86_64 | cut -d '"' -f 4 | wget -qi -
	chmod +x docker-compose-linux-x86_64
	sudo mv docker-compose-linux-x86_64 /usr/local/bin/docker-compose
	docker-compose version
	rm docker-compose-linux*
}

docker_setup(){
	docker-compose up -d --quiet-pull
}

repo_setup(){
	git clone https://gitlab.com/aiaragomes/fairifier2.git
	cd fairifier2
	cp .env.example .env
}

echo "Running the process as sudo"
echo "Setting up the environment"
# ubuntu_env_setup
redhat_env_setup

echo "Downloading the repo and creating the environment file for airflow"
repo_setup

echo "Creating docker containers"
docker_setup

echo "Done. Airflow can be accessed on 8080, Graphdb on 7200, term mapper on 5001"
