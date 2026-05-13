import httpx, json, re


def clean_accession(acession_id):
    ids = acession_id.split("_", maxsplit=1)
    primary_id = ids[0]
    return primary_id


def download_sequence(id):
    params = {"fields": ["sequence"]}
    headers = {"accept": "application/json"}
    base_url = f"https://rest.uniprot.org/uniprotkb/{id}"

    try:
        data = (
            httpx.get(
                url=base_url, params=params, headers=headers, follow_redirects=True
            )
            .raise_for_status()
            .json()
        )

        sequence = data["sequence"]["value"]

        return sequence

    except Exception as e:
        print(f"HTTP error occured: {e}")


def find_motif(sequence):
    motif_pattern = "(?=(N[^P][ST][^P]))"
    matches = list(
        re.finditer(pattern=motif_pattern, string=sequence, flags=re.I | re.X)
    )

    if matches:
        match_positions = [m.start() + 1 for m in matches]
        return " ".join([str(p) for p in match_positions])
    else:
        return None


if __name__ == "__main__":
    with open("./datasets/rosalind_mprt.txt") as f:
        uniprot_ids = [id for id in f.read().strip().splitlines()]

    primary_ids = [clean_accession(id) for id in uniprot_ids]

    for uniprot_id, primary_id in zip(uniprot_ids, primary_ids):

        sequence = download_sequence(primary_id)
        motif_positions = find_motif(sequence)

        if motif_positions:
            print(uniprot_id)
            print(motif_positions)
