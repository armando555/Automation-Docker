# For more information, please refer to https://aka.ms/vscode-docker-python
FROM ubuntu:18.04

RUN apt-get update && apt-get install -y software-properties-common git wget nano curl

RUN add-apt-repository ppa:deadsnakes/ppa 
# 
RUN apt-get update && apt-get install -y python3.7 python3-pip 

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Setting credentials
ARG username
ARG username2
ARG password
ARG password2
ARG urlGit
# Verify credentials
RUN echo ${username}
RUN echo ${password}

# Install pip CLI
RUN python3.7 -m pip install --no-cache-dir --upgrade "git+https://${username}:${password}@${urlGit}"

RUN psl-perfexp version
# Add the JDK 8 and accept licenses (mandatory)
RUN apt-get install -y openjdk-8-jdk && \
	apt-get install -y ant && \
	apt-get clean && \
	rm -rf /var/lib/apt/lists/* && \
	rm -rf /var/cache/oracle-jdk8-installer;

# Fix certificate issues, found as of     
RUN apt-get update && \
	apt-get install -y ca-certificates-java && \
	apt-get clean && \
	update-ca-certificates -f && \
	rm -rf /var/lib/apt/lists/* && \
	rm -rf /var/cache/oracle-jdk8-installer;

# Setup JAVA_HOME, this is useful for docker commandline
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/
RUN export JAVA_HOME

# JMeter Version, plugin manager and cmd runner
ARG JMETER_VERSION="5.5"
ARG JMETER_PLUGIN_MANAGER_VERSION="1.6"
ARG CMD_RUNNER_VERSION="2.2"

# Download and unpack the JMeter tar file
RUN cd /opt \
 && wget https://dlcdn.apache.org//jmeter/binaries/apache-jmeter-${JMETER_VERSION}.tgz \
 && tar xzf apache-jmeter-${JMETER_VERSION}.tgz \
 && rm apache-jmeter-${JMETER_VERSION}.tgz

# Create a symlink to the jmeter process in a normal bin directory
RUN ln -s /opt/apache-jmeter-${JMETER_VERSION}/bin/jmeter /usr/local/bin

# Copying custom property file
COPY user.properties /opt/apache-jmeter-${JMETER_VERSION}/bin/user.properties

#Installing plugin manager
RUN cd /opt \
 && curl -O https://repo1.maven.org/maven2/kg/apc/jmeter-plugins-manager/${JMETER_PLUGIN_MANAGER_VERSION}/jmeter-plugins-manager-${JMETER_PLUGIN_MANAGER_VERSION}.jar \
 && curl -O https://repo1.maven.org/maven2/kg/apc/cmdrunner/${CMD_RUNNER_VERSION}/cmdrunner-${CMD_RUNNER_VERSION}.jar \
 && mv cmdrunner-${CMD_RUNNER_VERSION}.jar /opt/apache-jmeter-${JMETER_VERSION}/lib \
 && mv jmeter-plugins-manager-${JMETER_PLUGIN_MANAGER_VERSION}.jar /opt/apache-jmeter-${JMETER_VERSION}/lib/ext
RUN java -cp /opt/apache-jmeter-${JMETER_VERSION}/lib/ext/jmeter-plugins-manager-${JMETER_PLUGIN_MANAGER_VERSION}.jar org.jmeterplugins.repository.PluginManagerCMDInstaller
RUN chmod +x /opt/apache-jmeter-${JMETER_VERSION}/bin/PluginsManagerCMD.sh
RUN /opt/apache-jmeter-${JMETER_VERSION}/bin/PluginsManagerCMD.sh install jpgc-casutg

#PASSING THE JTL FILES to the container
WORKDIR /cli

COPY . /cli

#Installing dependencies
RUN python3.7 -m pip install -r requirements.txt

#setting workdir in container
WORKDIR /cli/app

#Setting ENV variables
ENV URL="performance url api"
ENV URL2="ec2-3-141-17-194.us-east-2.compute.amazonaws.com"
ENV PORT="8080"
#ENV THREADS="10"
ENV RAMPUP="10"
ENV DURATION="3600"
ENV TIME="3000"
ENV JTL_FILE="resultados"
ENV JMX_FILE="Automation.jmx"
ENV USERNAMEP=${username2}
ENV PASSWORD=${password2}
ENV PROJECT_NAME="Armando Training"
ENV APP_NAME="Baldor Inc"
ENV TRANS_NAME="Random transactions"
ENV JOB="job 1"
ENV BUILD="1"
ENV VERSION="1.0"
ENV TEST_PLAN="TEST STRESS"
ENV TAG="1 hour spike all"
ENV THREADS="100"
ENV SHUTDOWN="20"
ENV INITIAL="10"
#add,subtract,multiply,divide,all
ENV ENDPOINT="all"

#stress_all,stress_one,peak_all,peak_one,spike_one,spike_all
ENV TEST="peak_all"


#CREATING SCRIPT TO RUN
RUN echo "python3.7 app.py"  > /run_module.sh

ENTRYPOINT ["/bin/bash", "/run_module.sh"]





