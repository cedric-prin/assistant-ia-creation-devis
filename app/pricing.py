def calcul_prix(lignes):
    total_ht = sum(l["quantite"] * l["prix_unitaire"] for l in lignes)
    tva = round(total_ht * 0.20, 2)
    total_ttc = round(total_ht + tva, 2)

    return {
        "total_ht": round(total_ht, 2),
        "tva": tva,
        "total_ttc": total_ttc
    }
