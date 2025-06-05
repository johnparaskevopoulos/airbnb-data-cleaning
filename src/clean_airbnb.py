# clean_airbnb.py

import pandas as pd
import matplotlib.pyplot as plt
import argparse
import os

def ensure_dir_exists(file_path):
    """Create parent directories for the given file if they don't exist."""
    directory = os.path.dirname(file_path)
    if directory:
        os.makedirs(directory, exist_ok=True)

# -----------------------------
# 🔹 Στάδιο 1: Καθαρισμός CSV
# -----------------------------
def clean_data(input_path, output_path):
    # Διαβάζουμε το αρχείο CSV από το path που έδωσε ο χρήστης
    df = pd.read_csv(input_path)

    # Αφαιρούμε γραμμές που περιέχουν NaN (κενές τιμές)
    df_cleaned = df.dropna()

    # Αποθηκεύουμε το καθαρισμένο αρχείο σε νέο path
    ensure_dir_exists(output_path)
    df_cleaned.to_csv(output_path, index=False)

    return df_cleaned

# --------------------------------------
# 🔹 Στάδιο 2: Δημιουργία διαγράμματος
# --------------------------------------
def generate_report(df, report_path):
    # Ομαδοποιούμε τα δεδομένα ανά neighborhood
    grouped = df.groupby("neighborhood").agg({
        "price": "mean"
    }).reset_index()

    # Δημιουργούμε ράβδο-διάγραμμα (bar chart)
    plt.figure(figsize=(8, 4))
    plt.bar(grouped["neighborhood"], grouped["price"], color='cornflowerblue')
    plt.title("Μέση Τιμή Airbnb ανά Περιοχή")
    plt.xlabel("Περιοχή")
    plt.ylabel("Τιμή (€)")
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Αποθηκεύουμε το διάγραμμα σε PNG αρχείο
    ensure_dir_exists(report_path)
    plt.savefig(report_path)
    print(f"✅ Report saved to {report_path}")

# -------------------------------------
# 🔹 Κεντρική λογική του προγράμματος
# -------------------------------------
def main():
    # Ορίζουμε παραμέτρους που θα δίνει ο χρήστης από το terminal
    parser = argparse.ArgumentParser(description="Καθαρισμός Airbnb CSV και δημιουργία report")
    parser.add_argument("--input", required=True, help="Διαδρομή στο αρχικό αρχείο CSV")
    parser.add_argument("--output", required=True, help="Διαδρομή για αποθήκευση cleaned CSV")
    parser.add_argument("--report", required=True, help="Διαδρομή PNG report")

    args = parser.parse_args()

    # Αν δεν υπάρχει το αρχείο εισόδου → εμφάνιση μηνύματος
    if not os.path.exists(args.input):
        print("❌ Το input αρχείο δεν υπάρχει.")
        return

    print("📥 Καθαρισμός δεδομένων...")
    cleaned_df = clean_data(args.input, args.output)

    print("📊 Δημιουργία διαγράμματος...")
    generate_report(cleaned_df, args.report)

    print("🎉 Ολοκληρώθηκε!")

# Εκτελεί το main μόνο όταν καλείται από terminal
if __name__ == "__main__":
    main()
