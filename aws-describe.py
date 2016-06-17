import boto3
import sys, argparse
import json


parser = argparse.ArgumentParser(description='Describe AWS Ec2 resources')
parser.add_argument('-d', '--describe-tags', action='store_true', help='describe tags parameter', default=False)
parser.add_argument('-tn', '--tags', action='store', nargs='+', help='tag or tags to descibe', default=[])
parser.add_argument('-gip', '--get-ip-address', action='store_true', help='returns just ip addresses', default=False)
parser.add_argument('-gn', '--get-instance-name', action='store_true', help='returns just ip addresses', default=False)
parser.add_argument('-gid', '--get-instance-id', action='store_true', help='returns just ip addresses', default=False)
parser.add_argument('-gsg', '--get-security-group', action='store_true', help='returns just ip addresses', default=False)
parser.add_argument('-v', '--verbose', action='store_true', help='returns just ip addresses', default=False)


args = parser.parse_args()
print args

#Lets check tags and build the array for the describe request
tag_filters = []
def simplify_tags(tagname) :
   if tagname == 'asg' :
      return 'tag:aws:autoscaling:groupName'
   else :
      return tagname

for i in range(len(args.tags)) :
   splitted = args.tags[i].split('=')
   if len(splitted) == 2 :
      data = {}
      data['Name'] = simplify_tags(splitted[0])
      data['Values'] = splitted[1]
      json_data = json.dumps(data)
      tag_filters.append(json_data) 
   else :
      print 'Tags were not written in the right way, You must specify tag_name=tag_value'

print tag_filters
