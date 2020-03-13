debugging with gdb
nc -l 9091 to start server- long running process emulation

gdb python 2167(process id)
sudo apt-get install python3-dbg python3-dev
pip install py-bt
zcat /usr/share/doc/python3.6/gdbinit.gz >> ~/.gdbinit

gdb -p <Processid>
py-bt
