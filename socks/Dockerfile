FROM ipython/ipython

EXPOSE 9999

RUN python3 -m pip install pandas

RUN apt-get install -y libfreetype6-dev
RUN python3 -m pip install matplotlib
WORKDIR /root/notebooks/socks

CMD ip="$(ifconfig | grep -A 1 'eth0' | tail -1 | cut -d ':' -f 2 | cut -d ' ' -f 1)" && ipython notebook --ip $ip --port 9999
