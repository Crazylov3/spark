docker run -v /home/hadoop/spark:/home/hadoop/spark \
           --name spark \
           -w /home/hadoop/spark \
           -i -t --rm spark
