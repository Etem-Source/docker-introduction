REM Sécurité : aucun montage de /var/run/docker.sock dans le conteneur

docker rm -f quiz-step4
docker run -d --name quiz-secure -p 8092:8080 ^
  --memory="128m" ^
  --cpus="0.5" ^
  --pids-limit=50 ^
  --read-only ^
  --security-opt no-new-privileges:true ^
  --cap-drop ALL ^
  quiz-docker:step4