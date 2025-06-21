#Will be used to enter comic issue entries into the database
import psycopg2
from os import system
from init import initialize_database

def main():
  print("Here!")
  name = "Comic Catalog"
  user = input("User Name: ")
  password = input("Password: ")
  host = ("127.0.0.1")
  port = ("5432")

  initialize_database(name, user, password, host, port)

  run = True
  while run:
    system("clear")

    print("********COMIC LOGGING CATALOG********\n")
    print("Please Select One of the Following Options")
    print("\tA| Add Entry Into the Catalog\n\tS| Generate Catalog Statistics")
    command = input("\nPlease chose an action:")
    command = command.upper()
  
    #gather user input to store in database
  


if __name__ == '__main__':
  main()
