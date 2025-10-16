# Fingerprint Classification

íÇÏåÓÇÒí ÓÇÏå ÈÑÇí ÊÔÎíÕ ÇËÑÇäÔÊ ÈÇ ÇÓÊİÇÏå ÇÒ í˜ CNN ˜ãÍÌã. Çíä Ñæå äãæäåÇí ÇÒ ÑÏÇÒÔ ÊÕÇæíÑ ÇËÑÇäÔÊ¡ íÔÑÏÇÒÔ¡ ÂöãíäÊ (augmentation)¡ ÂãæÒÔ ãÏá æ íÔÈíäí Ñæí ÊÕÇæíÑ ÌÏíÏ ÑÇ ÇÑÇÆå ãíÏåÏ.

ÊæÌå: Çíä Ñæå ÕÑİÇğ ÈÑÇí ãŞÇÕÏ ÂãæÒÔí ÇÓÊ æ äÈÇíÏ ÏÑ ãÍíØåÇí ÍÓÇÓ íÇ ÈÇ ãÓÇÆá ÇãäíÊí ÇÓÊİÇÏå ÔæÏ ÈÏæä ÈÑÑÓíåÇí áÇÒã.

---

## ÊæÖíÍ ˜æÊÇå

- ÈÇÑĞÇÑí ÊÕÇæíÑ ÇËÑÇäÔÊ ÇÒ ÓÇÎÊÇÑ ÏÇíÑ˜ÊæÑí ãÔÎÕ
- íÔÑÏÇÒÔ ÊÕÇæíÑ (ÑÇíÓ˜ÇáÑ¡ ÇäÏÇÒå ËÇÈÊ)
- ÇİÒÇíÔ ÏÇÏå (augmentation) ÈÑÇí ÈåÈæÏ generalization
- ãÏá CNN ÓÇÏå ÈÑÇí ˜áÇÓÈäÏí Èå Ïæ ÏÓÊå
- ÊÇÈÚ íÔÈíäí ÈÑÇí ÊÕÇæíÑ ÌÏíÏ

---

## íÔäíÇÒåÇ

- Python 3.8+
- TensorFlow/Keras
- OpenCV
- NumPy
- scikit-learn

---

## äÕÈ æ ÑÇåÇäÏÇÒí

1) ÇíÌÇÏ ãÍíØ ãÌÇÒí
- Linux/macOS:
  - python3 -m venv venv
  - source venv/bin/activate
- Windows:
  - python -m venv venv
  - venv\Scripts\activate

2) äÕÈ æÇÈÓÊååÇ
- pip install -r requirements.txt

3) ÂãÇÏåÓÇÒí ÏÇÏååÇ
- ÏÇÏååÇ ÑÇ ÏÑ ÓÇÎÊÇÑ ÒíÑ ŞÑÇÑ ÏåíÏ:
  - dataset/
    - live/
    - fake/

4) ÂãæÒÔ ãÏá
- python fingerprint.py

5) íÔÈíäí ÈÇ í˜ ÊÕæíÑ ÌÏíÏ
- ÇÒ ÊÇÈÚ predict_fingerprint(image_path) ÏÑ fingerprint.py ÇÓÊİÇÏå ˜äíÏ.

---

## ÓÇÎÊÇÑ Ñæå (íÔäåÇÏ)

fingerprint_project/
??? fingerprint.py            # ˜Ï ÇÕáí ÂãæÒÔ¡ ÇÑÒíÇÈí æ íÔÈíäí
??? data_loader.py            # ÈÇÑĞÇÑí æ íÔÑÏÇÒÔ ÏÇÏååÇ
??? train.py                  # ÂãæÒÔ ãÏá (ÇÑ ÌÏÇ ÈÇÔÏ)
??? predict.py                # íÔÈíäí Ñæí ÊÕÇæíÑ ÌÏíÏ
??? dataset/
?   ??? live/
?   ??? fake/
??? requirements.txt
??? README.md
