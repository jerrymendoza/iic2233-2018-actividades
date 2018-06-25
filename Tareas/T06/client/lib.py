def nota_octava(nota,octava):

    if nota>12 or nota<1 or octava>10 or octava<0:
        return None
    else:
        return (nota-1)+(octava)*12
