FROM python:3
ADD . /web
WORKDIR /web
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["/web/run.py"]