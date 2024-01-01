import csv
def read_csv_file(file_path):
    try:
        with open(file_path, 'r', newline='') as csv_file:
            csv_reader = csv.reader(csv_file)
            
         
            header = next(csv_reader, None)
            if header:
                print(f"Header: {header}")
            
            for row in csv_reader:
                print(f"Row: {row}")
    
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
    except Exception as e:
        print(f"Error: {e}")


csv_file_path = "users.csv"


read_csv_file(csv_file_path)
