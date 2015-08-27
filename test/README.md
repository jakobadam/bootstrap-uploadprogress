# Bootstrap UploadProgress test using Django

This is a test of bootstrap-uploadprogress using Django. It uses
uploading of software packages -- which are usually large files -- to
demonstrate the functionality.

## Getting started

Install Django and friends
```
$ pip install -r requirements.txt
```

Install Javascript prerequisites
```
$ ./manange.py bower install
```

Run development server
```
$ ./manage.py runserver
```

## Test

Point browser to http://localhost:8000

```
$ firefox localhost:8080
```

Go and upload something big.
