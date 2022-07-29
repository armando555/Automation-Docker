# Automation-Docker
 This is a automation of performance explorer, you only have to build and run the docker image. This automation can choose between 3 kind of performance tests(stress, spike, soak). Also, you can choose the specific endpoint that you cant to test (add, subtract, multiply, divide). 

 In adition, you can pass the specific project name, # job, build, the threads for the test, times of rampup, duration, shutdown( this only is used in spike test)

 # To build the image, you have to pass the credentials and the url of git to install performance explorer in the container
 ```
 docker image build --build-arg username="username" --build-arg password="password" --build-arg username2="username2" --build-arg password2="password2*" --build-arg urlGit="GITHUB PART" -t ubuntu-cli-image-java .
 ```

 # To execute you have to pass the different values of the ENV variable to run a specific test, specific endpoint, url to test, etc. the next image is a example
 you can use docker desktop and run the image or run the container by terminal with the arg -e


  ![Alt text](./img/docker%20desktop.png?raw=true "Image")

  ![Alt text](./img/example%20Automation.png?raw=true "Image")

