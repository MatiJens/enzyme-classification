from esm.models.esmc import ESMC

def initialize_esm_client():
    global _client
    if _client is None:
        _client = ESMC.from_pretrained("esmc_300m").to("cuda")