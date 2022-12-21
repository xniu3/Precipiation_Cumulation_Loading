# Install crontabs
RUN yum -y install crontabs
# Pull, clone and set work directory
WORKDIR /data
RUN git clone https://github.com/********.git /data/app
WORKDIR /data/app
RUN pip install -r requirements.txt
# Execute on 8:30 AM everyday
RUN echo "30 8 * * * python /data/app/Integration.py" >> /var/spool/cron/root
# Launch crond
CMD /usr/sbin/crond -i && python3 Integration.py