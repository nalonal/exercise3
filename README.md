## INSTALASI
git clone https://github.com/nalonal/exercise3<br>
sudo chmod 777 -R exercise3<br>
cd exercise3<br>
chmod u+x install.sh<br>
./install.sh<br><br>

**----Setting file .env----**<br>
nano .env<br>
ganti IP_PUBLIC_EXTERNAL = "localhost" dengan IP Public anda<br>

## STARTING
docker compose up -d

## SETELAH HABIS REBOOT/SHUTDOWN LINUX MACHINE
sudo chmod 666 /var/run/docker.sock