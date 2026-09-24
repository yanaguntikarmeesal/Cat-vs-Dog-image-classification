import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import os


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Cat vs Dog Image Classification",
    page_icon="🐱",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    /* ========================================================
       GLOBAL APPLICATION
       ======================================================== */

    .stApp {
        background:
            linear-gradient(
                135deg,
                #f8fafc 0%,
                #eef2ff 50%,
                #f8fafc 100%
            );

        color: #172033;
    }


    .main .block-container {
        padding-top: 1.5rem;
        padding-bottom: 2rem;
        max-width: 1350px;
    }


    /* ========================================================
       BANNER
       ======================================================== */

    .st-key-project_banner {
        background:
            linear-gradient(
                135deg,
                #111827 0%,
                #312e81 50%,
                #4c1d95 100%
            );

        border-radius: 24px;

        padding: 30px 35px;

        margin-bottom: 25px;

        box-shadow:
            0 15px 40px rgba(49, 46, 129, 0.25);

        border: 1px solid rgba(255, 255, 255, 0.10);
    }


    .st-key-project_banner h1 {
        color: #ffffff !important;

        font-size: 44px !important;

        font-weight: 850 !important;

        letter-spacing: -1px;

        margin-bottom: 5px !important;
    }


    .st-key-project_banner p {
        color: #dbeafe !important;

        font-size: 18px !important;
    }


    .st-key-project_banner .stCaption {
        color: #cbd5e1 !important;
    }


    /* ========================================================
       HEADINGS
       ======================================================== */

    h1 {
        color: #111827 !important;
        font-weight: 800 !important;
    }


    h2 {
        color: #1e293b !important;
        font-weight: 800 !important;
    }


    h3 {
        color: #334155 !important;
        font-weight: 750 !important;
    }


    /* ========================================================
       SIDEBAR
       ======================================================== */

    section[data-testid="stSidebar"] {
        background:
            linear-gradient(
                180deg,
                #eef2ff 0%,
                #f8fafc 55%,
                #e0e7ff 100%
            );

        border-right: 1px solid #dbe2f0;
    }


    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {
        color: #312e81 !important;
    }


    section[data-testid="stSidebar"] p {
        color: #334155 !important;
    }


    /* ========================================================
       FILE UPLOADER
       ======================================================== */

    [data-testid="stFileUploader"] {
        background: #ffffff;

        border: 2px dashed #818cf8;

        border-radius: 20px;

        padding: 20px;

        box-shadow:
            0 8px 25px rgba(49, 46, 129, 0.08);
    }


    [data-testid="stFileUploader"]:hover {
        border-color: #4f46e5;

        background: #fafaff;
    }


    /* ========================================================
       IMAGE
       ======================================================== */

    [data-testid="stImage"] {
        border-radius: 18px;

        overflow: hidden;

        box-shadow:
            0 10px 30px rgba(15, 23, 42, 0.10);
    }


    /* ========================================================
       METRIC CARDS
       ======================================================== */

    [data-testid="stMetric"] {
        background:
            linear-gradient(
                145deg,
                #ffffff,
                #f8fafc
            );

        border: 1px solid #e2e8f0;

        border-radius: 18px;

        padding: 20px;

        box-shadow:
            0 8px 25px rgba(15, 23, 42, 0.07);

        transition: all 0.2s ease;
    }


    [data-testid="stMetric"]:hover {
        transform: translateY(-3px);

        box-shadow:
            0 12px 30px rgba(15, 23, 42, 0.12);
    }


    [data-testid="stMetricLabel"] {
        color: #64748b !important;

        font-weight: 650 !important;
    }


    [data-testid="stMetricValue"] {
        color: #312e81 !important;

        font-weight: 850 !important;
    }


    /* ========================================================
       ALERTS
       ======================================================== */

    [data-testid="stAlert"] {
        border-radius: 16px;

        border: none;

        box-shadow:
            0 5px 18px rgba(15, 23, 42, 0.06);
    }


    /* ========================================================
       PROGRESS BAR
       ======================================================== */

    [data-testid="stProgressBar"] {
        margin-top: 8px;

        margin-bottom: 20px;
    }


    /* ========================================================
       EXPANDERS
       ======================================================== */

    [data-testid="stExpander"] {
        background: #ffffff;

        border: 1px solid #dbe2ea;

        border-radius: 17px;

        box-shadow:
            0 6px 20px rgba(15, 23, 42, 0.05);

        margin-top: 14px;
    }


    /* ========================================================
       BUTTONS
       ======================================================== */

    .stButton > button {
        width: 100%;

        background:
            linear-gradient(
                135deg,
                #4f46e5,
                #7c3aed
            );

        color: #ffffff;

        border: none;

        border-radius: 12px;

        padding: 12px 20px;

        font-size: 16px;

        font-weight: 700;

        transition: all 0.2s ease;
    }


    .stButton > button:hover {
        background:
            linear-gradient(
                135deg,
                #4338ca,
                #6d28d9
            );

        transform: translateY(-2px);

        box-shadow:
            0 8px 20px rgba(79, 70, 229, 0.25);
    }


    /* ========================================================
       DIVIDERS
       ======================================================== */

    hr {
        border: none;

        border-top: 1px solid #dbe2ea;

        margin-top: 28px;

        margin-bottom: 28px;
    }


    /* ========================================================
       CAPTIONS
       ======================================================== */

    .stCaption {
        color: #64748b !important;
    }


    /* ========================================================
       FOOTER
       ======================================================== */

    footer {
        visibility: hidden;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# PROJECT BANNER
# NO HTML CONTENT
# ============================================================

with st.container(key="project_banner"):

    st.title(
        "🐱 Cat vs Dog Image Classification 🐶"
    )

    st.write(
        "Deep Learning Image Classification using "
        "VGG16 Transfer Learning"
    )

    st.caption(
        "🧠 VGG16    •    🔄 Transfer Learning    •    "
        "🖼️ Image Classification    •    ⚡ TensorFlow"
    )


# ============================================================
# MODEL PATH
# ============================================================

MODEL_PATH = "catvsdog.h5"


# ============================================================
# LOAD MODEL
# ============================================================

@st.cache_resource
def load_model():

    if not os.path.exists(MODEL_PATH):

        return None

    model = tf.keras.models.load_model(
        MODEL_PATH,
        compile=False
    )

    return model


model = load_model()


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.header("🐾 About Project")

    st.write(
        """
        This application classifies an uploaded image
        as either a **Cat** or a **Dog** using a
        VGG16 transfer-learning model.
        """
    )

    st.divider()

    st.subheader("🧠 Model")

    st.write("**Architecture:** VGG16")

    st.write("**Transfer Learning:** ImageNet")

    st.write("**Input:** 224 × 224 × 3")

    st.write("**Output:** Binary Classification")

    st.write("**Optimizer:** Adam")

    st.write("**Loss:** Binary Crossentropy")

    st.divider()

    st.subheader("🐾 Classes")

    st.write("🐱 Cat")

    st.write("🐶 Dog")

    st.divider()

    st.info(
        "Upload a clear image of a cat or dog "
        "to get a prediction."
    )


# ============================================================
# MODEL CHECK
# ============================================================

if model is None:

    st.error(
        "⚠️ Model file `catvsdog.h5` was not found. "
        "Place it in the same folder as `app.py`."
    )

    st.stop()


else:

    st.success(
        "✅ VGG16 model loaded successfully."
    )


# ============================================================
# IMAGE UPLOAD
# ============================================================

st.header("📤 Upload an Image")

st.caption(
    "Choose a JPG, JPEG, PNG, BMP or WEBP image."
)


uploaded_file = st.file_uploader(
    "Choose a cat or dog image",
    type=[
        "jpg",
        "jpeg",
        "png",
        "bmp",
        "webp"
    ],
    help="Supported formats: JPG, JPEG, PNG, BMP and WEBP"
)


# ============================================================
# PREDICTION FUNCTION
# ============================================================

def predict_image(image, model):

    # Convert image to RGB
    image = image.convert("RGB")

    # Resize image
    image = image.resize(
        (224, 224)
    )

    # Convert to NumPy
    image_array = np.array(
        image,
        dtype=np.float32
    )

    # Add batch dimension
    image_array = np.expand_dims(
        image_array,
        axis=0
    )

    # Prediction
    prediction = model.predict(
        image_array,
        verbose=0
    )[0][0]

    # Classification
    if prediction >= 0.5:

        predicted_class = "Dog"

        confidence = prediction

    else:

        predicted_class = "Cat"

        confidence = 1 - prediction

    return (
        predicted_class,
        confidence,
        prediction
    )


# ============================================================
# PROCESS UPLOADED IMAGE
# ============================================================

if uploaded_file is not None:

    image = Image.open(
        uploaded_file
    )

    st.divider()


    # ========================================================
    # IMAGE + INFORMATION
    # ========================================================

    image_col, information_col = st.columns(
        [1.15, 1],
        gap="large"
    )


    # ========================================================
    # UPLOADED IMAGE
    # ========================================================

    with image_col:

        st.subheader("🖼️ Uploaded Image")

        st.image(
            image,
            caption=uploaded_file.name,
            use_container_width=True
        )


    # ========================================================
    # IMAGE INFORMATION
    # ========================================================

    with information_col:

        st.subheader("📋 Image Information")

        info1, info2 = st.columns(2)


        with info1:

            st.metric(
                "Format",
                image.format or "Unknown"
            )


        with info2:

            st.metric(
                "Image Size",
                f"{image.width} × {image.height}"
            )


        st.write("")


        st.info(
            "The image will be resized to "
            "**224 × 224 pixels** before prediction."
        )


    # ========================================================
    # PREDICTION
    # ========================================================

    st.divider()

    st.header("🔍 Prediction")


    predicted_class, confidence, raw_prediction = (
        predict_image(
            image,
            model
        )
    )


    # ========================================================
    # RESULT ICON
    # ========================================================

    if predicted_class == "Cat":

        result_icon = "🐱"

    else:

        result_icon = "🐶"


    # ========================================================
    # RESULT METRICS
    # ========================================================

    result_col1, result_col2, result_col3 = st.columns(
        3,
        gap="medium"
    )


    with result_col1:

        st.metric(
            "Prediction",
            f"{result_icon} {predicted_class}"
        )


    with result_col2:

        st.metric(
            "Confidence",
            f"{confidence * 100:.2f}%"
        )


    with result_col3:

        st.metric(
            "Raw Probability",
            f"{raw_prediction * 100:.2f}%"
        )


    # ========================================================
    # RESULT MESSAGE
    # ========================================================

    st.write("")


    if predicted_class == "Cat":

        st.success(
            f"🐱 The model predicts **Cat** "
            f"with **{confidence * 100:.2f}% confidence**."
        )

    else:

        st.info(
            f"🐶 The model predicts **Dog** "
            f"with **{confidence * 100:.2f}% confidence**."
        )


    # ========================================================
    # CONFIDENCE
    # ========================================================

    st.subheader("📊 Confidence")

    st.progress(
        float(confidence)
    )

    st.caption(
        f"Model confidence: "
        f"{confidence * 100:.2f}%"
    )


    # ========================================================
    # CLASS PROBABILITIES
    # ========================================================

    st.subheader("📈 Class Probabilities")


    cat_probability = (
        1 - raw_prediction
    )


    dog_probability = (
        raw_prediction
    )


    probability_col1, probability_col2 = st.columns(
        2,
        gap="medium"
    )


    with probability_col1:

        st.metric(
            "🐱 Cat",
            f"{cat_probability * 100:.2f}%"
        )

        st.progress(
            float(cat_probability)
        )


    with probability_col2:

        st.metric(
            "🐶 Dog",
            f"{dog_probability * 100:.2f}%"
        )

        st.progress(
            float(dog_probability)
        )


    # ========================================================
    # MODEL ARCHITECTURE
    # ========================================================

    st.divider()


    with st.expander(
        "🧠 View Model Architecture"
    ):

        st.write(
            "### VGG16 Transfer Learning"
        )

        st.write(
            """
            The project uses VGG16 with pretrained
            ImageNet weights.
            """
        )

        st.code(
            """
VGG16
   ↓
Flatten
   ↓
Dense(256, ReLU)
   ↓
Dense(1, Sigmoid)
            """,
            language="text"
        )

        st.write(
            """
            The VGG16 convolutional layers are frozen
            and the final classification layers are
            trained for Cat vs Dog classification.
            """
        )


    # ========================================================
    # PROJECT DETAILS
    # ========================================================

    with st.expander(
        "📚 Project Details"
    ):

        detail1, detail2 = st.columns(2)


        with detail1:

            st.write("### 🗂️ Dataset")

            st.write("🐱 Cats")

            st.write("🐶 Dogs")

            st.write(
                "**Input Size:** 224 × 224 × 3"
            )


        with detail2:

            st.write("### ⚙️ Training")

            st.write(
                "**Model:** VGG16"
            )

            st.write(
                "**Optimizer:** Adam"
            )

            st.write(
                "**Loss:** Binary Crossentropy"
            )

            st.write(
                "**Epochs:** 5"
            )


# ============================================================
# NO IMAGE MESSAGE
# ============================================================

else:

    st.info(
        "👆 Upload an image above to start "
        "Cat vs Dog classification."
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "🐱🐶 Cat vs Dog Image Classification "
    "• TensorFlow • VGG16 • Streamlit"
)

st.caption(
    "Developed by Yanaguntikar Meesal"
)

