# ia-codyssey
Github과 Codyssey를 연동하기 위해 만들어진 Repository 입니다.

## 📝 Mission 9: Docker 볼륨 영속성 검증 (Persistence Test)

### 1. 개요
Docker 컨테이너는 삭제되면 내부의 데이터도 함께 사라지는 휘발성 특징을 가지고 있습니다. 이를 해결하기 위해 **Docker Volume**을 사용하여 컨테이너가 삭제되어도 데이터가 안전하게 유지(영속성)되는지 검증합니다.

### 2. 검증 단계 및 명령어

#### Step 1: 볼륨을 연결하여 컨테이너 실행
`my-db-data`라는 이름의 볼륨을 생성함과 동시에 컨테이너의 `/app/data` 경로에 마운트합니다.
```bash
docker run -d -p 8080:5000 -v my-db-data:/app/data --name web-server my-web-app
```

#### Step 2: 데이터 생성 (Write)
실행 중인 컨테이너 내부의 볼륨 경로에 테스트 파일을 생성합니다.
```bash
docker exec web-server sh -c "echo 'Docker Volume Success!' > /app/data/test.txt"
```

#### Step 3: 컨테이너 삭제 (Destroy)
현재 실행 중인 컨테이너를 강제로 삭제하여 데이터 휘발 여부를 확인하기 전 단계로 진입합니다.
```bash
docker rm -f web-server
```

#### Step 4: 새 컨테이너에서 볼륨 재연결 (Restore)
동일한 볼륨(`my-db-data`)을 사용하여 새로운 컨테이너를 다시 실행합니다.
```bash
docker run -d -p 8080:5000 -v my-db-data:/app/data --name web-server my-web-app
```

#### Step 5: 데이터 유지 확인 (Verify)
새로운 컨테이너에서 이전 컨테이너가 생성했던 파일이 그대로 존재하는지 확인합니다.
```bash
docker exec web-server cat /app/data/test.txt
```

### 3. 결과
- **출력 내용:** `Docker Volume Success!`
- **결론:** 컨테이너를 삭제하고 새로 생성했음에도 불구하고, 볼륨에 저장된 데이터는 삭제되지 않고 유지됨을 확인하였습니다.
