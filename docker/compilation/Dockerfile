FROM evgen_generation:latest

USER root

# Install swift
RUN apt update -y
RUN apt install -y clang libpython2.7 libpython2.7-dev
RUN wget https://swift.org/builds/swift-5.3-release/ubuntu2004/swift-5.3-RELEASE/swift-5.3-RELEASE-ubuntu20.04.tar.gz
RUN tar -xzf swift-5.3-RELEASE-ubuntu20.04.tar.gz
RUN mv swift-5.3-RELEASE-ubuntu20.04 /usr/share/swift

#Install kotlin and JAVA
ENV JAVA_TOOL_OPTIONS='-Dfile.encoding=UTF8'
RUN apt install nginx curl zip unzip -y
RUN apt install openjdk-14-jdk python3 python3-doc clang golang-go gcc g++ -y
RUN curl -s https://get.sdkman.io | bash
RUN bash /root/.sdkman/bin/sdkman-init.sh
RUN /bin/bash -c "source /root/.sdkman/bin/sdkman-init.sh; sdk version; sdk install kotlin"

#Install TypeScript
RUN apt install -y node-typescript

# USER evgen
ENV PATH "$PATH:/usr/share/swift/usr/bin/"
ENV PATH "$PATH:/root/.sdkman/candidates/kotlin/current/bin/"
