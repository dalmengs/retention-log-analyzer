# base image
FROM python:3.10.13-slim-bookworm

# work directory setting
WORKDIR /usr/src/app

# copy project file
COPY . .

# install env
RUN pip install -r requirements.txt

# port open
EXPOSE 9999

# set env file and run server
RUN chmod +x ./entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]