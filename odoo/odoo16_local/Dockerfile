FROM ubuntu:22.04
MAINTAINER Freedoo <info@freedoo.es>

ARG DEBIAN_FRONTEND=noninteractive

SHELL ["/bin/bash", "-xo", "pipefail", "-c"]

# Generate locale C.UTF-8 for postgres and general locale data
ENV LANG C.UTF-8

# Install some deps, lessc and less-plugin-clean-css, and wkhtmltopdf
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        ca-certificates \
        curl \
        git \
        dirmngr \
        fonts-noto-cjk \
        gnupg \
        libssl-dev \
        node-less \
        npm \
        python3-num2words \
        python3-pdfminer \
        python3-pip \
        python3-phonenumbers \
        python3-pyldap \
        python3-qrcode \
        python3-renderpm \
        python3-setuptools \
        python3-slugify \
        python3-vobject \
        python3-watchdog \
        python3-xlrd \
        python3-xlwt \
        libxrender1 \
        libfontconfig1 \
        libx11-dev \
        libjpeg62 \
        libxtst6 \
        fontconfig \
        libjpeg-turbo8-dev \
        xfonts-base \
        xfonts-75dpi \
        wget \
        xz-utils

RUN apt update && apt upgrade -y --no-install-recommends

RUN wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6.1-2/wkhtmltox_0.12.6.1-2.jammy_amd64.deb
RUN dpkg -i "wkhtmltox_0.12.6.1-2.jammy_amd64.deb"
RUN apt -f install

# install latest postgresql-client
RUN sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt jammy-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
RUN wget -qO- https://www.postgresql.org/media/keys/ACCC4CF8.asc | tee /etc/apt/trusted.gpg.d/pgdg.asc &>/dev/null
RUN apt install postgresql postgresql-client -y

# Install rtlcss (on Debian buster)
RUN npm install -g rtlcss

# Install some libraries


# Install Odoo
ENV ODOO_VERSION 16.0
ARG ODOO_RELEASE=20231024
ARG ODOO_SHA=8f81d6ff0fe4f9bc5a63cdeccb7006a7fc98f134
RUN curl -o odoo.deb -sSL http://nightly.odoo.com/${ODOO_VERSION}/nightly/deb/odoo_${ODOO_VERSION}.${ODOO_RELEASE}_all.deb \
    && echo "${ODOO_SHA} odoo.deb" | sha1sum -c - \
    && apt-get update \
    && apt-get -y install --no-install-recommends ./odoo.deb \
    && rm -rf /var/lib/apt/lists/* odoo.deb

# Copy entrypoint script and Odoo configuration file
COPY ./entrypoint.sh /
COPY ./config/odoo.conf /etc/odoo/

# Set permissions and Mount /var/lib/odoo to allow restoring filestore and /mnt/extra-addons for users addons
RUN chown odoo /etc/odoo/odoo.conf \
    && mkdir -p /mnt/extra-addons \
    && mkdir -p /mnt/disc_management \
    && mkdir -p /opt/odoo/oca_repos \
    && mkdir -p /opt/odoo/custom_addons \
    && mkdir -p /opt/odoo/backups \
    && chown -R odoo /mnt/extra-addons \
    && chown -R odoo /mnt/disc_management \
    && chown -R odoo /opt/odoo/oca_repos \
    && chown -R odoo /opt/odoo/custom_addons \
    && chown -R odoo /opt/odoo/backups 

VOLUME ["/var/lib/odoo", "/mnt/extra-addons"]

# Copiamos nuestros scrips a Oca Repos para desplegar y enlazar OCA
COPY ./oca_scripts/deploy_oca.sh /opt/odoo/oca_repos
COPY ./oca_scripts/link_oca_repos.sh /opt/odoo/oca_repos
COPY ./oca_scripts/update_requirements.sh /opt/odoo/oca_repos

# Ejecutamos la actualización de los requirements.txt de los repos de OCA
# y además instalamos el paquete nano para editar archivos
RUN cd /opt/odoo/oca_repos \
    && sh /opt/odoo/oca_repos/update_requirements.sh \
    && apt update && apt install nano


# Expose Odoo services
EXPOSE 8069 8071 8072

# Set the default config file
ENV ODOO_RC /etc/odoo/odoo.conf

COPY wait-for-psql.py /usr/local/bin/wait-for-psql.py

# Set default user when running the container
USER odoo

ENTRYPOINT ["/entrypoint.sh"]
CMD ["odoo"]
