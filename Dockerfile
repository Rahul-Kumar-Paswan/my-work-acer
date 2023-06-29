FROM python
WORKDIR /app
COPY ./My-Python-Project/* /app
RUN pip install -r requirements.txt
CMD ["python","main.py"]