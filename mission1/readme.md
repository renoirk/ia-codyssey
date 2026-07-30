
```bash
### 1. 개발 환경 정보
- **OS**: macOS 15.7.4 24G517
- **Shell**: /bin/zsh
- **Terminal**: Apple_Terminal
- **Git Version**: git version 2.53.0
- **Docker Version**: Docker version 28.5.2, build ecc6942

git --version
\git version 2.53.0

### 2. 수행 체크리스트
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

