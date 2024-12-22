FROM minio/minio:latest

ENV MINIO_ROOT_USER="Sk1B1D33"
ENV MINIO_ROOT_PASSWORD="T01L3T-S4N"

CMD ["server", "/data", "--console-address", ":9001"]