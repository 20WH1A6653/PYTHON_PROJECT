print("hello")

def reading_input():
    fire_exist = (input("fire place:"))
    open_paths = []
    x = input("route points: ")
    paths_list = list()
    while (not(x == "0 0")):
        start, end = x.split(" ")
        start = int(start)
        end = int(end)
        paths_list.append((start, end))
        x = input("route points:")
        print(paths_list)
reading_input()        
