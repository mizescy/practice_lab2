import statistics

def main():
    print("testing")
    display_main_menu()
    num_list = get_user_input()
    print("Average: ", calc_average(num_list))
    print("Min and Max: ", find_min_max(num_list))
    print("Sorted Temeratures: ", sort_temperature(num_list))
    print("Median Temerature: ", calc_median_temperature(sort_temperature(num_list)))

def display_main_menu():
    print("Enter some numbers serparated by commas")

def get_user_input():
    user_input = input()
    input_split = user_input.split(",")
    list_input = []

    for item in input_split:
        item = item.strip()
        list_input.append(float(item))

    return list_input

def calc_average(num_list):
    return sum(num_list) / len(num_list)

def find_min_max(num_list):
    return  [min(num_list), max(num_list)]

def sort_temperature(num_list):
    return sorted(num_list)

def calc_median_temperature(num_list):
    return statistics.median(num_list) 


if __name__=="__main__":
    main()