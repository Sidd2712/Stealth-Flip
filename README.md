# Stealth-Flip : Advanced Steganography Tool with Encryption
# Steath-Flip is an advanced steganography tool that allows you to hide files inside images using pixel manipulation. It also provides an additional layer of encryption using AES-256 for secure data hiding and extraction. The image is altered in a way that it remains visually unchanged to the human eye but contains secret information.

## Features
- Hide any file inside PNG, BMP, TIFF, or TGA images.
- Extract hidden files from carrier images.
- AES-256 encryption for secure file storage.
- Passphrase authentication to prevent unauthorized access.
- Image transformation (e.g., negative) for additional obfuscation.
- Compression of files before embedding to optimize space usage.
  
## Prerequisites

Before using Se, ensure you have the following installed:
- Python 3.x
- Required Python packages (can be installed via `pip`):


# To hide a file within an image, use the following command:
```bash
python secret_pixel.py hide <input_image_name> secret.txt <output_image_name>
```

# To extract a hidden file from an image, use the following command:
```bash
 python secret_pixel.py extract <encrypted_image_name> <file_name>
```
