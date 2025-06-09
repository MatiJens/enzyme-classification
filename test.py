from Bio import SeqIO
import os

# --- WAŻNE ---
# Użyj DOKŁADNIE TEJ SAMEJ zmiennej 'path', co w Twoim głównym skrypcie!
path = 'data/' # <-- ZMIEŃ NA SWOJĄ ŚCIEŻKĘ

file_to_check = os.path.join(path, "EC1.fasta")

print(f"Próbuję otworzyć plik: {file_to_check}")

try:
    # Używamy list(), aby "zmusić" iterator do działania i policzenia elementów
    records = list(SeqIO.parse(file_to_check, "fasta"))
    
    if len(records) > 0:
        print(f"\nSUKCES! Znaleziono {len(records)} sekwencji w pliku.")
        for i, record in enumerate(records):
            if 180 >= len(record.seq) > 25:
                print(f"{i} sekwencja ma {len(record.seq)} znaków")
                break
    else:
        print(f"\nBŁĄD KRYTYCZNY: Plik istnieje, ale jest pusty lub nie zawiera poprawnych danych FASTA.")
        print("Liczba znalezionych sekwencji: 0")

except FileNotFoundError:
    print(f"\nBŁĄD KRYTYCZNY: Nie znaleziono pliku pod podaną ścieżką.")
except Exception as e:
    print(f"\nWYSTĄPIŁ INNY BŁĄD: {e}")