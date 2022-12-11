FROM python:3.10

WORKDIR /home
RUN git clone https://github.com/fogleman/sdf.git sdf-install

WORKDIR /home/sdf-install
RUN pip install -e .

WORKDIR /home/sdf
