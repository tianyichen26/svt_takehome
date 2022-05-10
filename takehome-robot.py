import requests
import json
import math
import argparse


# function for get http response from given api
def get_robot_info():
    global response_info
    response = requests.get("https://60c8ed887dafc90017ffbd56.mockapi.io/robots").text
    response_info = json.loads(response)



def find_best_robot(loadId,x,y):
    global response_info
    min_distance = 100000
    robot_dict = {}
    robot_id = 0
    # loop through http response to get the robot within 10 unit into a dictionary
    for r in response_info:
        dis_square = abs(x-r['x'])**2 + abs(y-r['y'])**2
        distance = math.sqrt(dis_square)
        if distance < 10:
            robot_dict[r['robotId']] = [r['batteryLevel'],distance]
    max_bat = 0

    # for robots in 10 unit, compare the battery life and choose the highest battery robot
    for key in robot_dict:
       if robot_dict[key][0]>max_bat:
           max_bat = robot_dict[key][0]
           robot_id = key
           select_distance = robot_dict[key][1]
    return robot_id,select_distance,max_bat


def main():
    parser = argparse.ArgumentParser(description='find best robot for the load!')
    parser.add_argument('-l', '--load',  required=True)
    parser.add_argument('-x', '--x', type = int, required=True)
    parser.add_argument('-y', '--y', type = int, required=True)
    args = parser.parse_args()

    get_robot_info()
    r_id,distance,batterlevel = find_best_robot(args.load,args.x,args.y)
    print(r_id)
main()
