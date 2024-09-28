import os
import shutil

OUT_TRAINING_PATH = "./traffic_light_images/training/all"

def main():
    color_path = {
        "green": "./traffic_light_images/training/green",
        "red": "./traffic_light_images/training/red", 
        "yellow": "./traffic_light_images/training/yellow"
    }
    
    for color in color_path:
        count = 0
        path = color_path[color]
        for image in os.listdir(path):
            count += 1
            ext = os.path.splitext(image)[1]
            shutil.copyfile(f"{path}/{image}", f"{OUT_TRAINING_PATH}/{color}{count}{ext}")
    
    
if __name__ == "__main__":
    main()