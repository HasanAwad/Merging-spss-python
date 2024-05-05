
# SPSS File Merger

## Overview
This Python script automates the process of merging multiple SPSS (.sav) files into a single file. It ensures that all metadata such as variable labels, value labels, variable formats, and missing values are preserved and integrated. This is particularly useful for researchers and analysts dealing with fragmented datasets across multiple SPSS files.

## Features
- **Merge Multiple Files**: Consolidates several .sav files into a single dataset, maintaining all associated metadata.
- **Metadata Management**: Handles variable labels, value labels, variable formats, and missing values efficiently.
- **User-Friendly**: Simple setup and execution process.

## Prerequisites
Ensure Python is installed along with the following packages:
- pandas
- pyreadstat

You can install them using pip:
```bash
pip install pandas pyreadstat
```

## Installation
Clone this repository to your local machine:
```bash
git clone https://github.com/HasanAwad/Merging-spss-python.git
```

## Usage
1. Place all .sav files you wish to merge in one directory.
2. Modify the `spss_file_paths` list in the script to include the paths to the files.
3. Run the script:
```bash
python3 main.py
```

## Functions
- `merge_spss_files(spss_file_paths)`: Reads and merges the files.
- `write_merged_spss_file(merged_df, output_file_path, metadata)`: Outputs the merged data into a new .sav file.
- `main()`: Entry point of the script which processes the files.

## Output
Produces a `merged_data_final.sav` file containing the merged data and metadata.

## Contributing
Feel free to fork this project and contribute by submitting a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For support, contact me at hasan.awwad.dev@gmail.com.
