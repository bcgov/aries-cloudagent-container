#!/usr/bin/env python3

import argparse
import os
import random
import re
import subprocess
import sys

VERSIONS = {
    "python": [
        {
            "version": "0.3.0",
            "args": {
                "base_image": "bcgovimages/von-image:py36-1.11-0"
            },
        },
        {
            "version": "0.3.1",
            "args": {
                "base_image": "bcgovimages/von-image:py36-1.11-0"
            },
        },
        {
            "version": "0.3.2",
            "args": {
                "base_image": "bcgovimages/von-image:py36-1.11-1"
            },
        },
        {
            "version": "0.3.3",
            "args": {
                "base_image": "bcgovimages/von-image:py36-1.11-1"
            },
        },
        {
            "version": "0.3.4",
            "args": {
                "base_image": "bcgovimages/von-image:py36-1.11-1"
            },
        },
        {
            "version": "0.3.5",
            "args": {
                "base_image": "bcgovimages/von-image:py36-1.11-1"
            },
        },
        {
            "version": "0.4.0",
            "args": {
                "base_image": "bcgovimages/von-image:py36-1.11-1"
            },
        },
        {
            "version": "0.4.1",
            "args": {
                "base_image": "bcgovimages/von-image:py36-1.14-0"
            },
        },
        {
            "version": "0.4.2",
            "args": {
                "base_image": "bcgovimages/von-image:py36-1.14-0"
            },
        },
        {
            "version": "0.4.3",
            "args": {
                "base_image": "bcgovimages/von-image:py36-1.14-1"
            },
        },
        {
            "version": "0.4.4",
            "args": {
                "base_image": "bcgovimages/von-image:py36-1.14-1"
            },
        },
        {
            "version": "0.4.5",
            "args": {
                "base_image": "bcgovimages/von-image:py36-1.14-1"
            },
        },
        {
            "version": "0.5.0",
            "args": {
                "base_image": "bcgovimages/von-image:py36-1.14-1"
            },
        },
        {
            "version": "0.5.1",
            "args": {
                "base_image": "bcgovimages/von-image:py36-1.14-1"
            },
        },
        {
            "version": "0.5.2",
            "args": {
                "base_image": "bcgovimages/von-image:py36-1.15-0"
            },
        },
        {
            "version": "0.5.3",
            "args": {
                "base_image": "bcgovimages/von-image:py36-1.15-0"
            },
        }
    ]
}


def list_versions():
    versions = []

    for implementation in VERSIONS.keys():

        for item in VERSIONS.get(implementation):

            version = item.get("version")
            if version not in versions:
                versions.append(version)

    # sort list alphabetically
    versions.sort()

    return versions


def get_implementation_version(implementation: str, version: str) -> dict:
    implementation = VERSIONS.get(implementation)

    for item in implementation:

        ver = item.get("version")

        if ver == version:
            return item

    return None


DEFAULT_NAME = "bcgovimages/aries-cloudagent"


parser = argparse.ArgumentParser(description="Generate the aries-cloudagent Docker image")
parser.add_argument(
    "-n", "--name", default=DEFAULT_NAME, help="the base name for the docker image"
)
parser.add_argument("-t", "--tag", help="a custom tag for the docker image")
parser.add_argument("-f", "--file", help="use a custom Dockerfile")
parser.add_argument(
    "--build-arg", metavar="ARG=VAL", action="append", help="add docker build arguments"
)
parser.add_argument(
    "--dry-run",
    action="store_true",
    help="print docker command line instead of executing",
)
parser.add_argument("--no-cache", action="store_true", help="ignore docker image cache")
parser.add_argument(
    "-o",
    "--output",
    help="output an updated Dockerfile with the build arguments replaced",
)
parser.add_argument("--python", help="use a specific python version")
parser.add_argument("--push", action="store_true", help="push the resulting image")
parser.add_argument(
    "-q", "--quiet", action="store_true", help="suppress output from docker build"
)
parser.add_argument("--platform", help="build for a specific platform")
parser.add_argument("--squash", action="store_true", help="produce a smaller image")
parser.add_argument("--test", action="store_true", help="perform tests on docker image")
parser.add_argument(
    "version", choices=list_versions(), help="the release version"
)
parser.add_argument(
    "implementation", choices=VERSIONS.keys(), help="the agent implementation language"
)


args = parser.parse_args()
ver = get_implementation_version(args.implementation, args.version)
base_image = ver.get("args").get("base_image")

target = args.implementation
dockerfile = os.path.join(target, "Dockerfile")
if args.file:
    dockerfile = args.file

tag = args.tag
tag_name = args.name
if tag:
    tag_name, tag_version = tag.split(":", 2)
else:
    base_name, base_version = base_image.split(":", 1)
    tag_version = base_version + "_" + args.version
    tag = tag_name + ":" + tag_version

build_args = {}
build_args.update(ver["args"])
build_args["tag_name"] = tag_name
build_args["tag_version"] = tag_version
build_args["agent_version"] = args.version
build_args["agent_implementation"] = args.implementation
build_args["base_image"] = base_image
if args.build_arg:
    for arg in args.build_arg:
        key, val = arg.split("=", 2)
        build_args[key] = val

if args.output:
    src_path = dockerfile
    src_replace = build_args
    if args.test:
        src_path = os.path.join(target, "Dockerfile.test")
        src_replace = {"base_image": tag}
    with open(args.output, "w") as out:
        with open(src_path) as src:
            for line in src:
                m = re.match(r"^ARG\s+(\w+)=?(.*)$", line)
                if m:
                    line = "ARG {}={}\n".format(
                        m.group(1), src_replace.get(m.group(1), m.group(2))
                    )
                out.write(line)
    sys.exit(0)

cmd_args = []
for k, v in build_args.items():
    cmd_args.extend(["--build-arg", "{}={}".format(k, v)])
if dockerfile:
    cmd_args.extend(["-f", dockerfile])
if args.no_cache:
    cmd_args.append("--no-cache")
if args.squash:
    cmd_args.append("--squash")
cmd_args.extend(["-t", tag])
if args.platform:
    cmd_args.extend(["--platform", args.platform])

cmd_args.append(target)
cmd = ["docker", "build", "--rm"] + cmd_args

if args.dry_run:
    print(" ".join(cmd))
else:
    print("Building docker image...")
    proc = subprocess.run(cmd, stdout=(subprocess.PIPE if args.quiet else None))
    if proc.returncode:
        print("build failed")
        sys.exit(1)
    if args.quiet:
        print("Successfully tagged {}".format(tag))
    proc_sz = subprocess.run(
        ["docker", "image", "inspect", tag, "--format={{.Size}}"],
        stdout=subprocess.PIPE,
    )
    size = int(proc_sz.stdout.decode("ascii").strip()) / 1024.0 / 1024.0
    print("%0.2f%s" % (size, "MB"))

if not args.dry_run:
    if args.test or args.push:
        test_path = os.path.join(target, "Dockerfile.test")
        test_tag = tag + "-test"
        proc_bt = subprocess.run(
            [
                "docker",
                "build",
                "--rm",
                "--build-arg",
                "base_image=" + tag,
                "-t",
                test_tag,
                "-f",
                test_path,
                target,
            ]
        )
        if proc_bt.returncode:
            print("test image build failed")
            sys.exit(1)
        proc_test = subprocess.run(["docker", "run", "--rm", "-i", test_tag])
        if proc_test.returncode:
            print("One or more tests failed")
            sys.exit(1)
        print("All tests passed")

    if args.push:
        print("Pushing docker image...")
        proc = subprocess.run(["docker", "push", tag])
        if proc.returncode:
            print("push failed")
            sys.exit(1)
