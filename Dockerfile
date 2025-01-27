FROM ubuntu:22.04

RUN apt-get update && DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt-get install -y \
      python3 python3-pip python3-venv python3-dev build-essential \
      libxml2-dev libxslt1-dev libffi-dev libpq-dev libssl-dev zlib1g-dev \
      libldap2-dev libsasl2-dev libssl-dev snmpd snmp libsnmp-dev git curl

RUN adduser --system --group openl2m
ADD --chown=openl2m openl2m /opt/openl2m
ADD --chown=openl2m requirements.txt /opt/openl2m

WORKDIR /opt/openl2m
RUN pip3 install -r requirements.txt

ADD --chown=openl2m entrypoint.sh .
USER openl2m

ENTRYPOINT ["/opt/openl2m/entrypoint.sh"]