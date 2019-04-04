FROM mysql:8

COPY masterdatasql/masterdata.sql /docker-entrypoint-initdb.d

ENV MYSQL_ROOT_PASSWORD sb
ENV MYSQL_DATABASE MasterData
ENV MYSQL_USER reader
ENV MYSQL_PASSWORD reader
