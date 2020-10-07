ARG base_image

FROM ${base_image}

ARG agent_version
ARG agent_implementation
ARG tag_name=aries-cloudagent
ARG tag_version=

ENV SUMMARY="aries-cloudagent image" \
    DESCRIPTION="aries-cloudagent provides a base image for running Hyperledger Aries agents in Docker. \
    This image layers the $agent_implementation implementation of aries-cloudagent $agent_version \
    on top of the base image $base_image."

LABEL summary="$SUMMARY" \
    description="$DESCRIPTION" \
    io.k8s.description="$DESCRIPTION" \
    io.k8s.display-name="aries-cloudagent $tag_version" \
    name="$tag_name" \
    version="$tag_version" \
    maintainer=""

RUN pip install --no-cache-dir git+https://github.com/ianco/ConfigArgParse.git#egg=ConfigArgParse
RUN pip install --no-cache-dir aries-cloudagent==${agent_version}

ENTRYPOINT ["/bin/bash", "-c", "aca-py \"$@\"", "--"]
