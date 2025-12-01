import os
from PIL import Image

def compress_images(directory):
    # Supported extensions to look for
    extensions = ['.jpg', '.jpeg', '.png', '.JPG', '.JPEG', '.PNG']
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_name, file_ext = os.path.splitext(file)
            
            if file_ext in extensions:
                try:
                    # Check file size (700 KB = 700 * 1024 bytes)
                    file_size = os.path.getsize(file_path)
                    target_quality = 85
                    
                    with Image.open(file_path) as img:
                        # Convert to RGB if necessary (e.g. for PNGs with transparency)
                        if img.mode in ('RGBA', 'P'):
                            img = img.convert('RGB')
                        
                        # If file is larger than 700KB, apply more aggressive compression
                        if file_size > 700 * 1024:
                            print(f"Large file detected ({file_size/1024:.2f} KB): {file}")
                            target_quality = 60
                            
                            # Also resize if dimensions are huge (e.g. > 1920px)
                            max_dimension = 1920
                            if max(img.size) > max_dimension:
                                # Use Image.Resampling.LANCZOS for Pillow >= 9.0, or Image.LANCZOS for older
                                resample_method = getattr(Image, 'Resampling', Image).LANCZOS
                                img.thumbnail((max_dimension, max_dimension), resample_method)
                                print(f"Resized to max {max_dimension}px")

                        # Define new file path with .jpg extension
                        new_file_path = os.path.join(root, file_name + ".jpg")
                        
                        # Save as JPG with compression
                        img.save(new_file_path, "JPEG", quality=target_quality, optimize=True)
                        print(f"Compressed and saved: {new_file_path}")
                        
                        # If the original file was not .jpg, remove it
                        if file_path != new_file_path:
                            os.remove(file_path)
                            print(f"Removed original: {file_path}")
                            
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")

if __name__ == "__main__":
    # Path to the assets/images folder relative to this script
    images_dir = os.path.join("src", "assets", "images")
    
    if os.path.exists(images_dir):
        print(f"Starting compression in {images_dir}...")
        compress_images(images_dir)
        print("Compression complete.")
        print("NOTE: Since file extensions may have changed to .jpg, please update your HTML files to reference the new .jpg filenames.")
    else:
        print(f"Directory not found: {images_dir}")
