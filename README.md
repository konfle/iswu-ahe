# Application System for Selection of Optimal Programming Language

### Stack of Technology
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/kubernetes-%23326ce5.svg?style=for-the-badge&logo=kubernetes&logoColor=white)
![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)

### Project Goal
The project aims to develop an inference system that, leveraging prior information about an IT project and the user's objectives, assists in choosing the most suitable programming language for the task.

## Environment

The recommended runtime environment for the application is [Minikube](https://minikube.sigs.k8s.io/docs/start/ "Minikube docs start").

### Benefits of Using Minikube as a Runtime Environment

- <b>Environmental Isolation:</b><br>
  Minikube allows you to run your Kubernetes cluster on a local machine, enabling you to environmentally isolate your application. This allows you to test the application in a controlled environment, minimize conflicts and see how the application will perform in real production conditions.

- <b> Ease of Startup:</b><br>
Minikube provides a simple and fast way to launch a Kubernetes cluster on a local machine. This allows developers to quickly access the Kubernetes environment without having to configure remote clusters.

- <b>Kubernetes Compatibility Testing:</b><br>
If an application is designed to run in a Kubernetes-based environment, using Minikube allows it to be tested for Kubernetes compatibility even before deployment to an actual production cluster.


## Database Management and Configuration

This project using PostgresSQL database.

Database version:
```bash
root@postgres-5cdf75db4d-ts24n:/# psql --version
psql (PostgreSQL) 16.1 (Debian 16.1-1.pgdg120+1)
```

### Kubernetes Resources for Minikube Cluster

##### Deployment
```bash
kubectl create --filename <path to database deployment>
```

##### Service
```bash
kubectl create --filename <path to database service>
```

##### PersistentVolumeClaim
```bash
kubectl create --filename <path to database PersistentVolumeClaim>
```

##### Secret
```bash
kubectl create --filename <path to database secret>
```

### Preparing the Database on the Minikube Cluster

##### Enter the Database Kubernetes Pod
```bash
kubectl exec --stdin --tty <data base pod name> --namespace default -- bash
```

##### Login to the Database
```bash
psql --username=<user name> --dbname=<database name>
```

##### Create a Table for Expert Knowledge
```sql
CREATE TABLE knowledge_base (
    id SERIAL PRIMARY KEY,
    condition VARCHAR(255),
    languages VARCHAR(255) ARRAY
);
```

##### Inject Expert Knowledge
```sql
INSERT INTO knowledge_base (condition, languages) VALUES
    ('app_type == "web" and not performance', '{"Python", "JavaScript", "Java", "Ruby", "PHP", "Go"}'),
    ('app_type == "web" and performance', '{"JavaScript", "Java", "Go"}'),
    ('app_type == "mobile" and performance', '{"Java", "Kotlin", "Swift"}'),
    ('app_type == "mobile" and not performance', '{"Java", "Kotlin", "Swift", "Objective-C", "Flutter", "React-Native"}'),
    ('app_type == "text"', '{"Bash/Shell", "Go"}'),
    ('app_type == "text" and not performance', '{"Bash/Shell", "Python", "Perl", "Lua", "Go"}');
```


## Deployment on Minikube Cluster and Service Launch
##### Deployment
```bash
kubectl create --filename <path to database deployment>
```

##### Service
```bash
kubectl create --filename <path to database service>
```

##### Service Launch
```bash
minikube service <name of application service>
```

##### Expected Result (it may be different depending on OS)
```bash
PS D:\iswu-ahe> minikube service iswu
|-----------|------|-------------|--------------|
| NAMESPACE | NAME | TARGET PORT |     URL      |
|-----------|------|-------------|--------------|
| default   | iswu |             | No node port |
|-----------|------|-------------|--------------|
* service default/iswu has no node port
* Starting tunnel for service iswu.
|-----------|------|-------------|------------------------|
| NAMESPACE | NAME | TARGET PORT |          URL           |
|-----------|------|-------------|------------------------|
| default   | iswu |             | http://127.0.0.1:57675 |
|-----------|------|-------------|------------------------|
* Opening service default/iswu in default browser...
! Because you are using a Docker driver on windows, the terminal needs to be open to run it.
```

## Quality Assurance and Testing Procedures

### Unit Tests

##### Command to run all test
```bash
kubectl exec -it <pod name> -- bash -c "python -m unittest"
```

###### Expected Result
```bash
PS D:\iswu-ahe> kubectl exec -it iswu-5498b7b64b-ttgz2 -- bash -c "python -m unittest"
.........
----------------------------------------------------------------------
Ran 9 tests in 0.012s

OK
```

##### Command to run specific test suite
```bash
kubectl exec -it <pod name> -- bash -c "python -m unittest <test directory>.<test suite name>"
```

###### Expected Result
```bash
PS D:\iswu-ahe> kubectl exec -it iswu-5498b7b64b-ttgz2 -- bash -c "python -m unittest tests.test_api"
..
----------------------------------------------------------------------
Ran 2 tests in 0.010s

OK

```

##### Command to run specific test case
```bash
kubectl exec -it <pod name> -- bash -c "python -m unittest <test directory>.<test suite name>.<test case name>"
```

```bash
kubectl exec -it <pod name> -- bash -c "python -m unittest <test directory>.<test suite name>.<test class name>.<test case name>"
```


###### Expected Result
```bash
.
----------------------------------------------------------------------
Ran 1 test in 0.007s

OK
```