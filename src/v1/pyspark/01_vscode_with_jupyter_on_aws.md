### Instructions for setting Up Jupyter Notebook on AWS EC2 and accessing via local VSCode

**In AWS EC2**:

1) Install pip3:
```sudo apt install python3-pip```

2) Install jupyter:
```pip3 install jupyter```

3) Update required to run jupyter properly
```
# edit bash
vi ~/.bashrc
# add this line at the end of the file
export PATH=$PATH:/home/ubuntu/.local/bin
# reboot or do this in current session
source ~/.bashrc
```

4) Start jupyter server:
```jupyter notebook --no-browser --ip=0.0.0.0 --port=3011 --NotebookApp.token='your_permanent_token'```

**In local machine**:

5) Add the new server into `.ssh/config`:
```
Host spark-ec2-instance
    HostName ec2-...compute.amazonaws.com
    User ubuntu
    IdentityFile /Users/userX/.ssh/spark_key.pem
```
5) Install 'Remote - SSH extension' in VSCode and add server:

	Open a remote window -> Connect to Host... -> Add New SSH Host... ->
	`ubuntu@ec2-...compute.amazonaws.com` 

6) In VSCode -> settings -> remote.ssh -> Config File:
	`/Users/userX/.ssh/config`

7) Open a new junyper notebook, and when running it
	-> Select Another Kernel... -> Existing Jupyter Server ->
	```http://ec2-...compute.amazonaws.com:3011/tree?token=your_permanent_token```
