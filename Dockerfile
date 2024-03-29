FROM python:3.10-slim
WORKDIR /app
ADD . ./

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt \
    && rm -rf requirements.txt

# Default port for Azure Web App for containers is 80
# Please note that port and serverPort in the config.toml file
# should correspond to the exposed port
EXPOSE 80

RUN mkdir ~/.streamlit
RUN cp .streamlit/config.prod.toml ~/.streamlit/config.toml
RUN cp .streamlit/credentials.prod.toml ~/.streamlit/credentials.toml
WORKDIR /app

ENTRYPOINT ["streamlit", "run"]
CMD ["src/app.py"]
