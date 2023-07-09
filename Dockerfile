# FROM python
# WORKDIR /app
# COPY . /app
# RUN pip install -r requirements.txt
# EXPOSE  3000
# CMD ["python", "-m" ,"project_package.main"]

# FROM python
# # RUN python setup.py sdist bdist_wheel
# WORKDIR /app
# COPY ./dist/project_package-1.0.0.tar.gz /app
# # RUN pip install -r requirements.txt
# RUN cd /dist
# RUN pip install project_package-1.0.0.tar.gz
# EXPOSE  3000
# CMD ["python", "-m" ,"project_package.main"]


# # Base image
# FROM python

# # Set the working directory inside the container
# WORKDIR /app

# # Copy the tar file into the container
# COPY ./dist/project_package-1.0.0.tar.gz .

# # Extract the contents of the tar file
# RUN tar -xzvf project_package-1.0.0.tar.gz

# # Change the working directory to the extracted project directory
# WORKDIR /app/my_project

# # Install any required dependencies (if applicable)
# # RUN pip install -r requirements.txt

# # Define the command to run your Python project
# CMD ["python", "-m" ,"project_package.main"]


FROM python
COPY . /app
WORKDIR /app
RUN python setup.py sdist bdist_wheel
RUN pip install -r requirements.txt
WORKDIR /app/dist
RUN pip install project_package-1.2.1.tar.gz
RUN pip install project_package-1.2.1-py3-none-any.whl
WORKDIR /app
EXPOSE  3000
CMD ["python", "-m" ,"project_package.main"]

# FROM python
# WORKDIR /app
# COPY . /app
# RUN pip install -r requirements.txt
# EXPOSE  3000
# # CMD ["python","main.py"]
# CMD ["python", "-m" ,"project_package.main"]

# Base image
# FROM python
# WORKDIR /app
# COPY dist/project_package-1.0.0-py3-none-any.whl .
# RUN pip install project_package-1.0.0-py3-none-any.whl
# EXPOSE  3000
# CMD ["python", "-m" ,"project_package.main"]


