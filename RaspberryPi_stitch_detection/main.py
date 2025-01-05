import cv2
import numpy as np

def load_image(path):
    """Load an image from the file path."""
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise FileNotFoundError(f"Image not found at {path}")
    return image

def match_images(master_image, slave_image):
    """Match slave image to master image and determine if the stitching matches."""
    # Initialize ORB detector
    orb = cv2.ORB_create()

    # Find keypoints and descriptors with ORB
    kp1, des1 = orb.detectAndCompute(master_image, None)
    kp2, des2 = orb.detectAndCompute(slave_image, None)

    # Create BFMatcher object with ratio test
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=False)

    # Match descriptors
    matches = bf.knnMatch(des1, des2, k=2)

    # Apply ratio test
    good_matches = []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            good_matches.append(m)

    # Determine a threshold for good matches
    min_good_matches = 10
    if len(good_matches) >= min_good_matches:
        result = "Pass"
    else:
        result = "Fail"

    # Draw and visualize matches
    master_image_color = cv2.cvtColor(master_image, cv2.COLOR_GRAY2BGR)
    slave_image_color = cv2.cvtColor(slave_image, cv2.COLOR_GRAY2BGR)
    img_matches = cv2.drawMatches(master_image_color, kp1, slave_image_color, kp2, good_matches, None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

    # Resize image to be small
    max_size = 800  # Define a maximum size for the longest side of the image
    height, width = img_matches.shape[:2]
    if width > max_size or height > max_size:
        if width > height:
            scale = max_size / width
        else:
            scale = max_size / height
        new_width = int(width * scale)
        new_height = int(height * scale)
        resized_img = cv2.resize(img_matches, (new_width, new_height))
    else:
        resized_img = img_matches

    # Display the resized image
    cv2.imshow('Matches', resized_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return result

def main(master_image_path, slave_image_path):
    try:
        # Load images
        master_image = load_image(master_image_path)
        slave_image = load_image(slave_image_path)

        # Match images
        result = match_images(master_image, slave_image)
        print(f"Matching result: {result}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Replace these paths with the paths to your images
    master_image_path = "stitch.jpeg"
    slave_image_path = "no3.jpeg"
    main(master_image_path, slave_image_path)
