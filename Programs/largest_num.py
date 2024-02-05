def largest_num(num_list):  #find largest number
    large_num = num_list[0]     # assume that first num in list largest
    for num in num_list:     # iterate over the list
        if num > large_num:     
            large_num = num     # assign larger number to variable large_num

    return large_num

def main():
    nums = input("Enter the list of numbers (separated by comma): ").strip().split(", ")
    num_list = list(map(eval, nums))        # convert input into string
    print("Largest Number is:", largest_num(num_list))

if __name__ == "__main__":
    main()