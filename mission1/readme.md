
```bash
# 1. 개발 환경 정보
- **OS**: macOS 15.7.4 24G517
- **Shell**: /bin/zsh
- **Terminal**: Apple_Terminal
- **Git Version**: git version 2.53.0
- **Docker Version**: Docker version 28.5.2, build ecc6942



#2. 수행 체크리스트

## 1). 현재 위치 및 목록 확인
pwd
/Users/renoirk9330/ia-codyssey/mission1
ls -al
total 8
drwxr-xr-x  3 renoirk9330  renoirk9330   96  7 30 16:11 .
drwxr-xr-x  5 renoirk9330  renoirk9330  160  7 30 15:59 ..
-rw-r--r--  1 renoirk9330  renoirk9330   55  7 30 16:11 mission_check.txt

## 2). 파일 생성 및 내용 확인
touch sample.txt
cat sample.txt

## 3). 복사, 이름 변경, 삭제
cp sample.txt sample_copy.txt 
ls
mission_check.txt	sample_copy.txt		sample.txt
mv sample_copy.txt renamed.txt
ls                            
mission_check.txt	renamed.txt		sample.txt
rm renamed.txt                
ls            
mission_check.txt	sample.txt

## 4). 권한 실습 (chmod [소유자,그룹,기타], r/w/x:4/2/1)
ls -l sample.txt
-rw-r--r--  1 renoirk9330  renoirk9330  0  7 30 17:18 sample.txt
chmod 400 sample.txt # 권한 변경 ( 나만 읽기)
ls -l sample.txt    
-r--------  1 renoirk9330  renoirk9330  0  7 30 17:18 sample.txt
mkdir test_dir
ls -ld test_dir
drwxr-xr-x  2 renoirk9330  renoirk9330  64  7 30 17:31 test_dir
chmod 700 test_dir # 권한 변경 ( 나만 접근 가능)
ls -ld test_dir
drwx------  2 renoirk9330  renoirk9330  64  7 30 17:31 test_dir

## 5). Docker 설치/점검
docker --version
Docker version 28.5.2, build ecc6942
docker info      
Client:
 Version:    28.5.2
 Context:    orbstack
 Debug Mode: false
 Plugins:
  buildx: Docker Buildx (Docker Inc.)
    Version:  v0.29.1
    Path:     /Users/renoirk9330/.docker/cli-plugins/docker-buildx
  compose: Docker Compose (Docker Inc.)
    Version:  v2.40.3
    Path:     /Users/renoirk9330/.docker/cli-plugins/docker-compose

Server:
 Containers: 0
  Running: 0
  Paused: 0
  Stopped: 0
 Images: 0
 Server Version: 28.5.2
 Storage Driver: overlay2
  Backing Filesystem: btrfs
  Supports d_type: true
  Using metacopy: false
  Native Overlay Diff: true
  userxattr: false
 Logging Driver: json-file
 Cgroup Driver: cgroupfs
 Cgroup Version: 2
 Plugins:
  Volume: local
  Network: bridge host ipvlan macvlan null overlay
  Log: awslogs fluentd gcplogs gelf journald json-file local splunk syslog
 CDI spec directories:
  /etc/cdi
  /var/run/cdi
 Swarm: inactive
 Runtimes: io.containerd.runc.v2 runc
 Default Runtime: runc
 Init Binary: docker-init
 containerd version: 1c4457e00facac03ce1d75f7b6777a7a851e5c41
 runc version: d842d7719497cc3b774fd71620278ac9e17710e0
 init version: de40ad0
 Security Options:
  seccomp
   Profile: builtin
  cgroupns
 Kernel Version: 6.17.8-orbstack-00308-g8f9c941121b1
 Operating System: OrbStack
 OSType: linux
 Architecture: x86_64
 CPUs: 6
 Total Memory: 15.67GiB
 Name: orbstack
 ID: 1f348cf6-fba5-4676-8222-be1d259985e2
 Docker Root Dir: /var/lib/docker
 Debug Mode: false
 Experimental: false
 Insecure Registries:
  ::1/128
  127.0.0.0/8
 Live Restore Enabled: false
 Product License: Community Engine
 Default Address Pools:
   Base: 192.168.97.0/24, Size: 24
   Base: 192.168.107.0/24, Size: 24
   Base: 192.168.117.0/24, Size: 24
   Base: 192.168.147.0/24, Size: 24
   Base: 192.168.148.0/24, Size: 24
   Base: 192.168.155.0/24, Size: 24
   Base: 192.168.156.0/24, Size: 24
   Base: 192.168.158.0/24, Size: 24
   Base: 192.168.163.0/24, Size: 24
   Base: 192.168.164.0/24, Size: 24
   Base: 192.168.165.0/24, Size: 24
   Base: 192.168.166.0/24, Size: 24
   Base: 192.168.167.0/24, Size: 24
   Base: 192.168.171.0/24, Size: 24
   Base: 192.168.172.0/24, Size: 24
   Base: 192.168.181.0/24, Size: 24
   Base: 192.168.183.0/24, Size: 24
   Base: 192.168.186.0/24, Size: 24
   Base: 192.168.207.0/24, Size: 24
   Base: 192.168.214.0/24, Size: 24
   Base: 192.168.215.0/24, Size: 24
   Base: 192.168.216.0/24, Size: 24
   Base: 192.168.223.0/24, Size: 24
   Base: 192.168.227.0/24, Size: 24
   Base: 192.168.228.0/24, Size: 24
   Base: 192.168.229.0/24, Size: 24
   Base: 192.168.237.0/24, Size: 24
   Base: 192.168.239.0/24, Size: 24
   Base: 192.168.242.0/24, Size: 24
   Base: 192.168.247.0/24, Size: 24
   Base: fd07:b51a:cc66:d000::/56, Size: 64

## 6). Docker 기본 운영 명령 수행
###1. 이미지 관리
**이미지 다운로드  및 목록 확인**
$ docker pull nginx. 
Using default tag: latest
latest: Pulling from library/nginx
062e450697fa: Pull complete 
82454cdbf456: Pull complete 
3c7ab7949321: Pull complete 
cacfcdd01f30: Pull complete 
b6698f04e005: Pull complete 
2bedaf25031a: Pull complete 
d26f27cc8c41: Pull complete 
Digest: sha256:5a88c9c45479443d7be2eadc894b4ed0a9801bae03d97a5760ae13b5c2005942
Status: Downloaded newer image for nginx:latest
docker.io/library/nginx:latest
$ docker images
REPOSITORY   TAG       IMAGE ID       CREATED       SIZE
nginx        latest    4e5db4761e0f   2 weeks ago   161MB
renoirk9330@c6r7s1 mission1 % 

###2. 컨테이너  관리
**다운로드한 이미지 실행 및  목록 확인 **
$ docker run -d --name my-web nginx
d5882f1b2fe4f633d1dc9cf37f8137d255e26f358edbac41a1e84fd922fe7db0
$ docker ps
CONTAINER ID   IMAGE     COMMAND                   CREATED          STATUS          PORTS     NAMES
d5882f1b2fe4   nginx     "/docker-entrypoint.…"   11 seconds ago   Up 11 seconds   80/tcp    my-web
# 컨테이저 중지
$ docker stop my-web
my-web

###3. 운영 및 모니터링
** 컨테이너 로그 및 리소스 확인**
$ docker logs my-web       
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
/docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
2026/07/30 12:07:11 [notice] 1#1: using the "epoll" event method
2026/07/30 12:07:11 [notice] 1#1: nginx/1.31.3
2026/07/30 12:07:11 [notice] 1#1: built by gcc 14.2.0 (Debian 14.2.0-19) 
2026/07/30 12:07:11 [notice] 1#1: OS: Linux 6.17.8-orbstack-00308-g8f9c941121b1
2026/07/30 12:07:11 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 20480:1048576
2026/07/30 12:07:11 [notice] 1#1: start worker processes
2026/07/30 12:07:11 [notice] 1#1: start worker process 29
2026/07/30 12:07:11 [notice] 1#1: start worker process 30
2026/07/30 12:07:11 [notice] 1#1: start worker process 31
2026/07/30 12:07:11 [notice] 1#1: start worker process 32
2026/07/30 12:07:11 [notice] 1#1: start worker process 33
2026/07/30 12:07:11 [notice] 1#1: start worker process 34
2026/07/30 12:07:56 [notice] 1#1: signal 3 (SIGQUIT) received, shutting down
2026/07/30 12:07:56 [notice] 29#29: gracefully shutting down
2026/07/30 12:07:56 [notice] 29#29: exiting
2026/07/30 12:07:56 [notice] 29#29: exit
2026/07/30 12:07:56 [notice] 32#32: gracefully shutting down
2026/07/30 12:07:56 [notice] 32#32: exiting
2026/07/30 12:07:56 [notice] 33#33: gracefully shutting down
2026/07/30 12:07:56 [notice] 33#33: exiting
2026/07/30 12:07:56 [notice] 30#30: gracefully shutting down
2026/07/30 12:07:56 [notice] 34#34: gracefully shutting down
2026/07/30 12:07:56 [notice] 30#30: exiting
2026/07/30 12:07:56 [notice] 32#32: exit
2026/07/30 12:07:56 [notice] 34#34: exiting
2026/07/30 12:07:56 [notice] 33#33: exit
2026/07/30 12:07:56 [notice] 34#34: exit
2026/07/30 12:07:56 [notice] 30#30: exit
2026/07/30 12:07:56 [notice] 31#31: gracefully shutting down
2026/07/30 12:07:56 [notice] 31#31: exiting
2026/07/30 12:07:56 [notice] 31#31: exit
2026/07/30 12:07:56 [notice] 1#1: signal 17 (SIGCHLD) received from 32
2026/07/30 12:07:56 [notice] 1#1: worker process 32 exited with code 0
2026/07/30 12:07:56 [notice] 1#1: signal 29 (SIGIO) received
2026/07/30 12:07:56 [notice] 1#1: signal 17 (SIGCHLD) received from 31
2026/07/30 12:07:56 [notice] 1#1: worker process 31 exited with code 0
2026/07/30 12:07:56 [notice] 1#1: signal 29 (SIGIO) received
2026/07/30 12:07:56 [notice] 1#1: signal 17 (SIGCHLD) received from 29
2026/07/30 12:07:56 [notice] 1#1: worker process 29 exited with code 0
2026/07/30 12:07:56 [notice] 1#1: worker process 33 exited with code 0
2026/07/30 12:07:56 [notice] 1#1: worker process 34 exited with code 0
2026/07/30 12:07:56 [notice] 1#1: signal 29 (SIGIO) received
2026/07/30 12:07:56 [notice] 1#1: signal 17 (SIGCHLD) received from 30
2026/07/30 12:07:56 [notice] 1#1: worker process 30 exited with code 0
2026/07/30 12:07:56 [notice] 1#1: exit
$ docker stats --no-stream
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT   MEM %     NET I/O   BLOCK I/O   PIDS


##7.컨테이너 실행 및 관리
### 1) 첫번째 컨테이너 실행하기 ( Hello World)
$ docker run hello-world
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
4f55086f7dd0: Pull complete 
Digest: sha256:c3cbe1cc1aa588a64951ac6286e0df7b27fe2e6324b1001c619bb358770c0178
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/

### 2) buntu 컨테이너 실행 및 내부 명령 수행
$ docker run -it ubuntu /bin/bash
Unable to find image 'ubuntu:latest' locally
latest: Pulling from library/ubuntu
ed819469700f: Pull complete 
a3679419df18: Pull complete 
Digest: sha256:3131b4cc82a783df6c9df078f86e01819a13594b865c2cad47bd1bca2b7063bb
Status: Downloaded newer image for ubuntu:latest

ls
bin  boot  dev  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
root@792e4a08e15d:/# echo " Hello from Ubuntu Container!"
 Hello from Ubuntu Container!

echo "Hello from Ubuntu Container!"
Hello from Ubuntu Container!

### 3) 컨테이너 종료/유지 및 attach/exec 차이 정리
① 컨테이너 빠져나오기 (종료 vs 유지)
exit 입력: 컨테이너 내부 쉘을 종료하면서 컨테이너도 함께 정지(Stop) 시킨다.
Ctrl + P, Q 입력: 컨테이너를 정지시키지 않고(Running) 백그라운드로 빠져나온다.
② attach vs exec (실행 중인 컨테이너 접속)
docker attach: 특징	행 중인 컨테이너의 **메인 프로세스(PID 1)**에 접속.	
docker exec: 실행 중인 컨테이너에 새로운 프로세스를 실행.


$ curl http://localhost:8080
<img width="1160" height="412" alt="image" src="https://github.com/user-attachments/assets/23af6809-8a09-40ef-9085-65b192242e02" />

##8.1 웹서버 실행하기 (Nginx)
###1) 포트 매팅 접속
$ docker run -d -p 8080:80 --name my-web nginx
6851386810e6cbe42ae6afdd8a1f352b25b342ca1335403bf1ded1df72287870
**브라우저에서 localhost:8080 접속 성공 확인**
Welcome to nginx!
If you see this page, nginx is successfully installed and working. Further configuration is required for the web server, reverse proxy, API gateway, load balancer, content cache, or other features.

For online documentation and support please refer to nginx.org.
To engage with the community please visit community.nginx.org.
For enterprise grade support, professional services, additional security features and capabilities please refer to f5.com/nginx.

Thank you for using nginx.

### 2. Nginx 컨테이너 실습
- **컨테이너 접속 및 수정**:
$ docker ps # 실행중인 컨테이너 목록 확인
CONTAINER ID   IMAGE     COMMAND                   CREATED          STATUS          PORTS                                     NAMES
6851386810e6   nginx     "/docker-entrypoint.…"   24 minutes ago   Up 24 minutes   0.0.0.0:8080->80/tcp, [::]:8080->80/tcp   my-web
  $ docker exec -it my-web bash` # 컨테이너 내부 접속
root@6851386810e6:/# echo "<h1>Hello, Docker Odyssey! My name is Shirley Kim </h1>" > /usr/share/nginx/html/index.html # 메인 페이지 문구 수정
#브라우저로 가서 localhost:8080 문구 확인
Hello, Docker Odyssey! My name is Shirley Kim


##8.2 Docker를 이용한 웹 서버 배포 실습
*Docker 이미지 빌드한다: Dockerfile을 작성하고 docker build를 통해 독립적인 실행 환경을 생성함.
*포트 포워딩(Port Mapping): -p 8080:5000 옵션을 통해 호스트 OS와 컨테이너 내부의 네트워크를 연결함.
*로그 확인: docker logs [컨테이너명]을 통해 서버 내부의 동작 상태를 확인함.

🐳Docker를 사용하여 간단한 Python Flask 웹 서버를 컨테이너화하고 배포.

(1). 프로젝트 구조
my-web-app/
├── app/
│   └── main.py       # Flask 웹 애플리케이션 소스
└── Dockerfile        # Docker 이미지 빌드 설정 파일

(2). 주요 구성 파일
🐍 Python 애플리케이션 (app/main.py)
Flask를 사용하여 0.0.0.0:5000 포트에서 동작하는 간단한 웹 서버.
python
📋 복사
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return '<h1>Docker Web Server Success!</h1>'
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

🐳 Docker 설정 (Dockerfile)
dockerfile
FROM python:3.9-slim # 1. 베이스 이미지 설정 (Python 3.9)
WORKDIR /app# 2. 작업 디렉토리 설정
RUN pip install flask # 3. Flask 설치
COPY ./app /app # 4. 소스 코드 복사
CMD ["python", "main.py"] # 5. 컨테이너 실행

(3). 실행
1) Docker 이미지 빌드
터미널에서 프로젝트 루트 폴더로 이동한 후 아래 명령어를 입력.
$ docker build -t my-web-server .
2) Docker 컨테이너 실행
빌드된 이미지를 바탕으로 컨테이너를 실행. 호스트의 8080 포트를 컨테이너의 5000 포트와 연결.
$ docker run -d -p 8080:5000 --name my-running-app my-web-server
3) 접속 확인
브라우저에서 다음 주소에 접속하거나 curl 명령어를 사용.
URL: http://localhost:8080
$ curl http://localhost:8080
<h1>Docker Web Server Success!</h1>%


## 🚀 Docker 커스텀 이미지 제작 결과 ( Dockerfile)

### 1. 베이스 이미지 선택
- **선택 이미지**: `python:3.9-slim`
- **이유**: 파이썬 실행 환경을 제공하면서도 이미지 크기가 작아 배포 효율이 높기 때문입니다.

### 2. 커스텀 포인트 및 목적
- **작업 디렉토리 설정 (`WORKDIR /app`)**: 컨테이너 내 앱 경로를 표준화하여 관리를 용이하게 함.
- **패키지 설치 (`RUN pip install flask`)**: 웹 서버 구동에 필요한 Flask 라이브러리를 이미지 빌드 단계에서 미리 설치함.
- **소스 복사 (`COPY ./app /app`)**: 로컬에서 개발한 Flask 코드를 이미지 내부로 포함시킴.

### 3. 빌드 및 실행 명령
- **빌드**: `docker build -t my-web-app .`
- **실행**: `docker run -d -p 8080:5000 my-web-app`

### 4. 실행 결과 확인
- 브라우저에서 `localhost:8080` 접속 시 "Hello, Docker!" 메시지 출력 확인.
- `docker logs [컨테이너ID]`를 통해 Flask 서버 정상 기동 로그 확인.

## Docker 볼륨 영속성 검증
Docker 컨테이너는 삭제되면 내부의 데이터도 함께 사라지는 휘발성 특징을 가지고 있습니다. 이를 해결하기 위해 Docker Volume을 사용하여 컨테이너가 삭제되어도 데이터가 안전하게 유지(영속성)되는지 검증.
1)볼륨을 연결하여 컨테이너 실행
my-db-data라는 이름의 볼륨을 생성함과 동시에 컨테이너의 /app/data 경로에 마운트
$ docker run -d -p 8080:5000 -v my-db-data:/app/data --name web-server my-web-app
2) 데이터 생성
$ docker exec web-server sh -c "echo 'Docker Volume Success!' > /app/data/test.txt"
3)컨테이너 삭제 (Destroy)
$ docker rm -f web-server
4) 새 컨테이너에서 볼륨 재연결 (Restore)
$ docker run -d -p 8080:5000 -v my-db-data:/app/data --name web-server my-web-app
5) 데이터 유지 확인 (Verify)
$ docker exec web-server cat /app/data/test.txt
6) 출력
Docker Volume Success!
7) 결론
컨테이너를 삭제하고 새로 생성했음에도 불구하고, 볼륨에 저장된 데이터는 삭제되지 않고 유지됨을 확인.

## Git 설정 및 GitHub 연동 기록

### 1). Git 사용자 정보 및 기본 설정
$ git config --list
credential.helper=osxkeychain
core.repositoryformatversion=0
core.filemode=true
core.bare=false
core.logallrefupdates=true
core.ignorecase=true
core.precomposeunicode=true
pull.rebase=false
remote.origin.url=https://github.com/renoirk/ia-codyssey.git
remote.origin.fetch=+refs/heads/*:refs/remotes/origin/*

### 2). GitHub 저장소 연동 확인
$ git remote -v
origin	https://github.com/renoirk/ia-codyssey.git (fetch)
origin	https://github.com/renoirk/ia-codyssey.git (push)

### 3). 연동 증거
* GitHub 저장소 URL: https://github.com/renoirk/ia-codyssey
* 로컬 작업 디렉토리와 원격 저장소가 성공적으로 연결되어 push/pull이 가능한 상태입니다.














### 터미널 실행 로그
```bash
pwd
/Users/renoirk9330/ia-codyssey/mission1
ls -al
total 8
drwxr-xr-x  3 renoirk9330  renoirk9330   96  7 30 16:11 .
drwxr-xr-x  5 renoirk9330  renoirk9330  160  7 30 15:59 ..
-rw-r--r--  1 renoirk9330  renoirk9330   55  7 30 16:11 mission_check.txt
renoirk9330@c6r7s1 mission1 % code readme.md
renoirk9330@c6r7s1 mission1 % touch sample.txt
renoirk9330@c6r7s1 mission1 % cat sample.txt
renoirk9330@c6r7s1 mission1 % cp sample.txt sample.txt
cp: sample.txt and sample.txt are identical (not copied).
renoirk9330@c6r7s1 mission1 % cp sample.txt sample_copy.txt
renoirk9330@c6r7s1 mission1 % mv sample_copy.txt renamed.txt
renoirk9330@c6r7s1 mission1 % rm renamed.txt
renoirk9330@c6r7s1 mission1 % cp sample.txt sample_copy.txt 
renoirk9330@c6r7s1 mission1 % ls
mission_check.txt	sample_copy.txt		sample.txt
renoirk9330@c6r7s1 mission1 % mv sample_copy.txt renamed.txt
renoirk9330@c6r7s1 mission1 % ls                            
mission_check.txt	renamed.txt		sample.txt
renoirk9330@c6r7s1 mission1 % rm renamed.txt                
renoirk9330@c6r7s1 mission1 % ls            
mission_check.txt	sample.txt
renoirk9330@c6r7s1 mission1 % ls -l sample.txt
-rw-r--r--  1 renoirk9330  renoirk9330  0  7 30 17:18 sample.txt
renoirk9330@c6r7s1 mission1 % chmod 400 sample.txt
renoirk9330@c6r7s1 mission1 % ls -l sample.txt    
-r--------  1 renoirk9330  renoirk9330  0  7 30 17:18 sample.txt
renoirk9330@c6r7s1 mission1 % 
renoirk9330@c6r7s1 mission1 % mkdir test_dir
renoirk9330@c6r7s1 mission1 % ls -ld test_dir
drwxr-xr-x  2 renoirk9330  renoirk9330  64  7 30 17:31 test_dir
renoirk9330@c6r7s1 mission1 % chmod 700 test_dir
renoirk9330@c6r7s1 mission1 % ls -id test_dir
3440697 test_dir
renoirk9330@c6r7s1 mission1 % ls -ld test_dir
drwx------  2 renoirk9330  renoirk9330  64  7 30 17:31 test_dir
renoirk9330@c6r7s1 mission1 % git --version
\git version 2.53.0
renoirk9330@c6r7s1 mission1 % docker --version
zsh: command not found: docker
renoirk9330@c6r7s1 mission1 % 
renoirk9330@c6r7s1 mission1 % git add readme.md
renoirk9330@c6r7s1 mission1 % git commit -m "docs: README.md 작성_환경정보"
[main d51aa51] docs: README.md 작성_환경정보
 1 file changed, 43 insertions(+)
 create mode 100644 mission1/readme.md
renoirk9330@c6r7s1 mission1 % git push origin main
오브젝트 나열하는 중: 6, 완료.
오브젝트 개수 세는 중: 100% (6/6), 완료.
Delta compression using up to 6 threads
오브젝트 압축하는 중: 100% (4/4), 완료.
오브젝트 쓰는 중: 100% (4/4), 949 bytes | 949.00 KiB/s, 완료.
Total 4 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/renoirk/ia-codyssey.git
   4a772e7..d51aa51  main -> main
renoirk9330@c6r7s1 mission1 % clear

$sw_vers
ProductName:		macOS
ProductVersion:		15.7.4
BuildVersion:		24G517

$echo $SHELL
/bin/zsh
$echo $0
-zsh
$echo $TERM_PROGRAM
Apple_Terminal


renoirk9330@c6r7s1 mission1 % git add README.md
renoirk9330@c6r7s1 mission1 % git commit -m "docs: 개발 환경 정보 (OS, Shell, Git) 추가"

renoirk9330@c6r7s1 mission1 % git add .
renoirk9330@c6r7s1 mission1 % git status

현재 브랜치 main
브랜치가 'origin/main'에 맞게 업데이트된 상태입니다.

커밋할 변경 사항:
  (use "git restore --staged <file>..." to unstage)
	수정함:        readme.md
	새 파일:       sample.txt

renoirk9330@c6r7s1 mission1 % git commit -m "docs: 개발 환경 정보 추가"                 
[main 7bce5d5] docs: 개발 환경 정보 추가
 2 files changed, 114 insertions(+), 6 deletions(-)
 create mode 100644 mission1/sample.txt
renoirk9330@c6r7s1 mission1 % git push origin main
오브젝트 나열하는 중: 8, 완료.
오브젝트 개수 세는 중: 100% (8/8), 완료.
Delta compression using up to 6 threads
오브젝트 압축하는 중: 100% (4/4), 완료.
오브젝트 쓰는 중: 100% (5/5), 2.07 KiB | 2.07 MiB/s, 완료.
Total 5 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/renoirk/ia-codyssey.git
   d51aa51..7bce5d5  main -> main
renoirk9330@c6r7s1 mission1 % 


renoirk9330@c6r7s1 mission1 % 

$docker --version
Docker version 28.5.2, build ecc6942
$docker info      
Client:
 Version:    28.5.2
 Context:    orbstack
 Debug Mode: false
 Plugins:
  buildx: Docker Buildx (Docker Inc.)
    Version:  v0.29.1
    Path:     /Users/renoirk9330/.docker/cli-plugins/docker-buildx
  compose: Docker Compose (Docker Inc.)
    Version:  v2.40.3
    Path:     /Users/renoirk9330/.docker/cli-plugins/docker-compose

Server:
 Containers: 0
  Running: 0
  Paused: 0
  Stopped: 0
 Images: 0
 Server Version: 28.5.2
 Storage Driver: overlay2
  Backing Filesystem: btrfs
  Supports d_type: true
  Using metacopy: false
  Native Overlay Diff: true
  userxattr: false
 Logging Driver: json-file
 Cgroup Driver: cgroupfs
 Cgroup Version: 2
 Plugins:
  Volume: local
  Network: bridge host ipvlan macvlan null overlay
  Log: awslogs fluentd gcplogs gelf journald json-file local splunk syslog
 CDI spec directories:
  /etc/cdi
  /var/run/cdi
 Swarm: inactive
 Runtimes: io.containerd.runc.v2 runc
 Default Runtime: runc
 Init Binary: docker-init
 containerd version: 1c4457e00facac03ce1d75f7b6777a7a851e5c41
 runc version: d842d7719497cc3b774fd71620278ac9e17710e0
 init version: de40ad0
 Security Options:
  seccomp
   Profile: builtin
  cgroupns
 Kernel Version: 6.17.8-orbstack-00308-g8f9c941121b1
 Operating System: OrbStack
 OSType: linux
 Architecture: x86_64
 CPUs: 6
 Total Memory: 15.67GiB
 Name: orbstack
 ID: 1f348cf6-fba5-4676-8222-be1d259985e2
 Docker Root Dir: /var/lib/docker
 Debug Mode: false
 Experimental: false
 Insecure Registries:
  ::1/128
  127.0.0.0/8
 Live Restore Enabled: false
 Product License: Community Engine
 Default Address Pools:
   Base: 192.168.97.0/24, Size: 24
   Base: 192.168.107.0/24, Size: 24
   Base: 192.168.117.0/24, Size: 24
   Base: 192.168.147.0/24, Size: 24
   Base: 192.168.148.0/24, Size: 24
   Base: 192.168.155.0/24, Size: 24
   Base: 192.168.156.0/24, Size: 24
   Base: 192.168.158.0/24, Size: 24
   Base: 192.168.163.0/24, Size: 24
   Base: 192.168.164.0/24, Size: 24
   Base: 192.168.165.0/24, Size: 24
   Base: 192.168.166.0/24, Size: 24
   Base: 192.168.167.0/24, Size: 24
   Base: 192.168.171.0/24, Size: 24
   Base: 192.168.172.0/24, Size: 24
   Base: 192.168.181.0/24, Size: 24
   Base: 192.168.183.0/24, Size: 24
   Base: 192.168.186.0/24, Size: 24
   Base: 192.168.207.0/24, Size: 24
   Base: 192.168.214.0/24, Size: 24
   Base: 192.168.215.0/24, Size: 24
   Base: 192.168.216.0/24, Size: 24
   Base: 192.168.223.0/24, Size: 24
   Base: 192.168.227.0/24, Size: 24
   Base: 192.168.228.0/24, Size: 24
   Base: 192.168.229.0/24, Size: 24
   Base: 192.168.237.0/24, Size: 24
   Base: 192.168.239.0/24, Size: 24
   Base: 192.168.242.0/24, Size: 24
   Base: 192.168.247.0/24, Size: 24
   Base: fd07:b51a:cc66:d000::/56, Size: 64

WARNING: DOCKER_INSECURE_NO_IPTABLES_RAW is set
renoirk9330@c6r7s1 mission1 % 

renoirk9330@c6r7s1 mission1 % docker run hello-world
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
4f55086f7dd0: Pull complete 
Digest: sha256:c3cbe1cc1aa588a64951ac6286e0df7b27fe2e6324b1001c619bb358770c0178
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/

renoirk9330@c6r7s1 mission1 % docker run -d -p 8080:80 --name my-web nginx
docker: Error response from daemon: Conflict. The container name "/my-web" is already in use by container "d5882f1b2fe4f633d1dc9cf37f8137d255e26f358edbac41a1e84fd922fe7db0". You have to remove (or rename) that container to be able to reuse that name.

Run 'docker run --help' for more information
renoirk9330@c6r7s1 mission1 % docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
renoirk9330@c6r7s1 mission1 % docker ps -a                                
CONTAINER ID   IMAGE         COMMAND                   CREATED          STATUS                      PORTS     NAMES
ef0752e80ea8   hello-world   "/hello"                  8 minutes ago    Exited (0) 8 minutes ago              zealous_diffie
d5882f1b2fe4   nginx         "/docker-entrypoint.…"   38 minutes ago   Exited (0) 38 minutes ago             my-web
renoirk9330@c6r7s1 mission1 % docker rm my-web
my-web
renoirk9330@c6r7s1 mission1 % docker run -d -p 8080:80 --name my-web nginx
6851386810e6cbe42ae6afdd8a1f352b25b342ca1335403bf1ded1df72287870
renoirk9330@c6r7s1 mission1 % ç

---

## 🛠 Git 설정 및 GitHub 연동 기록

### 1. Git 사용자 정보 및 기본 설정
```bash
# git config --list 실행 결과 (주요 설정)

```

### 2. GitHub 저장소 연동 확인
```bash
# git remote -v 실행 결과
origin	https://github.com/renoirk/ia-codyssey.git (fetch)
origin	https://github.com/renoirk/ia-codyssey.git (push)
```

### 3. 연동 증거
* GitHub 저장소 URL: https://github.com/renoirk/ia-codyssey
* 로컬 작업 디렉토리와 원격 저장소가 성공적으로 연결되어 push/pull이 가능한 상태입니다.

