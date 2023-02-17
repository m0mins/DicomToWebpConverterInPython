import os
from PIL import Image
import pydicom
input_dir =  r'/home/momin/DicomFiles/SourceFolder'
output_dir =  r'/home/momin/Converted/Destination'

def convert_dicom_to_webp(input_filename, input_dir, output_dir):
    # Load the DICOM file
    dicom_file = pydicom.dcmread(os.path.join(input_dir, input_filename))

    # Convert the DICOM file to a PIL Image object
    pil_image = Image.fromarray(dicom_file.pixel_array)

    # Save the PIL Image object as a WebP file in the output directory
    webp_filename = os.path.splitext(input_filename)[0] + ".webp"
    pil_image.save(os.path.join(output_dir, webp_filename), "WEBP")
    
print('Converted Successfully')


# Set the input and output directories


# Loop through all the DICOM files in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith(".dcm"):
        # Convert the DICOM file to WebP and move it to the output directory
        convert_dicom_to_webp(filename, input_dir, output_dir)
