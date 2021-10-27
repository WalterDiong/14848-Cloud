def main():
    print("Welcome to Big Data Processing Application\n\
Please type the number that corresponds to which application you would like to run:\n\
Enter 5 to exit:\n\
1. Apache Hadoop\n\
2. Apache Spark\n\
3. Jupyter Notebook\n\
4. SonarQube and SonarScanner\n")

    while(True):
        value = input("")
        if value == "1":
            print("Activating Hadoop!\n")
        elif value == "2":
            print("Activating Spark!\n")
        elif value == "3":
            print("Activating Jupyter!\n")
        elif value == "4":
            print("Activating Sonar Stuff!\n")
        elif value == "5":
            quit()

main()