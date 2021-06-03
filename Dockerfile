FROM python:rc
RUN mkdir /app
WORKDIR /app
ADD requirements-v2.txt /app
ADD main.py /app
RUN pip3 install -r requirements.txt
CMD ["gunicorn", "-w 4" , "-b", "0.0.0.0:8000", "main:app"]