# Optical-Character-Recognition

To install all the necassary library 
```
make install
```

move to the api directory 
```
cd api
```

to run the fast api
```
fastapi dev main.py
```


The endpoint is a POST API at /ocr/. It expects:

    A file field in the request body with a PNG or JPEG image.
