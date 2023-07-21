def get_min_distance(houses, towers):
    min_distance = 0
    for each_house in houses:
        if each_house > towers[0]:
            min_distance_each_house = each_house - towers[0]
        else:
            min_distance_each_house = towers[0] - each_house

        for each_tower in towers:
            if each_house > each_tower:
                distance = each_house - each_tower
            else:
                distance = each_tower - each_house
            
            if distance < min_distance_each_house:
                min_distance_each_house = distance

        if min_distance_each_house > min_distance:
            min_distance = min_distance_each_house

    return min_distance


def convert_to_num(str_list):
    num_list = []
    for s in str_list:
        num = int(s)
        num_list.append(num)
    return num_list
           
def main():
    houses = input().split()
    towers = input().split()
    given_distance = int(input())
    houses_number = convert_to_num(houses)
    towers_number = convert_to_num(towers)

    min_distance = get_min_distance(houses_number, towers_number)
    min_adjustment = min_distance - given_distance

    print(min_adjustment)

main()