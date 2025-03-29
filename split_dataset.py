import os, shutil, random

# -------------------------------
# Configuration
# -------------------------------
DATASET_DIR = "./AID"  
OUTPUT_DIR = "./data"  
TRAIN_RATIO = 0.8

# Create output directories
train_dir = os.path.join(OUTPUT_DIR, "train")
val_dir = os.path.join(OUTPUT_DIR, "val")
os.makedirs(train_dir, exist_ok=True)
os.makedirs(val_dir, exist_ok=True)

# -------------------------------
# Split Dataset
# -------------------------------
def split_dataset():
    categories = os.listdir(DATASET_DIR)
    
    for category in categories:
        category_path = os.path.join(DATASET_DIR, category)
        if not os.path.isdir(category_path):
            continue  # Skip non-folder files
        
        images = os.listdir(category_path)
        random.shuffle(images)  # Shuffle images for randomness
        
        split_idx = int(len(images) * TRAIN_RATIO)
        train_images = images[:split_idx]
        val_images = images[split_idx:]
        
        # Create class directories in train and val folders
        os.makedirs(os.path.join(train_dir, category), exist_ok=True)
        os.makedirs(os.path.join(val_dir, category), exist_ok=True)
        
        # Move images to train folder
        for img in train_images:
            shutil.copy(os.path.join(category_path, img), os.path.join(train_dir, category, img))
        
        # Move images to validation folder
        for img in val_images:
            shutil.copy(os.path.join(category_path, img), os.path.join(val_dir, category, img))
        
        print(f"Processed {category}: {len(train_images)} train, {len(val_images)} val")


if __name__ == "__main__":
    split_dataset()
    print("✅ Dataset splitting complete!")
