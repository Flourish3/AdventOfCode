if __name__ == "__main__":
    with open("2022/data/day04.txt") as f:
        count = 0
        overlap_count = 0
        overlap_count_2 = 0

        for line in f. readlines():
            first_elf, second_elf  = line.strip().split(",")
            x1,x2 = list(map(int, first_elf.split("-")))
            y1,y2 = list(map(int, second_elf.split("-")))
            print(x1, " ", x2, "   -   ", y1, " ", y2)
            if ((x2<=y2 and x1>=y1)  or (y2<=x2 and y1>=x1)):
                print("match!")
                count+=1
            
            if (y2>=x1 and x2>=y1) or (x1<=y2 and y2<=x2) or (x2<=y2 and x1>=y1)  or (y2<=x2 and y1>=x1):
                print("Overlap match")
                overlap_count += 1
                
            # Count by checking if ther is no overlap
            if not ((x2 < y1) or (y2 < x1)):
                overlap_count_2 += 1

        print(count)
        print(overlap_count)
        print(overlap_count_2)
