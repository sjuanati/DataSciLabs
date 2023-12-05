## Instructions for setting up Jupyter Notebook on AWS EC2 and accessing via local VSCode

**In AWS EC2**:

1) Install pip3:
```shell
sudo apt install python3-pip
```

2) Install jupyter:
```shell
pip3 install jupyter
```

3) Update required to run jupyter properly:
```shell
# edit bash
vi ~/.bashrc
# add this line at the end of the file
export PATH=$PATH:/home/ubuntu/.local/bin
# reboot or do this in current session
source ~/.bashrc
```

4) Start jupyter server:
```shell
jupyter notebook --no-browser --ip=0.0.0.0 --port=3011 --NotebookApp.token='your_permanent_token'
```

**In local machine**:

5) Add the new server into `.ssh/config`:
```shell
Host spark-ec2-instance
    HostName ec2-...compute.amazonaws.com
    User ubuntu
    IdentityFile /Users/userX/.ssh/spark_key.pem
```
5) Install 'Remote - SSH extension' in VSCode and add server:

	Open a remote window -> Connect to Host... -> Add New SSH Host... ->
	`ubuntu@ec2-...compute.amazonaws.com` 

6) Update config file In VSCode:

   	settings -> remote.ssh -> Config File: `/Users/userX/.ssh/config`

8) Open a new jupyter notebook, and when running it:

	Select Another Kernel... -> Existing Jupyter Server -> `http://ec2-...compute.amazonaws.com:3011/tree?token=your_permanent_token`
