# FastAPI Image Patcher
<img width="612" alt="image" src="https://github.com/mustafacavusoglu/Image-Patcher/assets/65891055/7a490c0e-7c3c-438b-9eb0-882eb649c59c">

This FastAPI application provides a simple image patching functionality. It allows you to upload an image, specify patching parameters, and receive patched images.
You can access app from [this link](https://patcher-r5zqyoknpa-uc.a.run.app/)

## Setup, You can access locally by this steps.

1. Clone the repository:

```bash
git clone https://github.com/mustafacavusoglu/Image-Patcher.git
```

2. Change Directory:

```bash
cd Image-Patcher
```

3. Install Packages:

```bash
pip install -r requirements.txt
```

4. Run Application:

```bash
uvicorn app:app --reload
```

## Usage
- Open your web browser and go to http://127.0.0.1:8000.

- You will see the main page with a form to upload an image.

- Upload an image and fill in the patching parameters (stride_x, stride_y, out).

- Click the "Patch Image" button.

- The patched images will be displayed on the result page.
