import os
import yaml

def get_directory_structure(directory, ignore_dirs):
    structure = []
    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if d not in ignore_dirs]
        level = root.replace(directory, '').count(os.sep)
        indent = ' ' * 4 * (level)
        structure.append(f"{indent}{os.path.basename(root)}/")
        sub_indent = ' ' * 4 * (level + 1)
        for file in files:
            structure.append(f"{sub_indent}{file}")
    return '\n'.join(structure)

def export_files_to_txt(directory, output_file, ignore_dirs, file_extensions, filenames):
    structure = get_directory_structure(directory, ignore_dirs)
    
    with open(output_file, 'w') as outfile:
        # Write the directory structure at the top
        outfile.write("Directory and File Structure:\n")
        outfile.write(structure)
        outfile.write("\n\nFiles Content:\n")
        
        for root, dirs, files in os.walk(directory):
            # Ignore specified directories
            dirs[:] = [d for d in dirs if d not in ignore_dirs]
            
            for file in files:
                if file in filenames or os.path.splitext(file)[1] in file_extensions:
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r') as infile:
                        outfile.write(f"------\n{file_path}\n")
                        outfile.write(infile.read())
                        outfile.write("\n")

def load_config(config_file):
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)
    return config

if __name__ == "__main__":
    config = load_config('config.yml')
    project_directory = config['project_directory']
    output_txt_file = config['output_file']
    ignore_dirs = set(config['ignore_dirs'])
    file_extensions = set(config['file_extensions'])
    filenames = config['filenames']
    
    export_files_to_txt(project_directory, output_txt_file, ignore_dirs, file_extensions, filenames)
    print(f"Files exported to {output_txt_file}")
