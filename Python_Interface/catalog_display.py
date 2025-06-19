#Will be used to enter comic issue entries into the database
import psycopg2
from os import system

def main():
  run = True
  while run:
    system("clear")
    #connect to database (maybe have multiple to select from in the future)
    conn = pyscopg2.connect("dbname=repalce user=postgres")
    curr = conn.cursor()

    print("********COMIC LOGGING CATALOG********\n")
    print("Please Select One of the Following Options")
    print("\tA| Add Entry Into the Catalog\n\tS| Generate Catalog Statistics")
    command = input("\nPlease chose an action:")
    command = command.upper()
  
    #gather user input to store in database
  


if __name__ == '__main__':
  main()
