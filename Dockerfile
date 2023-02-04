FROM bitnami/spark:latest

WORKDIR /model_conversion
USER root
RUN apt-get update && \
    apt-get install -y openjdk-8-jdk && \
    apt-get clean && \
    update-ca-certificates -f
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/
RUN export JAVA_HOME
RUN export PYSPARK_SUBMIT_ARGS="--master spark://127.0.0.1:6666"
RUN pip install py4j
RUN pip install notebook
RUN pip install pandas
RUN pip install numpy
RUN pip install matplotlib
RUN #pip install scikit-learn
RUN pip install seaborn
# RUN pip install tensorflow
RUN pip install keras
RUN pip install elephas
ENTRYPOINT [ "/bin/bash" ]