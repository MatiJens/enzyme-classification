from utils.get_features import get_features
from utils.load_fasta import load_fasta

enzyme_path = 'data/enzyme/enzyme.fasta'
not_enzyme_path = 'data/not_enzyme/not_enzyme.fasta'

enzyme, not_enzyme = load_fasta(enzyme_path, not_enzyme_path)

enzyme_features = get_features(enzyme)
not_enzyme_features = get_features(not_enzyme)

print(enzyme_features.head())
print(not_enzyme_features.head())