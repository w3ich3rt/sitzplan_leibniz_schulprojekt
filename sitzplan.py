import csv
import random
import math

def read_student_data(file_name):
    student_data = []
    with open(file_name, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            student_data.append(row)
    return student_data

def assign_seats(student_data, table_size):
    random.shuffle(student_data)
    num_students = len(student_data)
    num_tables = math.ceil(num_students / table_size)
    tables = [student_data[i:i+table_size] for i in range(0, num_students, table_size)]
    if len(tables) > num_tables:
        last_table = tables.pop()
        for student in last_table:
            tables[random.randint(0, num_tables - 1)].append(student)
    return tables

def draw_table(table, table_number):
    print(f"Tisch {table_number}:")
    print("+----------------------+")
    for student in table:
        name = f"{student}"
        print(f"| {name:<20} |")
    print("+----------------------+\n")

def main():
    #file_name = input("Bitte geben Sie den Dateinamen der Schülerliste an (CSV-Format): ")
    #student_data = read_student_data(file_name)
    student_data = ["Bernd", "Claus", "Emily", "Larissa", "Karl", "Rudi", "Torben", "Lena", "Mara", "Wolle"]

    table_size = int(input("Bitte geben Sie die gewünschte Tischgröße (Anzahl der Sitzplätze pro Tisch) an: "))

    tables = assign_seats(student_data, table_size)

    for i, table in enumerate(tables):
        draw_table(table, i+1)

if __name__ == '__main__':
    main()
