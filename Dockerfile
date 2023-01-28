FROM bitnami/spark:latest

WORKDIR /model_conversion
USER root
RUN apt-get update && \
    apt-get install -y openjdk-11-jdk ca-certificates-java && \
    apt-get clean && \
    update-ca-certificates -f
ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64/
RUN export JAVA_HOME
RUN export PYSPARK_SUBMIT_ARGS="--master spark://127.0.0.1:6666"
RUN pip install py4j
RUN pip install notebook
RUN pip install pandas
RUN pip install numpy
RUN pip install matplotlib
RUN pip install scikit-learn
RUN pip install seaborn
RUN echo "spark.sql.autoBroadcastJoinThreshold=-1" >> /opt/bitnami/spark/conf/spark-defaults.conf
ENTRYPOINT [ "/bin/bash" ]