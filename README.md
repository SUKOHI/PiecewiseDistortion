# PiecewiseDistortion
A python package to manage image distortion.

# Requirements

1. numpy
2. scikit-image
3. PIL (pillow)

# Installation

    pip install piecewise_distortion

# Usage

    import piecewise_distortion as pd

    file_path = 'lena.jpg'  
    roi_points = [(100,100),(400,100),(400,400),(100,400)]  
    from_points = [(300,300),(250,250)]  
    to_points = [(350,350),(200,200)]  

    dt = pd.PiecewiseDistortion(roi_points)
    distorted_im = dt.get_distorted_image(pil_im, from_points, to_points)

# Example

![Example](http://i.imgur.com/GdCkRpKl.jpg)

# License

This package is licensed under the MIT License.  
Copyright 2017 Sukohi Kuhoh
