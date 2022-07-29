# For more information, please refer to https://aka.ms/vscode-docker-python
FROM ubuntu:18.04

RUN apt-get update && apt-get install -y software-properties-common git wget nano curl

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

# JMeter Version
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

WORKDIR /plugin

COPY . /plugin/

RUN cd /opt \
 && curl -O https://repo1.maven.org/maven2/kg/apc/jmeter-plugins-manager/${JMETER_PLUGIN_MANAGER_VERSION}/jmeter-plugins-manager-${JMETER_PLUGIN_MANAGER_VERSION}.jar \
 && curl -O https://repo1.maven.org/maven2/kg/apc/cmdrunner/${CMD_RUNNER_VERSION}/cmdrunner-${CMD_RUNNER_VERSION}.jar \
 && mv cmdrunner-${CMD_RUNNER_VERSION}.jar /opt/apache-jmeter-${JMETER_VERSION}/lib \
 && mv jmeter-plugins-manager-${JMETER_PLUGIN_MANAGER_VERSION}.jar /opt/apache-jmeter-${JMETER_VERSION}/lib/ext
RUN java -cp /opt/apache-jmeter-${JMETER_VERSION}/lib/ext/jmeter-plugins-manager-${JMETER_PLUGIN_MANAGER_VERSION}.jar org.jmeterplugins.repository.PluginManagerCMDInstaller
RUN chmod +x /opt/apache-jmeter-${JMETER_VERSION}/bin/PluginsManagerCMD.sh
RUN /opt/apache-jmeter-${JMETER_VERSION}/bin/PluginsManagerCMD.sh install jpgc-casutg



