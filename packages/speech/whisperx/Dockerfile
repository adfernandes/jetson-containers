#---
# name: whisperx
# group: audio
# depends: [pytorch, torchaudio, faster-whisper, transformers]
# requires: '>=34.1.0'
# docs: docs.md
#---
ARG BASE_IMAGE
FROM ${BASE_IMAGE}

WORKDIR /opt

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
		  ffmpeg \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

RUN pip3 install scipy jiwer ipywebrtc
RUN pip3 install scikit-learn

RUN git clone https://github.com/m-bain/whisperX.git && \
    cd whisperX && \
    sed -i 's/==/>=/g' requirements.txt && \
    sed -i 's/~=/>=/g' requirements.txt && \
    cat requirements.txt && \
    pip3 install -r requirements.txt && \
    python3 setup.py --verbose bdist_wheel

RUN cp whisperX/dist/whisperx*.whl /opt && \
    pip3 install /opt/whisperx*.whl

ENV LD_PRELOAD=/usr/lib/aarch64-linux-gnu/libgomp.so.1
RUN pip3 show whisperx && python3 -c 'import whisperx'

