from django.db import models

class Hemocentro(models.Model):
    NOME_CHOICES = [
        ('FUNDAÇÃO PRÓ-SANGUE', 'FUNDAÇÃO PRÓ-SANGUE'),
        ('UNIFESP', 'UNIFESP'),
        ('SANTA CASA', 'SANTA CASA'),
        ('COLSAN', 'COLSAN'),
        ('UNICAMP', 'UNICAMP'),
        ('RIBEIRÃO PRETO', 'RIBEIRÃO PRETO'),
        ('SÃO JOSÉ DO RIO PRETO', 'SÃO JOSÉ DO RIO PRETO'),
        ('MARILIA', 'MARILIA'),
        ('BOTUCATU', 'BOTUCATU'),
    ]
    nome = models.CharField(max_length=100, choices=NOME_CHOICES)

    class Meta:
        app_label = 'estoque'

class EstoqueSangue(models.Model):
    hemocentro = models.ForeignKey(Hemocentro, on_delete=models.CASCADE)
    estoque_atual_A_positivo = models.IntegerField(default=0)
    estoque_minimo_A_positivo = models.IntegerField(default=0)
    estoque_atual_A_negativo = models.IntegerField(default=0)
    estoque_minimo_A_negativo = models.IntegerField(default=0)
    estoque_atual_B_positivo = models.IntegerField(default=0)
    estoque_minimo_B_positivo = models.IntegerField(default=0)
    estoque_atual_B_negativo = models.IntegerField(default=0)
    estoque_minimo_B_negativo = models.IntegerField(default=0)
    estoque_atual_AB_positivo = models.IntegerField(default=0)
    estoque_minimo_AB_positivo = models.IntegerField(default=0)
    estoque_atual_AB_negativo = models.IntegerField(default=0)
    estoque_minimo_AB_negativo = models.IntegerField(default=0)
    estoque_atual_O_positivo = models.IntegerField(default=0)
    estoque_minimo_O_positivo = models.IntegerField(default=0)
    estoque_atual_O_negativo = models.IntegerField(default=0)
    estoque_minimo_O_negativo = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.hemocentro} - Estoque de Sangue"

    class Meta:
        verbose_name_plural = 'EstoqueSangue'  # Defina o nome plural para aparecer na interface de administração

        