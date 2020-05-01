import boto3
import click

session = boto3.Session(profile_name = 'shotty')
ec2 = session.resource('ec2')

def filter_instances(project):
    instances = []
    if project: #checking if project name is passed via cli
        filters = [{'Name':'tag:project','Values':[project]}]  # This one comes from boto3 docs. Somehow filtering based on project name isn't working well in my code
        instances = ec2.instances.filter(Filters = filters)
    else:
        instances=ec2.instances.all()

    return instances

@click.group()
def instances():
    """Commands for instances"""



@instances.command("list")
@click.option("--project",default=None, help="Instances with project name specified will be shown. If no project name then show all the instances")
def list_instances(project): # project name from the CLI option will be passed here
    "List EC2 instances"

    instances = filter_instances(project)
    for i in instances:
#        print(i.tags)
        tags = {t["Key"]:t["Value"] for t in i.tags or []}
#           in this statement we are just creating a tags variable which will have tags assigned to EC2 instance
#           by default when you try to find out tags on EC2 instances, it will come as list, but each member of list will be a dictionary - Name of tag:Value of tag. The above line is just taking the name and value and making it
#               dictonary rather than list of dictionary. The last part "[]" says if there is not tag, then create empty value.
        print('  '.join((i.id, i.instance_type, i.placement["AvailabilityZone"], i.state["Name"], i.public_dns_name, tags.get("project","<null>"))))

    return



@instances.command("stop")
@click.option("--project",default=None, help="Instances with project name specified will be STOPPED. If no project name then STOP all the instances")
def stop_instances(project):
    "STOP EC2 instances"

    instances = filter_instances(project)
    for i in instances:
        print("STOPPING ... {0}".format(i.id))
        i.stop()
    return

@instances.command("start")
@click.option("--project",default=None, help="Instances with project name specified will be STARTED. If no project name then START all the instances")
def start_instances(project):
    "START EC2 instances"
    instances = filter_instances(project)
    for i in instances:
        print("STARTING ... {0}".format(i.id))
        i.start()
    return



if __name__ == '__main__':
    instances()
