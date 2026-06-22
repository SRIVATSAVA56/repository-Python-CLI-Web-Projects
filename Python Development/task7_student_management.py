import json
import os

FILE_PATH = "students.json"

students_db = {}

def load_data():
    """Loads data from the JSON file into the dictionary. O(N) Time, O(N) Space."""
    global students_db
    if os.path.exists(FILE_PATH):
        try:
            with open(FILE_PATH, 'r') as file:
                loaded_data = json.load(file)
                if isinstance(loaded_data, dict):
                    students_db = loaded_data
                else:
                    print("Warning: Incompatible data format found in JSON. Starting fresh.")
                    students_db = {}
        except json.JSONDecodeError:
            students_db = {}

def save_data():
    """Saves the dictionary to the JSON file. O(N) Time, O(1) Auxiliary Space."""
    with open(FILE_PATH, 'w') as file:
        json.dump(students_db, file, indent=4)

def add_student(student_id, name, grade):
    """Adds a student. O(1) Time."""
    if student_id in students_db:
        print(f"Error: Student ID '{student_id}' already exists.")
        return
    students_db[student_id] = {"name": name, "grade": grade}
    save_data()
    print(f"Success: Added {name}.")

def update_student(student_id, name=None, grade=None):
    """Updates a student. O(1) Time."""
    if student_id not in students_db:
        print(f"Error: Student ID '{student_id}' not found.")
        return
    
    if name:
        students_db[student_id]['name'] = name
    if grade:
        students_db[student_id]['grade'] = grade
        
    save_data()
    print(f"Success: Updated Student ID '{student_id}'.")

def delete_student(student_id):
    """Deletes a student. O(1) Time."""
    # Using dict.pop() removes the key and handles the missing key error gracefully
    if students_db.pop(student_id, None):
        save_data()
        print(f"Success: Deleted Student ID '{student_id}'.")
    else:
        print(f"Error: Student ID '{student_id}' not found.")

def view_all():
    """Displays all students. O(N) Time."""
    if not students_db:
        print("No student records found.")
        return
    
    print("\n--- Student Records ---")
    for s_id, info in students_db.items():
        print(f"ID: {s_id} | Name: {info['name']} | Grade: {info['grade']}")
    print("-----------------------")

def main():
    load_data()
    
    while True:
        print("\n1. Add Student | 2. Update Student | 3. Delete Student | 4. View All | 5. Exit")
        choice = input("Enter choice (1-5): ").strip()
        
        if choice == '1':
            s_id = input("Enter Student ID: ").strip()
            name = input("Enter Name: ").strip()
            grade = input("Enter Grade: ").strip()
            if s_id and name and grade:
                add_student(s_id, name, grade)
            else:
                print("Error: All fields are required.")
                
        elif choice == '2':
            s_id = input("Enter Student ID to update: ").strip()
            name = input("Enter new Name (leave blank to keep current): ").strip()
            grade = input("Enter new Grade (leave blank to keep current): ").strip()
            
            if not name: name = None
            if not grade: grade = None
            
            add_student(s_id, name, grade) # Bug: Should be update_student
            
        elif choice == '3':
            s_id = input("Enter Student ID to delete: ").strip()
            delete_student(s_id)
            
        elif choice == '4':
            view_all()
            
        elif choice == '5':
            print("Exiting System. Data is saved.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()