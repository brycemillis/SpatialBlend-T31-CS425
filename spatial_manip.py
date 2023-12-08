from PIL import Image
import numpy as np

def resize_to_smallest(image1, image2):
    # Find the smallest dimensions between the two images
    min_width = min(image1.size[0], image2.size[0])
    min_height = min(image1.size[1], image2.size[1])

    # Resize both images to these dimensions
    image1 = image1.resize((min_width, min_height))
    image2 = image2.resize((min_width, min_height))

    return image1, image2


def low_pass_filter(image, cutoff_frequency=20):     
    # Fourier transform
    f_transform = np.fft.fft2(image)
    f_transform_shifted = np.fft.fftshift(f_transform)

    rows, cols = image.shape
    crow, ccol = rows//2, cols//2

    # Create a low-pass filter
    mask = np.zeros((rows, cols), np.uint8)
    mask[crow-cutoff_frequency:crow+cutoff_frequency, ccol-cutoff_frequency:ccol+cutoff_frequency] = 1

    # Apply filter and inverse DFT
    f_transform_shifted *= mask
    f_transform = np.fft.ifftshift(f_transform_shifted)
    image_back = np.fft.ifft2(f_transform)
    image_back = np.abs(image_back)

    return image_back

def high_pass_filter(image, cutoff_frequency=20):
    # Fourier transform
    f_transform = np.fft.fft2(image)
    f_transform_shifted = np.fft.fftshift(f_transform)

    rows, cols = image.shape
    crow, ccol = rows//2, cols//2

    # Create a high-pass filter
    mask = np.ones((rows, cols), np.uint8)
    mask[crow-cutoff_frequency:crow+cutoff_frequency, ccol-cutoff_frequency:ccol+cutoff_frequency] = 0

    # Apply filter and inverse DFT
    f_transform_shifted *= mask
    f_transform = np.fft.ifftshift(f_transform_shifted)
    image_back = np.fft.ifft2(f_transform)
    image_back = np.abs(image_back)

    return image_back

def create_hybrid_image(image_file1, image_file2, output_file, low_pass_cutoff, high_pass_cutoff):
    # Load images and convert to grayscale
    image1 = Image.open(image_file1).convert('L')
    image2 = Image.open(image_file2).convert('L')

    # Resize images to the smallest common size
    image1, image2 = resize_to_smallest(image1, image2)

    # Convert images to numpy arrays
    image1_array = np.array(image1)
    image2_array = np.array(image2)

    # Apply filters with different cutoff frequencies
    low_pass_image = low_pass_filter(image1_array, low_pass_cutoff)
    high_pass_image = high_pass_filter(image2_array, high_pass_cutoff)

    # Save the low pass and high pass images
    Image.fromarray(low_pass_image.astype(np.uint8)).convert("RGB").save('low_pass_image.png')
    Image.fromarray(high_pass_image.astype(np.uint8)).convert("RGB").save('high_pass_image.png')

    # Combine the images
    hybrid_image = low_pass_image + high_pass_image - np.mean(high_pass_image)

    # Normalize and convert back to image
    hybrid_image = np.clip(hybrid_image, 0, 255)
    hybrid_image = Image.fromarray(hybrid_image.astype(np.uint8))
    hybrid_image = hybrid_image.convert("RGB")
    hybrid_image.save(output_file)

# Example usage
create_hybrid_image('shrek.jpg', 'harry.jpg', 'hybrid_image.png', low_pass_cutoff=20, high_pass_cutoff=40)
