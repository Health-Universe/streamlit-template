"""Contains the `Home` page contents of the app."""
import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon="🏠",
)

st.title("Health Universe - Streamlit 📊")
st.divider()
st.markdown(
    """
**Welcome to the [Health Universe](https://www.healthuniverse.com) community!** Health Universe
is an open-source cloud deployment platform and community for  machine learning (ML) and AI from science to medicine.

This template provides a starter [Streamlit](https://streamlit.io/) application deployable to Health Universe.
"""
)

st.subheader("Structure")

st.markdown(
    """
The application is organized into a modular structure to enhance maintainability and scalability.
The directory structure includes a main Home.py file, a src module, and submodules such as
components, config, pages, and utils.

```plaintext
{your_folder_name_here}/
    ├── src/
    │   ├── components/
    │   │   └── __init__.py
    │   ├── config/
    │   │   └── __init__.py
    │   ├── pages/
    │   │   ├── 1_Demo.py
    │   │   ├── 2_Deploy.py
    │   │   └── __init__.py
    │   ├── schemas/
    │   │   ├── chads_vasc_score.py
    │   │   └── __init__.py
    │   ├── utils/
    │   │   ├── data_loader.py
    │   │   └── __init__.py
    │   └── __init__.py
    │── Home.py
    └── __init__.py
```
"""
)
