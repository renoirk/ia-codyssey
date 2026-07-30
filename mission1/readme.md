
```bash
### 1. 현재 위치 및 목록 확인
pwd
/Users/renoirk9330/ia-codyssey/mission1
ls -al
total 8
drwxr-xr-x  3 renoirk9330  renoirk9330   96  7 30 16:11 .
drwxr-xr-x  5 renoirk9330  renoirk9330  160  7 30 15:59 ..
-rw-r--r--  1 renoirk9330  renoirk9330   55  7 30 16:11 mission_check.txt

### 2. 파일 생성 및 내용 확인
touch sample.txt
cat sample.txt

### 3. 복사, 이름 변경, 삭제
cp sample.txt sample_copy.txt 
ls
mission_check.txt	sample_copy.txt		sample.txt
mv sample_copy.txt renamed.txt
ls                            
mission_check.txt	renamed.txt		sample.txt
rm renamed.txt                
ls            
mission_check.txt	sample.txt

### 권한 실습 (chmod [소유자,그룹,기타], r/w/x:4/2/1)
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

### 환경 버전 확인 (Git, Docker)
git --version
\git version 2.53.0

