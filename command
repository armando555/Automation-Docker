jmeter -n -t ./jmx/"+name_file_jmx+" -Jurl="+url+" -Jpuerto="+port+" -Jthreads="+threads+" -Jrampup="+rampup+" -Jendpoint="+endpoint+" -Jtime="+duration+" -JtimeWait="+time_wait+" -JpathSave=./jtl/"+name_file_jtl+".jtl"




docker image build --build-arg username="username" --build-arg password="password" --build-arg username2="username2" --build-arg password2="password2*" --build-arg urlGit="GITHUB PART" -t ubuntu-cli-image-java .


docker image build -t ubuntu-jmeter-plugin .


jmeter -n -t peak_load_test.jmx -Jurl=ec2-3-141-17-194.us-east-2.compute.amazonaws.com -Jpuerto=8080 -Jthreads=100 -Jrampup=10 -Jendpoint=all -Jtime=60 -JtimeWait=3000 -JpathSave=./jtl/resultados.jtl -Jshutdown=20 -Jinitial=10