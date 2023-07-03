# StegoSketch 

## Requirement 
```
!pip install Pillow
!pip install stegano
```

<br>

## Instructions

```
1. install requirements
2. unzip the file, cd to the directory and run it!
```

```
gcc -O3 ChaCha.c ChaCha.h -o ChaCha
```

<br>
<br>

## Usage

```
./StegoSketch.py -i image01.jpeg -d Secret-Data 
```

**Example - Visible**

```
$ ./StegoSketch.py -i image01.jpeg -d Secret-Data

Secret Message Hidden Successfully 100% on: Steganography_img.png
Extracted Secret Message:  Secret-Data
```

<br>

**Example -Invisible**
```
$ ./StegoSketch.py -v image01.jpeg -d Secret-Data 
Secret Message Hidden Successfully 100% on: watermark_img.png
   
```
