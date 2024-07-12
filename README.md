# Project Export Script

This script exports the contents of specified files in a project directory into a single text file, with a directory and file structure at the top.

## Configuration

The script is configured via a `config.yml` file. Below is an example configuration:

```yaml
project_directory: '/path/to/your/project'
output_file: '/path/to/your/output/file.txt'
ignore_dirs:
  - node_modules
  - .git
file_extensions:
  - .js
  - .css
  - .html
  - .yml
filenames:
  - Dockerfile
```

## Install dependency
`pip install pyyaml`

## Run the script
`python export_files.py`

## Check Output File: 
The output file specified in the config.yml will contain the directory and file structure at the top, followed by the contents of the specified files, each separated by "------".

## Sample Result
```
Directory and File Structure:
project/
    Dockerfile
    config.yml
    export_files.py
    src/
        index.js
        style.css
        index.html

Files Content:
------
/path/to/your/project/Dockerfile
# Sample Dockerfile content
FROM node:14
WORKDIR /app
COPY . .
RUN npm install
CMD ["node", "src/index.js"]

------
/path/to/your/project/src/index.js
// Sample JavaScript content
console.log('Hello, World!');

------
/path/to/your/project/src/style.css
/* Sample CSS content */
body {
    font-family: Arial, sans-serif;
}

------
/path/to/your/project/src/index.html
<!-- Sample HTML content -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Hello, World!</h1>
    <script src="index.js"></script>
</body>
</html>
```

## Limitations and Precautions
- If the project directory is too large, the script may take a long time to execute and the output file may become very large, potentially causing performance issues or exceeding file size limits. 
- The script reads all specified files into memory, which could lead to high memory usage for very large files or many files. 
- If you plan to use the output file with an AI service, be aware of token or character limits imposed by the AI provider, as exceeding these limits could result in truncated responses or errors. 
- To optimize performance, add any other large or unnecessary directories to the `ignore_dirs` list in the `config.yml` file.