DATA_FILE = '../DATA/world_airport_codes.txt'
# sample data
# ABE ALLENTOWN, PENNSYLVANIA, USA
# ABF ABAIANG, REP. OF KIRIBATI
# ABG ABINGDON, QLD., AUSTRALIA

def main():
    codes = read_data()
    while True:
        code = input("Enter airport code: ")
        if code == '': # user just pressed <ENTER>
            print("Please enter a code")
            continue
        if code == 'q':
            print("goodbye")
            break
        
        # use code.upper() so user can type in lower or upper
        city = codes.get(code.upper(), "NOT FOUND")
        print(city)

def read_data():
    with open(DATA_FILE) as codes_in:
        codes = {}
        for raw_line in codes_in:
            line = raw_line.rstrip('\n')
            code = line[:3]  # first three chars
            airport = line[4:]  # fourth char through end
            codes[code] = airport
        return codes

if __name__ == "__main__":
    main()