import pandas as pd
import numpy as np
import os
import csv
import shutil
from ultralytics import YOLO

def countDistinct(boxes):

    res = 1

    for i in range(1, boxes.shape[0]):
        j = 0
        for j in range(i):
            if (boxes[i].cls.item() == boxes[j].cls.item()):
                break

        if (i == j + 1):
            res += 1

    return res

def main():

    # Load the Yolo model
    model = YOLO("/home/jacob/BirdBotV1/localmodeltest/100epochSet2.pt")
    
    # Folder Labels
    image_Folder = "unclassifiedImages/"
    finished_Image_Folder = "classifiedImages/"
    classified_Results = "birdData/"
    results_file = "results.csv"
    results_Path = os.path.join(classified_Results, results_file)

    # CSV labels
    labels = ['Species', 'Quantity', 'Year', 'Month', 'Day', 'Hour']


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
    birddata = pd.read_csv(results_Path)

    # List to store new rows being added
    new_rows = []
    #specimen_count = np.empty((1,2))
    
    
    # Loop through all the images in the unclassified folder
    for filename in os.listdir(image_Folder):

        # Get date and time information of the image
        year = filename[:4]
        month = filename[4:6]
        day = filename[6:8]
        hour = filename[8:10]

        # Get a path to the image
        file_path = os.path.join(image_Folder, filename)

        try:

            # Run the model over the image
            results = model(file_path)

            # Parse results
            boxes = results[0].boxes

            #species_count = countDistinct(boxes)

            # Cycle through spotted birds
            for box in boxes:
                class_id = int(box.cls.item())
                bird_species = results[0].names[class_id]

                # Add entry
                new_rows.append([bird_species, year, month, day, hour])
                birddata.index = birddata.index + 1

            # Move file out of unclassfied files
            shutil.move(file_path, os.path.join(finished_Image_Folder, filename))

        except Exception as e:
            print(f"Error processing {filename}: {e}")


    # Update birddata
    temp_frame = pd.DataFrame(new_rows, columns=labels)
    birddata = pd.concat([temp_frame, birddata], ignore_index=True)

    # Save updated data frame
    birddata.to_csv(results_Path)



if __name__ == "__main__":
    main()