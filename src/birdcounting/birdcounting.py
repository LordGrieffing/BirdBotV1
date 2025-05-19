import pandas as pd
import os
import csv


def main():
    
    # Folder Labels
    image_Folder = "unclassifiedImages/"
    finished_Image_Folder = "classifiedImages/"
    classified_Results = "birdData/"
    results_file = "results.csv"
    results_Path = os.path.join(classified_Results, results_file)

    # CSV labels
    labels = ['Species', 'Year', 'Month', 'Day', 'Hour']


    # Make sure directories exist, if not create directories
    os.makedirs(image_Folder, exist_ok=True)
    os.makedirs(finished_Image_Folder, exist_ok=True)
    os.makedirs(classified_Results, exist_ok=True)

    # Make sure csv file exists if not make it
    if not os.path.exists(results_Path):
        with open(results_Path, mode='w', newline="") as f:
            writer = csv.writer(f)
            writer.writerow(labels)

    # Read csv as dataframe
    birdbata = pd.read_csv(results_Path)
    
    
    
    
    
    pass

















































if __name__ == "__main__":
    main()