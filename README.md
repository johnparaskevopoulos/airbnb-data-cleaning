# 🧼 Airbnb Data Cleaning Pipeline (Python & Pandas)

Αυτό το mini project υλοποιεί ένα μικρό ETL pipeline για καθαρισμό και ανάλυση δεδομένων Airbnb με χρήση Python και Pandas.

## 📁 Δομή Project

my_data_engineer_journey/
├── data/
│ ├── raw/ # Αρχικά (μη καθαρισμένα) δεδομένα
│ └── processed/ # Καθαρισμένα δεδομένα έτοιμα για analysis
├── reports/ # Αρχεία εξόδου (π.χ. PNG διαγράμματα)
├── notebooks/ # Εξερευνητικά Jupyter notebooks
├── src/ # Scripts σε μορφή CLI (π.χ. clean_airbnb.py)
├── README.md # Περιγραφή project


## 🔧 Περιγραφή

Το αρχείο `src/clean_airbnb.py`:

- Διαβάζει ένα CSV με καταχωρήσεις Airbnb
- Καθαρίζει τα δεδομένα (αφαίρεση NaN)
- Ομαδοποιεί ανά περιοχή και υπολογίζει μέσες τιμές
- Δημιουργεί bar chart και αποθηκεύει PNG report

## 🚀 Εκτέλεση

```bash
python src/clean_airbnb.py \
  --input data/raw/airbnb_athens.csv \
  --output data/processed/airbnb_cleaned.csv \
  --report reports/airbnb_report.png
```

Τα απαραίτητα directories θα δημιουργηθούν αυτόματα εάν δεν υπάρχουν.
