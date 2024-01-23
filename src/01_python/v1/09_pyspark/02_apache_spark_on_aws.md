### Instructions for setting up Apache Spark on AWS EC2

**In AWS EC2**:

1) Install Java (just to run Java apps, so no jdk):
```shell
sudo apt-get install default-jre
```

2) Install py4j (to allow PySpark connect to Apach Spark via JVM):
```shell
pip3 install py4j
```

3) Install Apache Spark:
```shell
wget https://dlcdn.apache.org/spark/spark-3.5.0/spark-3.5.0-bin-hadoop3.tgz
tar -xzf spark-3.5.0-bin-hadoop3.tgz
```

4) Edit bash and update paths:
```shell
# edit bash
vi ~/.bashrc
# update paths for spark
export SPARK_HOME=/home/ubuntu/spark-3.5.0-bin-hadoop3
export PATH=$PATH:/home/ubuntu/.local/bin:$SPARK_HOME/bin:$SPARK_HOME/sbin
# reboot or update current session
source ~/.bashrc
```

5) Install PySpark:
```shell
pip3 install pyspark
```
