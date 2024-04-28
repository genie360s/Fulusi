import os
import subprocess

# Define spider names
spiders = [ 'amana', 'azania', 'baroda', 'boi', 'bot', 'dasheng', 'dcb', 'habib', 'icb', 'mkombozi', 'nmb', 'utt_amis']

# Loop through each spider
for spider in spiders:
    # Construct the file path
    file_path = f"data/{spider}.json"
    
    # Check if the JSON file already exists
    if os.path.exists(file_path):
        # If the file exists, delete it
        os.remove(file_path)
    
   
    command = f"scrapy crawl {spider} -o {file_path}"
    

    subprocess.run(command, shell=True)
