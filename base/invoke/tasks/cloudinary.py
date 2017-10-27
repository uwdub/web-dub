import cloudinary
import cloudinary.uploader
import cloudinary.utils
import hashlib
import invoke
import os
import requests
import yaml


@invoke.task()
def compile_people_images():
    # Obtain our stored people data
    with open('_compile-people-images.yml') as f:
        people = yaml.safe_load(f)['people']

    # Iterate over all our people files
    people_paths = []
    for people_root_entry, people_dir_entries, people_file_entries in os.walk('_people'):
        # Skip the images directories
        if '_images_raw' in people_dir_entries:
            people_dir_entries.remove('_images_raw')
        # Skip the unchecked directories
        if '_unchecked' in people_dir_entries:
            people_dir_entries.remove('_unchecked')
        # Skip any template files
        if 'template.md' in people_file_entries:
            people_file_entries.remove('template.md')

        # Keep only .md files
        people_file_entries = [
            people_file_current
            for people_file_current
            in people_file_entries
            if os.path.splitext(people_file_current)[1] == '.md'
        ]

        for file_entry_current in people_file_entries:
            people_paths.append(
                os.path.normpath(
                    os.path.join(people_root_entry, file_entry_current)
                )
            )

    # Go through the corresponding images
    for people_path_current in people_paths:
        # Get a base without the extension
        people_path_current_base = os.path.splitext(people_path_current)[0]
        # Convert that into an image base
        people_path_current_image_raw_base = os.path.join(
            os.path.split(people_path_current_base)[0],
            '_images_raw',
            os.path.split(people_path_current_base)[1]
        )
        people_path_current_image_normalized = os.path.join(
            people_path_current_base + '.jpg'
        )

        # Check if a corresponding image exists
        people_path_current_image_raw = None
        if os.path.exists(people_path_current_image_raw_base + '.jpg'):
            people_path_current_image_raw = people_path_current_image_raw_base + '.jpg'
        elif os.path.exists(people_path_current_image_raw_base + '.png'):
            people_path_current_image_raw = people_path_current_image_raw_base + '.png'

        # If we have an image for this person, check whether it needs normalized
        if people_path_current_image_raw:
            # Handle a case where this is a new person
            if people_path_current not in people:
                people[people_path_current] = {
                    'image_hash': '',
                }

            # Our parameters are part of the hash
            params_cloudinary = {
                'width': 150,
                'height': 150,
                'crop': 'thumb',
                'gravity': 'auto'
            }

            # Get the hash from the file, to compare against our stored data
            md5 = hashlib.md5()
            md5.update(repr(sorted(params_cloudinary.items())).encode('utf-8'))
            with open(people_path_current_image_raw, 'rb') as f:
                md5.update(f.read())
            image_hash_current = md5.hexdigest()

            # Get the hash we have previously processed
            image_hash_stored = people[people_path_current]['image_hash']

            # If the image has changed, we need to process it
            if image_hash_current != image_hash_stored:
                # Normalizing will require Cloudinary
                if os.path.exists('secrets/cloudinary.yml'):
                    with open('secrets/cloudinary.yml') as f:
                        secrets_cloudinary = yaml.safe_load(f)['secrets']

                    cloudinary.config(
                        cloud_name=secrets_cloudinary['cloud_name'],
                        api_key=secrets_cloudinary['api_key'],
                        api_secret=secrets_cloudinary['api_secret'],
                    )

                    cloudinary_image_id = os.path.split(people_path_current_base)[1]

                    cloudinary.uploader.upload(
                        people_path_current_image_raw,
                        public_id=cloudinary_image_id
                    )

                    cloudinary_image_url = cloudinary.utils.cloudinary_url(
                        cloudinary_image_id,
                        **params_cloudinary
                    )[0]

                    # Download the image
                    response = requests.get(cloudinary_image_url, stream=True)
                    with open(people_path_current_image_normalized, 'wb') as f:
                        f.write(response.content)

                    # Store the hash we used to compute this
                    people[people_path_current] = {
                        'image_hash': image_hash_current,
                    }

    # Store our updated people
    data = {'people': people}
    with open('_compile-people-images.yml', 'w') as f:
        yaml.dump(
            data,
            stream=f,
            default_flow_style=False
        )
