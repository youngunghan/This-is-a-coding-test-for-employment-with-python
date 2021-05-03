# n: size of list
# m: Number of times that you can add
# k: Number of times that cannot be added in succession
def add_law_large_number(n, m, k):
    max_first = 0
    max_second = 0
    for i in range(n):
        if nums[i] > max_first:
            max_second = max_first
            max_first = nums[i]
        elif max_second < nums[i] < max_first:
            max_second = nums[i]

    cnt = 0
    large_num = 0
    for _ in range(m):
        if cnt < k:
            large_num += max_first
        else:
            large_num += max_second
            cnt = 0
        cnt += 1
    print(large_num)

def read_data():
    with open('큰 수의 법칙_92p\input.txt', 'r') as f:
        datas = []
        while True:
            line = f.readline()
            if not line:
                break            
            datas.append( list(map(int, line.split())) )
        return datas
    
def main():
    datas = read_data()
    size_nums = datas[0][0]
    added_cnt = datas[0][1]
    max_continuously_added_cnt = datas[0][2]
    global nums 
    nums = datas[1]

    add_law_large_number(size_nums, added_cnt, max_continuously_added_cnt)

main()