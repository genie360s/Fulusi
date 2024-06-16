import os
import subprocess

# Define spider names
spiders = [ 'amana', 'azania', 'baroda', 'boi', 'bot', 'dasheng', 'dcb', 'habib', 'icb', 'mkombozi', 'nmb', 'utt_amis', 'faida']

# Loop through each spider
for spider in spiders:
   
    command = f"scrapy crawl {spider}"
    
    subprocess.run(command, shell=True)
