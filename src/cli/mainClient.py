from src.cli.container import *
import click
import yaml
import os
import docker
import re

# sets the docker host from your environment variables
client = docker.Client(**docker.utils.kwargs_from_env(assert_hostname=False))

pathFile = "/home/dido/github/DockerFinder/resources/versions.yml"

#@click.command()
#@click.argument('image', nargs=-1)
#@click.option('--image', '-i', help='Image name in which to run do', default=None)
def dofinder(image):


    # try to set image
    if not image:
        ims = client.images()
        if len(ims) >= 1:
            image = [im['RepoTags'][0] for im in client.images()][0]


    assert image, 'No image given or found locally.'

    # get image if not available locally
    imnames = [im['RepoTags'][0] for im in client.images()]
    if (not any([image in imname for imname in imnames])) and client.search(image):
        print('Image {} not found locally. Pulling from docker hub.'.format(image))
        ret = client.pull(image)
        print(ret)

    versionCommands = yaml.load(open(pathFile))

    with Container(image, cleanup=True) as c:
        for bin, cmd, regex in getVersionCommad(versionCommands):
            print("[{}] searching {} ".format(image, bin))
            for output_line in c.run(bin+" "+cmd):
                p = re.compile(regex)     ## can ve saved the compilatiion of the regez to sae time (if the refez is equal to all the version)
                match = p.search(output_line.decode())
                if match:
                    ver = match.group(0)
                    print('[{}] found {} {}'.format(image, bin, ver))
                else:
                    print("[{}] not found {}".format(image, bin))



def getVersionCommad(ymlCommand):
    for app in ymlCommand:
        yield app["name"], app["ver"], app["re"]


#if __name__ == '__main__':
#    dofinder()

dofinder("python")

dofinder("java")