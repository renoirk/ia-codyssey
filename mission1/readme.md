
```bash
### 1. 개발 환경 정보
- **OS**: macOS 15.7.4 24G517
- **Shell**: /bin/zsh
- **Terminal**: Apple_Terminal
- **Git Version**: git version 2.53.0
- **Docker Version**: Docker version XXXXXXX ( 설치 후 작성)

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

### 2). 파일 생성 및 내용 확인
touch sample.txt
cat sample.txt

### 3). 복사, 이름 변경, 삭제
cp sample.txt sample_copy.txt 
ls
mission_check.txt	sample_copy.txt		sample.txt
mv sample_copy.txt renamed.txt
ls                            
mission_check.txt	renamed.txt		sample.txt
rm renamed.txt                
ls            
mission_check.txt	sample.txt

### 4). 권한 실습 (chmod [소유자,그룹,기타], r/w/x:4/2/1)
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

renoirk9330@c6r7s1 mission1 % sw_vers
ProductName:		macOS
ProductVersion:		15.7.4
BuildVersion:		24G517
renoirk9330@c6r7s1 mission1 % systeminfo |findstr /B /C:"OS Name" /C: "OS Version"
zsh: command not found: systeminfo
zsh: command not found: findstr
renoirk9330@c6r7s1 mission1 % echo $SHELL
/bin/zsh
renoirk9330@c6r7s1 mission1 % echo $0
-zsh
renoirk9330@c6r7s1 mission1 % echo $TERM_PROGRAM
Apple_Terminal
renoirk9330@c6r7s1 mission1 % git add README.md
renoirk9330@c6r7s1 mission1 % git commit -m "docs: 개발 환경 정보 (OS, Shell, Git) 추가"
현재 브랜치 main
브랜치가 'origin/main'에 맞게 업데이트된 상태입니다.

커밋하도록 정하지 않은 변경 사항:
  (무엇을 커밋할지 바꾸려면 "git add <파일>..."을 사용하십시오)
  (use "git restore <file>..." to discard changes in working directory)
	수정함:        readme.md

추적하지 않는 파일:
  (커밋할 사항에 포함하려면 "git add <파일>..."을 사용하십시오)
	sample.txt

커밋할 변경 사항을 추가하지 않았습니다 ("git add" 및/또는 "git commit -a"를
사용하십시오)
renoirk9330@c6r7s1 mission1 % git push origin main
Everything up-to-date
renoirk9330@c6r7s1 mission1 % 
