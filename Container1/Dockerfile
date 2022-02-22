FROM ubuntu:16.04 
   
MAINTAINER Your name <wei.ling@mailbox.tu-dresden.de>

COPY memcached-1.4.33.tar.gz .

RUN apt-get update
RUN apt-get upgrade -y
RUN useradd -ms /bin/bash  ubuntu
RUN apt-get install -y openssh-server
RUN apt-get install -y gcc
RUN apt-get install -y make
RUN apt-get install -y libevent-dev
RUN apt-get install -y vim
RUN echo "ubuntu:ubuntu" | chpasswd
RUN echo "StrictHostKeyChecking=no" >> /etc/ssh/ssh_config
RUN mkdir /var/run/sshd
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
RUN echo "export VISIBLE=now" >> /etc/profile
RUN gunzip -c memcached-1.4.33.tar.gz | tar xf -
RUN cd memcached-1.4.33 && ./configure && make && make install
RUN mkdir /home/ubuntu/.ssh && echo 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDcFj9AJ0yx2NswwEKPFQZqpiYZ8Mzk1LlRNatsVQqUfaDoQTKewuHRpp5jREB9RIMPczgFPDZSOBQ+mV8u5qJScmOcB8rhaF0GZkF1KIgHSNj8VqDNZWP52m1+NxSJetp6Opu3zTzkoZt9uo4HHeVZseTfN0UkxSjcWKYPX7+rOrvMhIxxKB9bR7UjmMkmoMfzP8UVkmc4MxIOo+RW9OM9GFselGN9JTYceZW8xhWNH2ENXQNWE5a807vP6kaKWp5bQ/c7NpISvTAO5UaVD26IRrtqea//MiUORjbXX+dEpFZuN6fRMh+zemerQ9rDHcgxRMacGZxBUjIRCa92zSr3 gitlab-runner@sep' >> /home/ubuntu/.ssh/authorized_keys && \
        echo 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCdK1lnrkOK0NLsEhH9ZusnETUwyEwV63Te1ri5XzzHc7OOMdspu6UN5yG0CJBQEomWmMYgJd8hIK07WcbVu6SHmFJMF0GOKO3xWF+wDS0ILdR2WZXpiSVBkLMIxFCOVHIT9cuSY7MHsP6/0QOiohb7flikPQk0CREDhtRPIvLlHViR/HEbpekZjiwKPJYP8DrpqjSnhwS/+ZOwezeM0T/TkbeVZOOPakY5PxzIG1CUN5MgyJNcr6mdngeke76/IFXF4aMlNcu9PO2vXkAUhrO3ghOEChpdo4rDIIz1/JL0dbLnrdsuNHhx2DHqLAFjme0Fv/AHAt1xVaaFKVwBGECueVby2Adn9fql8+EWVNnlxcfVhqr29rmXvYTVsp6se6ZQhYd6F/Fn5jrLMviOv9hEkIs60/UWK6p45FzZDInNbJBfdBg9ud8ujg1zDrjJNgohqNwgbiNqpu64a7ZsB/TD1ehHIRekj/5h1zGJrV+b3ngs9m3Gqy4PtBoth5cBXZfwYW2uL4VdoxCutNN7HtgKQv2CMGEAfLcyFul9Xk+oHALBHDPodRA91qPW5l2eE5BeZisTBVLq14S7zQFTXyQa2RnBXgjait5iNzcjszaaVKK5y65rNtbar30oItU4OkNIbKxwxu/ec/k//7eNdqb3UU0tSDxWJRckSVNDgPdgdw== 751069606@qq.com' >> /home/ubuntu/.ssh/authorized_keys && \
        echo 'ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIFqIfYucYM495P+zj6/76PhK/Ed2PzU6Qo0tf90gTF4Y <wei.ling@mailbox.tu-dresden.de>' >> /home/ubuntu/.ssh/authorized_keys
RUN mkdir /root/.ssh && echo 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDcFj9AJ0yx2NswwEKPFQZqpiYZ8Mzk1LlRNatsVQqUfaDoQTKewuHRpp5jREB9RIMPczgFPDZSOBQ+mV8u5qJScmOcB8rhaF0GZkF1KIgHSNj8VqDNZWP52m1+NxSJetp6Opu3zTzkoZt9uo4HHeVZseTfN0UkxSjcWKYPX7+rOrvMhIxxKB9bR7UjmMkmoMfzP8UVkmc4MxIOo+RW9OM9GFselGN9JTYceZW8xhWNH2ENXQNWE5a807vP6kaKWp5bQ/c7NpISvTAO5UaVD26IRrtqea//MiUORjbXX+dEpFZuN6fRMh+zemerQ9rDHcgxRMacGZxBUjIRCa92zSr3 gitlab-runner@sep' >> /root/.ssh/authorized_keys && \
        echo 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCdK1lnrkOK0NLsEhH9ZusnETUwyEwV63Te1ri5XzzHc7OOMdspu6UN5yG0CJBQEomWmMYgJd8hIK07WcbVu6SHmFJMF0GOKO3xWF+wDS0ILdR2WZXpiSVBkLMIxFCOVHIT9cuSY7MHsP6/0QOiohb7flikPQk0CREDhtRPIvLlHViR/HEbpekZjiwKPJYP8DrpqjSnhwS/+ZOwezeM0T/TkbeVZOOPakY5PxzIG1CUN5MgyJNcr6mdngeke76/IFXF4aMlNcu9PO2vXkAUhrO3ghOEChpdo4rDIIz1/JL0dbLnrdsuNHhx2DHqLAFjme0Fv/AHAt1xVaaFKVwBGECueVby2Adn9fql8+EWVNnlxcfVhqr29rmXvYTVsp6se6ZQhYd6F/Fn5jrLMviOv9hEkIs60/UWK6p45FzZDInNbJBfdBg9ud8ujg1zDrjJNgohqNwgbiNqpu64a7ZsB/TD1ehHIRekj/5h1zGJrV+b3ngs9m3Gqy4PtBoth5cBXZfwYW2uL4VdoxCutNN7HtgKQv2CMGEAfLcyFul9Xk+oHALBHDPodRA91qPW5l2eE5BeZisTBVLq14S7zQFTXyQa2RnBXgjait5iNzcjszaaVKK5y65rNtbar30oItU4OkNIbKxwxu/ec/k//7eNdqb3UU0tSDxWJRckSVNDgPdgdw== 751069606@qq.com' >> /root/.ssh/authorized_keys && \
        echo 'ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIFqIfYucYM495P+zj6/76PhK/Ed2PzU6Qo0tf90gTF4Y <wei.ling@mailbox.tu-dresden.de>' >> /root/.ssh/authorized_keys
EXPOSE 80
EXPOSE 11211
EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
