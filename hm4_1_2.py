#first function

def total_salary(path):

    try:

        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            salary_total = 0
            count = 0

            for line in lines:
                salary_total += int(line.split(',')[1])
                count += 1

            salary_median = salary_total / count
            
            return salary_total, salary_median
        
    except FileNotFoundError:
        print('File not found')


#second function
        
def get_cats_info(path):

    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            cats_info = []

            for line in lines:
                cat_info = {}
                id, name, age = line.split(',')
                cat_info = {'id': id, 'name': name, 'age': str(age).strip()}
                cats_info.append(cat_info)

            return cats_info
        
    except FileNotFoundError:
        print('File not found')
    
    except UnicodeDecodeError as e:
        print(f"Decoding Error: {e}")

cats_info = get_cats_info("E:\Python\cats.txt")
print(cats_info)