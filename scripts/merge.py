import os
import json
import argparse
from typing import List, Dict, Any

def load_json_files(directory: str) -> List[Dict[str, Any]]:
    """
    Loads all JSON files from the specified directory.
    
    Args:
        directory (str): The path to the directory containing JSON files.
    
    Returns:
        List[Dict[str, Any]]: A list of dictionaries loaded from each JSON file.
    """
    json_files = [file for file in os.listdir(directory) if file.endswith('.json')]
    data_list: List[Dict[str, Any]] = []
    for file in json_files:
        path = os.path.join(directory, file)
        try:
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                data_list.append(data)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from file {path}: {e}")
    return data_list

def combine_keys(data_list: List[Dict[str, Any]]) -> Dict[str, List[Any]]:
    """
    Combines the values of keys "ai_providers", "AI_Types", and "AI_API_Services" 
    from a list of dictionaries into single lists.
    
    Args:
        data_list (List[Dict[str, Any]]): List of JSON-loaded dictionaries.
    
    Returns:
        Dict[str, List[Any]]: A dictionary with combined lists for the keys.
    """
    ai_providers: List[Any] = []
    AI_Types: List[Any] = []
    AI_API_Services: List[Any] = []
    
    for data in data_list:
        if 'ai_providers' in data and isinstance(data['ai_providers'], list):
            ai_providers.extend(data['ai_providers'])
        if 'AI_Types' in data and isinstance(data['AI_Types'], list):
            AI_Types.extend(data['AI_Types'])
        if 'AI_API_Services' in data and isinstance(data['AI_API_Services'], list):
            AI_API_Services.extend(data['AI_API_Services'])
    
    return {
        "ai_providers": ai_providers,
        "AI_Types": AI_Types,
        "AI_API_Services": AI_API_Services
    }

def save_combined_data(output_file: str, combined_data: Dict[str, List[Any]]) -> None:
    """
    Saves the combined data dictionary as a JSON file.
    
    Args:
        output_file (str): Path to the output JSON file.
        combined_data (Dict[str, List[Any]]): The dictionary containing the combined lists.
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(combined_data, f, indent=4)

def parse_arguments() -> argparse.Namespace:
    """
    Parses command-line arguments.
    
    Returns:
        argparse.Namespace: Parsed arguments with input directory and output file.
    """
    parser = argparse.ArgumentParser(
        description="Combine JSON files from a directory into a single JSON file."
    )
    parser.add_argument(
        '--input_dir',
        type=str,
        default="data/providers/",
        help="Directory containing JSON files (default: data/providers/)"
    )
    parser.add_argument(
        '--output_file',
        type=str,
        default="data/ai_api_services.json",
        help="Output JSON file path (default: data/ai_api_services.json)"
    )
    return parser.parse_args()

def main() -> None:
    args = parse_arguments()
    data_list = load_json_files(args.input_dir)
    combined_data = combine_keys(data_list)
    save_combined_data(args.output_file, combined_data)
    print(f"Combined JSON data has been saved to {args.output_file}")

if __name__ == "__main__":
    main()
