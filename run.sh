docker run -v /home/hadoop/spark:/home/hadoop/spark \
           --name spark \
           -w /home/hadoop/spark \
           -i -t -p 8888:8888 --rm spark
