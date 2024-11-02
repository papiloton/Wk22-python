import jenkins
import csv


jenkins_url='http://ec2-18-208-223-15.compute-1.amazonaws.com:8080'
jenkins_username='devops'
jenkins_pass='devops'
server = jenkins.Jenkins(jenkins_url, username=jenkins_username,password=jenkins_pass)

number_jobs=server.jobs_count()
user = server.get_whoami()['fullName']
_jobs =server.get_jobs()
job_list=[]
for job in _jobs:
    job_list.append([job.get('name'), job.get('url'), job.get('coler')])

    with open("jenkins_jobs.csv", 'w',newline='') as f:
        writer = csv.writer(f)
        HEADER=['job_name', 'job_url', 'job_color']
        writer.writerow(HEADER)
        writer.writerow(job_list)