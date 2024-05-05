import pandas as pd
import pyreadstat

def merge_spss_files(spss_file_paths):
    merged_dfs = []
    labels_to_columns = {}
    merged_value_labels = {}
    merged_variable_formats = {}
    merged_missing_values = {}

    for file_path in spss_file_paths:
        print(f"Processing {file_path}")
        df, meta = pyreadstat.read_sav(file_path, apply_value_formats=True)
        
        column_labels = {df.columns[i]: label for i, label in enumerate(meta.column_labels) if label}
        
        new_column_names = {}
        for col, label in column_labels.items():
            standardized_col = labels_to_columns.get(label, col)
            
            # Avoiding column name duplication
            if standardized_col in df.columns:
                standardized_col += f"_{df.columns.get_loc(col)}"  # Add a unique suffix based on column position
            
            new_column_names[col] = standardized_col
            labels_to_columns[label] = standardized_col

            # Merging metadata (Variables)
            existing_labels = merged_value_labels.get(standardized_col, {})
            new_labels = meta.variable_value_labels.get(col, {})
            existing_labels.update(new_labels)
            merged_value_labels[standardized_col] = existing_labels

            merged_variable_formats[standardized_col] = meta.variable_measure.get(col, '')
            merged_missing_values[standardized_col] = meta.missing_ranges.get(col, [])

        df.rename(columns=new_column_names, inplace=True)
        df.reset_index(drop=True, inplace=True)
        merged_dfs.append(df)

    merged_df = pd.concat(merged_dfs, axis=0, ignore_index=True, sort=False)
    return merged_df, labels_to_columns, merged_value_labels, merged_variable_formats, merged_missing_values

def write_merged_spss_file(merged_df, output_file_path, metadata):
    metadata_dict = {
        'column_labels': {column_name: label for label, column_name in metadata['labels_to_columns'].items()},
        'variable_value_labels': metadata['merged_value_labels'],
        'variable_measure': metadata['merged_variable_formats'],
        'missing_ranges': metadata['merged_missing_values'],
        'variable_display_width': {col: 11 for col in merged_df.columns}  
    }
    pyreadstat.write_sav(merged_df, output_file_path, column_labels=metadata_dict['column_labels'],
                         variable_measure=metadata_dict['variable_measure'], missing_ranges=metadata_dict['missing_ranges'],
                         variable_value_labels=metadata_dict['variable_value_labels'],
                         variable_display_width=metadata_dict['variable_display_width'])
    print(f"Successfully merged SPSS files into {output_file_path}")

def main():
    spss_file_paths = [
    './35.sav',
    './36.sav',
    './37.sav',
    './38.sav',
    #######
    './41.sav',
    './42.sav',
    './43.1.sav',
    './44.sav',
    './48.sav',
    './49.sav',
    #######
    './51.sav',
    './53.sav',
    './55.1.sav',
    './56.2.sav',
    #######
    './61.sav',
    './62.sav',
    './63.4.sav',
    './64.2.sav',
    './65.2.sav',
    './68.1.sav',
    #######
    './71.3.sav',
    './79.3.sav',
    #######
    './84.3.sav',
    './86.2.sav',
    './87.3.sav',
    './89.1.sav',
    ]

    merged_df, labels_to_columns, merged_value_labels, merged_variable_formats, merged_missing_values = merge_spss_files(spss_file_paths)
    output_file_path = 'merged_data_final.sav'
    metadata = {
        'labels_to_columns': labels_to_columns,
        'merged_value_labels': merged_value_labels,
        'merged_variable_formats': merged_variable_formats,
        'merged_missing_values': merged_missing_values
    }
    write_merged_spss_file(merged_df, output_file_path, metadata)

if __name__ == "__main__":
    main()
