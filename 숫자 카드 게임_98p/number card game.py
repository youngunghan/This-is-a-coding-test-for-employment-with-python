def read_data():
    with open('숫자 카드 게임_98p\input.txt', 'r') as f:
        datas = []
        while True:
            line = f.readline()
            if not line:
                break            
            datas.append( list(map(int, line.split())) )
        return datas

def main():
    datas = read_data()
    max_rows = []
    for row_data in datas[1:]:
        max_rows.append(min(row_data))
    print(max(max_rows))

main()
