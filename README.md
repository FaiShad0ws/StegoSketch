# StegoSketch 
This project is a Python implementation of visible and invisible watermarking techniques for multimedia security.

Invisible watermarking uses Least Significant Bit (LSB) steganography techniques to embed data into the media's pixels, whereas visible watermarking adds the data as a visible overlay. 

<br>

## Requirement 
```
pip install Pillow
pip install stegano
```

<br>

## Instructions

```
1. install requirements
2. unzip the file and cd to the directory
3. run ./StegoSketch.py -h 
```

<br>


## Usage

```
$ ./StegoSketch.py -i image01.jpeg -d Secret-Data 
```

**Example - Invisible**
```
$ ./StegoSketch.py -i image01.jpeg -d Secret-Data

Secret Message Hidden Successfully 100% on: watermark_img.png  
```
<br>


**Example - Visible**

```
$ ./StegoSketch.py -v image02.jpeg -d Secret-Data

Secret Message Hidden Successfully 100% on: Steganography_img.png
Extracted Secret Message:  Secret-Data
```

<br>

