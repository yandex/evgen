FROM ubuntu:20.04

RUN apt update -y && apt install -y wget vim

RUN useradd -ms /bin/bash evgen
USER evgen
RUN echo "export PATH=/usr/share/swift/usr/bin:$PATH" >> ~/.bashrc

WORKDIR /home/evgen
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
RUN bash Miniconda3-latest-Linux-x86_64.sh -b -p /home/evgen/miniconda
RUN rm Miniconda3-latest-Linux-x86_64.sh
ENV PATH=/home/evgen/miniconda/bin:$PATH
RUN conda init bash
RUN conda install python=3.8

ADD --chown=evgen . /home/evgen/evgen
WORKDIR /home/evgen/evgen
RUN pip install .
