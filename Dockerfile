FROM python:3.9.9
EXPOSE 8080
RUN pip3 install Django Pillow
WORKDIR /app 
COPY ./app /app
ENTRYPOINT ["python3"] 
CMD ["manage.py", "runserver", "0.0.0.0:8080"]