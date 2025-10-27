import csv

def main():
    # read csv using generic read
    produce_file_csv = open("produce.csv")
    produce_file_csv_content = produce_file_csv.read()
    print(produce_file_csv_content)

    # read csv using csv module
    produce_file_csv2 = open("produce.csv")
    produce_file_csv2_content = csv.DictReader(produce_file_csv2)
    print(produce_file_csv2_content)

    produce_file_csv2_fields = produce_file_csv2_content.fieldnames
    print(produce_file_csv2_fields)

    for row in produce_file_csv2_content:
        print(row)


    # read tsv using generic read
    produce_file_tsv = open("produce.tsv")
    produce_file_tsv_content = produce_file_tsv.read()
    print(produce_file_tsv_content)

    # read tsv using csv read
    produce_file_tsv2 = open("produce.tsv")
    produce_file_tsv2_content = csv.DictReader(produce_file_tsv2)
    print(produce_file_tsv2_content)

    produce_file_tsv2_fields = produce_file_tsv2_content.fieldnames
    print(produce_file_tsv2_fields)

    for row in produce_file_tsv2_content:
        print(row)


if __name__ == "__main__":
    main()
