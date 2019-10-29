import csv


def get_top_performers(file_path, number_of_top_students=5):
    with open(file_path, 'r', newline='') as f:
        sorted_rows = sorted(csv.DictReader(f), key=lambda v: float(v['average mark']), reverse=True)
        return [v['student name'] for v in sorted_rows[:number_of_top_students]]


def save_by_descending_age(file_path):
    with open(file_path, 'r', newline='') as rf:
        reader = csv.DictReader(rf)
        sorted_rows = sorted(reader, key=lambda v: int(v['age']), reverse=True)

    with open(file_path.replace('.csv', '_age.csv'), 'w', newline='') as wf:
        writer = csv.DictWriter(wf, reader.fieldnames)
        writer.writeheader()
        writer.writerows(sorted_rows)


if __name__ == '__main__':
    assert get_top_performers(r"data/students.csv") == ['Josephina Medina', 'Teresa Jones', 'Richard Snider',
                                                        'Jessica Dubose', 'Heather Garcia'], 'Test 1 failed'

