#
# process-faculty-images.py
#
# Detect face regions in raw faculty profile images via AWS Rekognition, and
# save cropped versions.
#
# Usage (from root of project): invoke process_faculty_images
# 

import os
import io
import glob
import invoke
import boto3
from PIL import Image


os.environ['AWS_CONFIG_FILE'] = 'secrets/aws-config'
IMAGES_DIRECTORY = '_people/faculty'

def bound_lower(val, bound):
  return val if val > bound else bound

def bound_upper(val, bound):
  return val if val < bound else bound

@invoke.task()
def process_faculty_images():
  if not os.path.exists(os.environ['AWS_CONFIG_FILE']):
    print('Error: Missing credentials file %s. Aborting.' % os.environ['AWS_CONFIG_FILE'])
    return

  # find all files in need of processing. We assume that if we have a *-raw
  # file and no corresponding *-processed file, we need to process this file.
  img_types = ('.jpg', '.jpeg', '.png')
  unprocessed_images = []
  for img_type in img_types:
    for image in glob.glob(os.path.join(IMAGES_DIRECTORY, '*-raw' + img_type)):
      base_filename = os.path.basename(image).rstrip(img_type).split('-raw')[0]
      if not os.path.exists(os.path.join(IMAGES_DIRECTORY, base_filename +
                                         '-processed' + img_type)):
        unprocessed_images.append(image)

  # establish a connection to the Rekognition service
  session = boto3.Session(profile_name='rekognition')
  client = boto3.client('rekognition')

  # process images
  num_processed_images = 0
  for image in unprocessed_images:
    print('Processing', image)
    img = Image.open(image)
    img_bytes = io.BytesIO()
    img.save(img_bytes, format=img.format)

    # send unprocessed image to Rekognition for face detection
    response = client.detect_faces(
      Image={
        'Bytes': img_bytes.getvalue()
      },
      Attributes=[
        'DEFAULT'
      ]
    )

    # Rekognition returns bounding box information as a percentage of original
    # image dimensions, so we multiply those values by our image width and height, 
    # plus some padding. We also make sure that the padding doesn't extend past
    # the dimensions of the original image.
    # TODO: how well will fixed padding values work in general?
    b_box = response['FaceDetails'][0]['BoundingBox']
    img_width, img_height = img.size
    padding_left, padding_top, padding_bottom, padding_right = (100, 150, 200, 200)
    face_left = bound_lower((b_box['Left']*img_width) - padding_left, 0)
    face_top = bound_lower((b_box['Top']*img_height) - padding_top, 0)
    face_width = b_box['Width']*img_width
    face_height = b_box['Height']*img_height
    face_right = bound_upper(face_left + face_width + padding_right, img_width)
    face_bottom = bound_upper(face_top + face_height + padding_bottom, img_height)

    # save the final cropped image
    img_type = '.' + img.format.lower()
    base_filename = os.path.basename(image).rstrip(img_type).split('-raw')[0]
    (img.crop((face_left, face_top, face_right, face_bottom))
        .save(os.path.join(IMAGES_DIRECTORY, base_filename + 
                           '-processed' + img_type)))
    num_processed_images += 1

    # remove the raw image
    os.remove(os.path.join(IMAGES_DIRECTORY, base_filename + '-raw' + img_type))

  print('Done! Processed %d images' % num_processed_images)
