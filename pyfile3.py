# pyfile3.py
import os
import random

def run_pyfile3():
    print("pyfile3 is running")

    # Access files in the "resources" folder
    resources_dir = "Resources"
    resource_files = os.listdir(resources_dir)

    for filename in resource_files:
        file_path = os.path.join(resources_dir, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                file_contents = file.read()
                print(f"Content of {filename}:")
                print(file_contents)

                # Add random computations
                file_contents = file_contents.split('\n')
                for i, line in enumerate(file_contents):
                    random_number = random.randint(1, 100)
                    computed_line = f"Random Computation {i + 1}: {line.strip()} + {random_number} = {eval(line.strip()) + random_number}"
                    file_contents[i] = computed_line

                # Write back to the file
                with open(file_path, 'w') as updated_file:
                    updated_content = '\n'.join(file_contents)
                    updated_file.write(updated_content)

if __name__ == "__main__":
    run_pyfile3()
