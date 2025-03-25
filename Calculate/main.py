import sys
import calculate



def main():
    
    #print(sys.argv)
    #print(sys.argv[1])

    if len(sys.argv) == 2 and sys.argv[1] != "-r":
        print("USAGE: main.py [-r]")
        exit()
  

    for line in sys.stdin:
        math_input = line.strip()
        if math_input == "???":
            print("USAGE: main.py [-r]")
            exit()
        if not math_input:
            continue

        try:

            tech_deque = calculate.tokenize(math_input)
            if len(sys.argv) == 2 and sys.argv[1] == '-r':
                print(f"= {calculate.postfix(tech_deque)}")
            else:
                print(f"= {calculate.prefix(tech_deque)}")

        except RuntimeError as runerr:
                print (runerr)

if __name__ == "__main__":
    main()