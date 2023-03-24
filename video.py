import cv2

# Open the video file
video = cv2.VideoCapture("SI_on_SI.mp4")

# Initialize a frame counter and a frame index
frame_num = 0
frame_index = 0

# Calculate the frame skip factor based on the video length
num_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
frame_skip = max(num_frames // 10, 1)

# Loop through the video frames
while True:
    # Read a frame from the video
    ret, frame = video.read()

    # If the frame was not read successfully, break out of the loop
    if not ret:
        break

    # If the frame number is a multiple of the frame skip factor, save it as an image
    if frame_num % frame_skip == 0:
        cv2.imwrite(f"frame{frame_index}.jpg", frame)
        frame_index += 1

    # Increment the frame counter
    frame_num += 1

    # Stop the loop if we have saved the required number of frames
    if frame_index == 10:
        break

# Release the video file handle
video.release()

def rowing(rng, img_name):
    from PIL import Image

    # Open the 10 images
    images = []
    for i in rng:
        image_path = f"frame{i}.jpg"
        images.append(Image.open(image_path))

    # Resize the images to have the same height
    width, height = images[0].size
    new_height = 200
    new_width = int(width * new_height / height)
    for i in range(5):
        images[i] = images[i].resize((new_width, new_height))

    # Concatenate the images horizontally
    row_image = Image.new("RGB", (new_width * len(rng), new_height))
    for i in range(5):
        row_image.paste(images[i], (new_width * i, 0))

    # Save the row of images
    row_image.save(img_name)

rowing(range(5), "row_image_1.jpg")
rowing(range(5, 10, 1), "row_image_2.jpg")