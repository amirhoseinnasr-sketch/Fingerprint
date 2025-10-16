# Fingerprint Classification

��������� ���� ���� ����� ������� �� ������� �� � CNN �����. ��� ���� ������� �� ������ ������ ������ʡ ��ԝ�����ԡ ����� (augmentation)� ����� ��� � ��ԝ���� ��� ������ ���� �� ����� �����.

����: ��� ���� ����� ���� ����� ������ ��� � ����� �� ���؝��� ���� �� �� ����� ������ ������� ��� ���� �������� ����.

---

## ����� �����

- ��ѐ���� ������ ������� �� ������ ���ј���� ����
- ��ԝ������ ������ (����Ә��ѡ ������ ����)
- ������ ���� (augmentation) ���� ����� generalization
- ��� CNN ���� ���� ���ӝ���� �� �� ����
- ���� ��ԝ���� ���� ������ ����

---

## ��ԝ������

- Python 3.8+
- TensorFlow/Keras
- OpenCV
- NumPy
- scikit-learn

---

## ��� � ���������

1) ����� ���� �����
- Linux/macOS:
  - python3 -m venv venv
  - source venv/bin/activate
- Windows:
  - python -m venv venv
  - venv\Scripts\activate

2) ��� ��������
- pip install -r requirements.txt

3) ��������� ������
- ������ �� �� ������ ��� ���� ����:
  - dataset/
    - live/
    - fake/

4) ����� ���
- python fingerprint.py

5) ��ԝ���� �� � ����� ����
- �� ���� predict_fingerprint(image_path) �� fingerprint.py ������� ����.

---

## ������ ���� (�������)

fingerprint_project/
??? fingerprint.py            # �� ���� ����ԡ ������� � ��ԝ����
??? data_loader.py            # ��ѐ���� � ��ԝ������ ������
??? train.py                  # ����� ��� (ǐ� ��� ����)
??? predict.py                # ��ԝ���� ��� ������ ����
??? dataset/
?   ??? live/
?   ??? fake/
??? requirements.txt
??? README.md
