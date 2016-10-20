FROM debian:jessie

MAINTAINER Kladgs et Totoche

RUN apt-get update   && \
    apt-get install -y  \
    tor                 \
    git                 \
    bison               \
    libexif-dev         \
    python-pip          \
    curl                \
    pkg-config          \
    vim                  

RUN pip install stem

RUN git clone https://github.com/HugoMeziani/CaepaInvestigatio.git
RUN chmod +x CaepaInvestigatio/start.sh
RUN chmod +x CaepaInvestigatio/onionrunner.py

ADD onion_master_list.txt /

CMD /start.sh
