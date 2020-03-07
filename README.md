# PythonProject
Python Apps




Memo:

cd /home/seluser/selenium

sudo apt update
sudo apt install build-essential libbz2-dev libdb-dev \
  libreadline-dev libffi-dev libgdbm-dev liblzma-dev \
  libncursesw5-dev libsqlite3-dev libssl-dev \
  zlib1g-dev uuid-dev tk-dev

wget https://www.python.org/ftp/python/3.8.2/Python-3.8.2.tgz
tar xzf Python-3.8.2.tgz

cd Python-3.8.2
./configure --enable-shared
make
sudo make install
sudo sh -c "echo '/usr/local/lib' > /etc/ld.so.conf.d/custom_python3.conf"
sudo ldconfig

curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
~/.local/bin/pip install selenium
~/.local/bin/pip install retrying
~/.local/bin/pip install pyppeteer

sudo rm -rf /home/seluser/selenium/Python-3.8.2*
