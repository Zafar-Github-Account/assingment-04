def main():
    fehrenheit =float(input("\033[1;3m Enter tempreture in fehrenheit:  \033[0m"))
    celsius = (fehrenheit - 32) * 5.0/9.0
    print(f"Temperature : {fehrenheit}F ={celsius} C ")

if __name__ == '__main__':
    main()    