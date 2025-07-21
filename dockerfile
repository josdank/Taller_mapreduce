FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN chmod +x mapper.py reducer.py split_logs.sh
CMD ["/bin/bash"]
