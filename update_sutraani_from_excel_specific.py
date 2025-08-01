import pandas as pd
import json
import os

def update_sutraani_index_from_excel(excel_file_path, index_file_path="sutraani/index.txt"):
    """
    Read Excel file with startTime, endTime, i, duration columns and update sutraani index
    """
    
    # Read the Excel file
    try:
        df = pd.read_excel(excel_file_path)
        print(f"Successfully read Excel file: {excel_file_path}")
        print(f"Columns found: {list(df.columns)}")
        print(f"Number of rows: {len(df)}")
        
        # Show first few rows for verification
        print("\nFirst 5 rows of Excel data:")
        print(df.head())
        
        # Validate required columns
        required_columns = ['startTime', 'endTime', 'i', 'duration']
        missing_columns = [col for col in required_columns if col not in df.columns]
        
        if missing_columns:
            print(f"Error: Missing required columns: {missing_columns}")
            print(f"Available columns: {list(df.columns)}")
            return False
            
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return False
    
    # Read the current index file
    try:
        with open(index_file_path, 'r', encoding='utf-8') as f:
            index_data = json.load(f)
        print(f"Successfully read index file: {index_file_path}")
        
    except Exception as e:
        print(f"Error reading index file: {e}")
        return False
    
    # Create a mapping from Excel 'i' values to row data
    excel_data = {}
    for _, row in df.iterrows():
        i_value = str(int(row['i']))  # Convert to string to match index format
        excel_data[i_value] = {
            'startTime': float(row['startTime']),
            'endTime': float(row['endTime']),
            'duration': float(row['duration'])
        }
    
    print(f"Created mapping for {len(excel_data)} entries from Excel")
    
    # Show some sample mappings
    print("\nSample Excel data mappings:")
    sample_keys = list(excel_data.keys())[:5]
    for key in sample_keys:
        print(f"  {key}: {excel_data[key]}")
    
    # Update the index data
    updated_count = 0
    not_found_count = 0
    
    for item in index_data.get('data', []):
        i_value = item.get('i')
        if i_value in excel_data:
            # Add the new fields from Excel
            item['startTime'] = excel_data[i_value]['startTime']
            item['endTime'] = excel_data[i_value]['endTime']
            item['duration'] = excel_data[i_value]['duration']
            updated_count += 1
        else:
            not_found_count += 1
    
    print(f"Updated {updated_count} entries in the index")
    print(f"Not found in Excel: {not_found_count} entries")
    
    # Write the updated index back to file
    try:
        with open(index_file_path, 'w', encoding='utf-8') as f:
            json.dump(index_data, f, ensure_ascii=False, indent=4)
        print(f"Successfully updated index file: {index_file_path}")
        return True
        
    except Exception as e:
        print(f"Error writing index file: {e}")
        return False

def main():
    """
    Main function to run the update process
    """
    # You can modify this path to point to your Excel file
    excel_file_path = "sutraani/audio_timeline.xlsx"  # Replace with your Excel file path
    
    if not os.path.exists(excel_file_path):
        print(f"Error: Excel file not found: {excel_file_path}")
        print("Please update the excel_file_path variable in the script with the correct path.")
        return
    
    # Update the sutraani index
    success = update_sutraani_index_from_excel(excel_file_path)
    
    if success:
        print("Successfully updated sutraani index with Excel data!")
    else:
        print("Failed to update sutraani index.")

if __name__ == "__main__":
    main() 