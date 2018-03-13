#!/usr/bin/env groovy

pipeline {
	 
    agent any
    
    environment {
        imgtag="wiprohpe/rsvp:${env.BUILD_NUMBER}"
    }   	    
    stages {
        stage('Build') {
            steps {
                echo 'Building...'
		sh("docker -H :5555 build -t ${imgtag} .")
            }
        }
	stage('Test') {
           steps {
               echo 'Testing RSVP'
	       sh("docker -H :5555 run ${imgtag} python testrsvp.py")	       
            }
	}
	stage('Push') {
           steps {
               echo 'Pushing Image to Docker hub'
	       sh("docker -H :5555 login -u wiprohpe -p Wipro@123")
	       sh("docker -H :5555 push ${imgtag}")	       
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying in kubectl !!!'
		sh("sed -i.bak 's#teamcloudyuga/rsvpapp#${imgtag}#' ./k8s/rsvp-web-deployment.yaml")
		sh("kubectl apply --kubeconfig=/var/lib/jenkins/config --namespace=testing-jsayar -f ./k8s/rsvp-web-deployment.yaml")		
            }
        }
    }
}
