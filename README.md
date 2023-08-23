# Health Universe - Streamlit Template 📊

This template provides a starter Streamlit application for deploying to Health Universe.

## Local Quickstart

In the root directory, open your console and run:

```console
pip install -r requirements.txt
```

Then, run the following command to start the application:

```console
cd src && streamlit run home.py
```

## Structure

This repository is organized into a modular structure to enhance maintainability and scalability.
The directory includes a main home.py file, a src module, and submodules
components, config, pages, schemas, and utils.

```plaintext
{your_folder_name_here}/
    ├── src/
    │   ├── components/
    │   │   └── __init__.py
    │   ├── config/
    │   │   └── __init__.py
    │   ├── pages/
    │   │   ├── 1_demo.py
    │   │   ├── 2_deploy.py
    │   │   └── __init__.py
    │   ├── schemas/
    │   │   ├── chads_vasc_score.py
    │   │   └── __init__.py
    │   ├── utils/
    │   │   ├── data_loader.py
    │   │   └── __init__.py
    │   └── __init__.py
    │── home.py
    └── __init__.py
```
