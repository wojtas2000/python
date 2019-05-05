import csv
import sprawdz
import czy_istnieje


def usun_imie():
    """funkcja usuwająca wprowadzone imie z bazy"""

    imie = (input("Dodaj imię:").strip()).capitalize()
    nazwisko = (input("Dodaj nazwisko:").strip()).capitalize()

    if sprawdz.czy_poprawnie(imie, nazwisko):
        if czy_istnieje.jest(imie, nazwisko):

            with open("baza.csv", "r") as csv_file:
                csv_reader = csv.DictReader(csv_file)

                with open("baza_test.csv", "w", newline='') as new_file:
                    filed_name = ['Imie', 'Nazwisko']
                    csv_writer_new_file = csv.DictWriter(new_file, fieldnames=filed_name)
                    csv_writer_new_file.writeheader()

                    for line in csv_reader:
                        if line["Imie"] != imie and line["Nazwisko"] != nazwisko:
                            csv_writer_new_file.writerow(line)

            with open("baza_test.csv", "r") as csv_file_2:
                csv_reader_2 = csv.DictReader(csv_file_2)

                with open("baza.csv", "w", newline='') as new_file_2:
                    filed_name_2 = ['Imie', 'Nazwisko']
                    csv_writer_new_file_2 = csv.DictWriter(new_file_2, fieldnames=filed_name_2)
                    csv_writer_new_file_2.writeheader()

                    for line_1 in csv_reader_2:
                        csv_writer_new_file_2.writerow(line_1)

            print("Wpis \"{} {}\" został pomyślnie usunięty.\n".format(imie, nazwisko))

        else:
            print("Podanego kontaktu nie ma w bazie.\n")
