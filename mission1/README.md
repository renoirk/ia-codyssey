# ia-codyssey Mission 1

## 1. 프로젝트 개요
본 프로젝트는 개발자로서 필수적인 리눅스 CLI, Docker, Git/GitHub의 기본 사용법을 익히고, 이를 활용해 로컬 개발 환경을 세팅하는 미션입니다. 터미널 제어, 도커 컨테이너 및 볼륨 관리, 커스텀 이미지 빌드, Git을 활용한 버전 관리 등을 실습하며 **"재현 가능한 개발 워크스테이션 구축"**을 목표로 합니다.

## 2. 개발 환경 정보
- **OS**: macOS 15.7.4 24G517
- **Shell**: /bin/zsh
- **Terminal**: Apple_Terminal
- **Git Version**: git version 2.53.0
- **Docker Version**: Docker version 28.5.2, build ecc6942

## 3. 수행 체크리스트 
- [x] 터미널 기본 조작 및 폴더 구성
- [x] 권한 변경 실습
- [x] Docker 설치/점검
- [x] hello-world 실행
- [x] Dockerfile 빌드/실행 (커스텀 이미지)
- [x] 포트 매핑 접속
- [x] 바인드 마운트 반영 / 볼륨 영속성 검증
- [x] Git 설정 + VSCode GitHub 연동

---

## 4. 터미널 조작 및 권한 실습 로그

### 1) 현재 위치 및 목록 확인
```bash
pwd
/Users/renoirk9330/ia-codyssey/mission1
ls -al
total 8
drwxr-xr-x  3 renoirk9330  renoirk9330   96  7 30 16:11 .
drwxr-xr-x  5 renoirk9330  renoirk9330  160  7 30 15:59 ..
-rw-r--r--  1 renoirk9330  renoirk9330   55  7 30 16:11 mission_check.txt

```

### 2) 파일 생성 및 내용 확인

```bash
touch sample.txt
cat sample.txt

```

### 3) 복사, 이름 변경, 삭제

```bash
cp sample.txt sample_copy.txt 
ls
mission_check.txt	sample_copy.txt		sample.txt
mv sample_copy.txt renamed.txt
ls                            
mission_check.txt	renamed.txt		sample.txt
rm renamed.txt                
ls            
mission_check.txt	sample.txt

```

### 4) 권한 실습  (chmod [소유자,그룹,기타], r/w/x:4/2/1)

```bash
ls -l sample.txt
-rw-r--r--  1 renoirk9330  renoirk9330  0  7 30 17:18 sample.txt

# 권한 변경 (나만 읽기)
chmod 400 sample.txt 
ls -l sample.txt    
-r--------  1 renoirk9330  renoirk9330  0  7 30 17:18 sample.txt

# 디렉토리 권한 변경 (나만 접근 가능)
mkdir test_dir
ls -ld test_dir
drwxr-xr-x  2 renoirk9330  renoirk9330  64  7 30 17:31 test_dir
chmod 700 test_dir 
ls -ld test_dir
drwx------  2 renoirk9330  renoirk9330  64  7 30 17:31 test_dir

```

---

## 5. Docker 설치 및 기본 운영

### 1) Docker 설치 점검

```bash
docker --version
Docker version 28.5.2, build ecc6942

docker info
# OrbStack 기반 Docker Engine 정상 동작 확인
# Server Version: 28.5.2
# Operating System: OrbStack
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

```

### 2) 이미지 관리 및 컨테이너 실행

```bash
# 이미지 다운로드
docker pull nginx

# 다운로드된 도커 이미지 목록 확인
docker images
REPOSITORY   TAG       IMAGE ID       CREATED       SIZE
nginx        latest    a6bd71f48f68   1 weeks ago   187MB

# 다운로드한 이미지 실행
docker run -d --name my-web nginx

# 컨테이너 로그 및 리소스 확인
docker logs my-web
docker stats --no-stream

# 전체 컨테이너 목록(중지된 컨테이너 포함) 확인
docker ps -a
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS     NAMES
abc123def456   nginx     "/docker-entrypoint.…"   10 minutes ago   Up 10 minutes   80/tcp    my-web

# 컨테이너 중지 및 삭제
docker stop my-web
my-web
docker rm my-web
my-web
```

### 3) hello-world 및 ubuntu 테스트

```bash
# hello-world
docker run hello-world
Hello from Docker!

# ubuntu 접속 테스트
docker run -it ubuntu /bin/bash
root@792e4a08e15d:/# echo "Hello from Ubuntu Container!"

```

* **컨테이너 종료/유지(attach/exec) 차이:**
* `exit`: 컨테이너 내부 쉘을 종료하며 컨테이너 정지.
* `Ctrl + P, Q`: 컨테이너를 정지시키지 않고 백그라운드로 빠져나옴.
* `attach`: 실행 중인 컨테이너의 메인 프로세스(PID 1)에 접속.
* `exec`: 실행 중인 컨테이너에 새로운 프로세스를 실행.



---

## 6. Docker 커스텀 이미지 제작 및 배포 (포트 매핑)

### 1) 프로젝트 구조 및 파일

```text
my-web-app/
├── app/
│   └── main.py       # Flask 웹 애플리케이션 소스
└── Dockerfile        # Docker 이미지 빌드 설정 파일

```

**app/main.py**

```python
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return '<h1>Docker Web Server Success!</h1>'
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

```

**Dockerfile**

```dockerfile
FROM python:3.9-slim
WORKDIR /app
RUN pip install flask
COPY ./app /app
CMD ["python", "main.py"]

```

### 2) 빌드 및 포트 매핑 실행

```bash
# 이미지 빌드
docker build -t my-web-server .

# 컨테이너 실행 (포트 포워딩 8080 -> 5000)
docker run -d -p 8080:5000 --name my-running-app my-web-server

# 접속 확인
curl http://localhost:8080
<h1>Docker Web Server Success!</h1>

```
---

## 7. Docker 볼륨 영속성 검증

1. **볼륨을 연결하여 컨테이너 실행**
```bash
docker run -d -p 8080:5000 -v my-db-data:/app/data --name web-server my-web-app

```


2. **데이터 생성**
```bash
docker exec web-server sh -c "echo 'Docker Volume Success!' > /app/data/test.txt"

```


3. **컨테이너 삭제 (Destroy)**
```bash
docker rm -f web-server

```


4. **새 컨테이너에서 볼륨 재연결 (Restore)**
```bash
docker run -d -p 8080:5000 -v my-db-data:/app/data --name web-server my-web-app

```


5. **데이터 유지 확인 (Verify)**
```bash
docker exec web-server cat /app/data/test.txt
# 출력: Docker Volume Success!

```

* **결론:** 컨테이너를 삭제하고 새로 생성했음에도 볼륨에 저장된 데이터는 삭제되지 않고 유지됨.

---

6. **바인드 마운트(Bind Mount) 및 볼륨 백업/복원**
```bash
#바인드마운트
docker run -d -p 8080:5000 -v $(pwd)/local_data:/app/data --name web-server my-web-app

#볼륨 데이터 백업
(임시 컨테이너(alpine)를 실행하여 my-db-data 볼륨 내부의 데이터를 호스트의 현재 경로에 backup.tar 파일로 백업)
docker run --rm -v my-db-data:/volume -v $(pwd):/backup alpine tar cvf /backup/backup.tar -C /volume .

#볼륨 데이터 복원(Restore)
docker run --rm -v my-db-data:/volume -v $(pwd):/backup alpine tar xvf /backup/backup.tar -C /volume
```
---

## 8. Git 설정 및 GitHub 연동 기록

```bash
# 사용자 및 기본 설정 확인
git config --list
# remote.origin.url=[https://github.com/renoirk/ia-codyssey.git](https://github.com/renoirk/ia-codyssey.git) 확인 완료

# GitHub 저장소 연동 확인
git remote -v
origin	[https://github.com/renoirk/ia-codyssey.git](https://github.com/renoirk/ia-codyssey.git) (fetch)
origin	[https://github.com/renoirk/ia-codyssey.git](https://github.com/renoirk/ia-codyssey.git) (push)

# GitHub 원격 저장소로 푸시(Publish) 성공 로그
git push origin main
# Enumerating objects: 5, done.
# Counting objects: 100% (5/5), done.
# Delta compression using up to 6 threads
# Compressing objects: 100% (3/3), done.
# Writing objects: 100% (3/3), 987 bytes | 987.00 KiB/s, done.
# Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
# To [https://github.com/renoirk/ia-codyssey.git](https://github.com/renoirk/ia-codyssey.git)
#    d3b0738..f9a531b  main -> main
```

* **연동 증거:** 로컬 작업 디렉토리와 원격 저장소(`https://github.com/renoirk/ia-codyssey`)가 성공적으로 연결되어 push/pull 확인.

---

## 9. 트러블슈팅

### 1) 컨테이너 이름 충돌 오류

* **문제:** `docker run -d -p 8080:80 --name my-web nginx` 명령어를 실행했을 때 `Error response from daemon: Conflict. The container name "/my-web" is already in use...` 에러가 발생함.
* **원인 가설:** 이전에 동일한 이름(`my-web`)으로 컨테이너를 실행했다가 중지(Stop)시켰으나, 컨테이너 객체가 삭제되지 않고 백그라운드에 남아있어서 새 컨테이너 생성 시 이름이 충돌했을 것이다.
* **확인:** `docker ps -a` 명령어로 확인한 결과, `my-web` 이름의 컨테이너가 Exited 상태로 존재함을 확인함.
* **해결:** `docker rm my-web` 명령어로 기존에 멈춰있는 컨테이너를 완전히 삭제한 뒤, 다시 `run` 명령어를 실행하여 정상 작동을 확인.

### 2) 파일 권한 부족으로 인한 접근 거부 (Permission Denied)

* **문제:** 권한 실습 중에 `sample.txt`를 `chmod 400`으로 변경 후, 테스트를 위해 텍스트를 추가하려고 `echo "test" > sample.txt`를 입력했더니 `Permission denied`가 뜸.
* **원인 가설:** `chmod 400`은 소유자에게 '읽기(r)' 권한만 주고 '쓰기(w)' 권한을 박탈했으므로, 파일 내용을 수정하거나 덮어쓰는 것이 시스템 상에서 차단되었을 것이다.
* **확인:** `ls -l sample.txt`로 `-r--------` 권한 상태임을 재확인.
* **대안/해결:** 쓰기 테스트를 위해 `chmod 600 sample.txt`로 소유자 쓰기 권한을 부여한 후 다시 시도하여 성공함.

### 3) 포트 충돌 진단
* **문제:** 컨테이너 실행 시 특정 포트(예: 8080)가 이미 사용 중이라는 포트 충돌 에러가 발생함.

* **확인:** lsof 또는 netstat  명령어 사용하여 포트,프로세스 확인
lsof -i :8080
netstat -an | grep 8080
* **해결:** :  프로세스 종료 (kill) 또는 포트 변경 (예: 8081). 
kill -9 8080
docker run -d -p 8081:5000 -v my-db-data:/app/data --name web-server my-web-app

---

## 10. 미션 핵심 개념 정리 (과제 목표 달성)

1. **절대 경로와 상대 경로의 차이:**
* 절대 경로는 디렉토리 트리의 가장 최상단인 루트(`/`)부터 목적지까지의 전체 경로를 의미합니다. (예: `/Users/renoirk9330/ia-codyssey/mission1`)
* 상대 경로는 현재 내가 위치한 디렉토리를 기준으로 한 목적지까지의 경로입니다. (예: `./mission1` 또는 `../test_dir`)
상황별 권장안: Docker 환경에서 호스트(내 컴퓨터)의 디렉터리를 마운트할 때는 다른 사람의 환경에서도 동일하게 동작(재현성 확보)할 수 있도록 현재 위치를 나타내는 상대 경로(예: $(pwd))를 활용하는 것이 좋습니다. 반면, 컨테이너 내부 환경이나 Dockerfile 내에서 작업 디렉터리를 지정할 때는 위치 혼동을 방지하기 위해 명확한 절대 경로(예: /app)를 사용하는 것을 권장합니다.

2. **파일 권한(r/w/x)과 755, 644 해석:**
* r(읽기=4), w(쓰기=2), x(실행=1)을 뜻하며, 세 자리는 각각 소유자(User), 그룹(Group), 기타(Others)의 권한 합입니다.
* `755`: 소유자는 읽기/쓰기/실행(4+2+1=7), 그룹과 기타는 읽기/실행(4+1=5) 권한. (보통 디렉토리에 많이 쓰임)
* `644`: 소유자는 읽기/쓰기(4+2=6), 그룹과 기타는 읽기(4) 권한. (보통 파일에 많이 쓰임)


3. **포트 매핑이 필요한 이유:**
* 컨테이너는 호스트(내 컴퓨터)와 독립된 격리 네트워크 공간을 사용합니다. 외부에서 브라우저 등을 통해 컨테이너 안에서 도는 웹서버에 접속하려면, 내 컴퓨터의 특정 포트로 들어오는 요청을 컨테이너 내부의 포트로 연결(포워딩)해 주어야만 통신이 가능하기 때문입니다. 또한, 보안상 필요한 포트(예: 80, 443)만 선별적으로 매핑하여 외부에 노출되는 포트를 최소화하는 것이 권장됩니다.


4. **Docker 볼륨 (영속 데이터):**
* 기본적으로 Docker 컨테이너 내부에서 생성된 데이터는 컨테이너가 삭제될 때 함께 증발(휘발성)합니다. DB 데이터처럼 컨테이너 생명주기와 상관없이 데이터를 안전하고 영구적으로 보존하기 위해 호스트 PC의 저장 공간과 마운트하는 것이 Docker 볼륨입니다.


5. **Git과 GitHub의 역할 차이:**
* **Git:** 내 로컬 컴퓨터 환경에서 파일의 변경 이력을 추적하고 버전 관리를 수행하는 시스템 도구입니다.
* **GitHub:** Git으로 관리되는 로컬 저장소들을 인터넷 클라우드 상에 백업하고, 다른 사람들과 코드 리뷰 및 병합 등 원격 협업을 가능하게 해주는 호스팅 플랫폼 서비스입니다.




```

```
