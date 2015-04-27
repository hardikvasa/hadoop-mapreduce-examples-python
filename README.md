# Hadoop Mapreduce Examples in Python
Couple of the Mapreduce examples in python and a documentation on running them!

## Steps of running the codes

**Folder Structure**

The files are assumed to be stored in the given locations in the Linux OS. This is just an example illustration and in real the location does not matter.

* Hadoop installed in: /usr/local
* words.txt (sample word file on which the mapreduce jobs are run): /usr/local
* mapper.py (mapper file) and reducer.py (reducer file): /usr/local 
* words.txt in hdfs: /wordcount


**Creating Files**

`touch words.txt` 


**Making Directory in hdfs**

`hadoop fs -mkdir -p /wordcount`



**Copying test file from local directory to hdfs**

`hadoop fs -copyFromLocal /usr/local/words.txt /wordcount`



**Check for file listing on hdfs:**

`hadoop fs -ls /wordcount`


**Running the mapreduce job**

`/usr/local/hadoop/bin/hadoop  jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -file /usr/local/mapper.py    -mapper mapper.py -file /usr/local/reducer.py   -reducer reducer.py -input /wordcount/words.txt -output /wordcount/output`


**Print the output**

`hadoop fs -cat /wordcount/output/part-00000`


**Remove the output folder from hdfs**  

`hadoop dfs -rmr hdfs:///wordcount/output`


**User friendly list of files and sizes in a directory**

`ls -lh`


**Giving full permissions to a folder if required**

`chmod 777 -R /usr/local/hadoop_store`
