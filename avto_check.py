def avto_raqam_tekshir_yuridik(raqam):
    natija=False
    if (
        type(raqam)==str and
        len(raqam)==8 and
        raqam[:5].isdigit() and
        raqam[5:].isupper()
    ):
        natija=True
    return natija
print(avto_raqam_tekshir_yuridik("60123AAA"))