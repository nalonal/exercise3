## INSTALASI
git clone https://github.com/nalonal/exercise3<br>
chmod 777 exercise3<br>
cd exercise3<br>
chmod u+x install.sh<br>
./install.sh<br>
Buka file .env -> ganti IP_PUBLIC_EXTERNAL = "localhost" dengan IP Public anda<br>

## STARTING
docker compose up -d

## SETELAH HABIS REBOOT/SHUTDOWN LINUX MACHINE
sudo chmod 666 /var/run/docker.sock