from xml.parsers.expat import model
from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw

class Funcionario(models.Model):
    id = models.AutoField(primary_key=True)
    nome= models.CharField(max_length=100, verbose_name="Nome do cracha")
    matricula = models.IntegerField(verbose_name="matricula da empresa")
    setor = models.CharField(max_length=50, verbose_name="Setor")


class Equipamento(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=150, verbose_name="Nome do equipamento")
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.descricao}"


class Kit(models.Model):
    STATUS_KIT = [
        ("EM_USO", "Em uso"),
        ("INDISPONIVEL", "Indisponivel"),
        ("DISPONIVEL", "Disponivel"),
    ]
    
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=150, verbose_name="Nome do kit")
    image = models.ImageField(upload_to="img/%Y/%m/%d", null=False, blank=False)
    qr_code = models.ImageField(upload_to="qr_codes", blank=True)
    equipamentos = models.ForeignKey(Equipamento, on_delete=models.PROTECT, verbose_name="Equipamento")
    status = models.CharField(verbose_name="Status", max_length=12, choices=STATUS_KIT, default="DISPONIVEL")
    url = models.CharField(max_length=250, verbose_name="url")

    def __str__(self):
        return f"{self.descricao}"

    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make([self.descricao, self.equipamentos, self.image.url, self.url])
        canvas = Image.new('RGB', (470,470), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f'qrcode-{self.url}'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)


class Solicitacao(models.Model):
    STATUS_SOLICITACAO = [
        ("SOLICITADO", "Solicitado"),
        ("FINALIZADO", "Finalizado"),
    ]
    
    id = models.AutoField(primary_key=True)
    kit = models.ForeignKey(Kit, on_delete=models.PROTECT, verbose_name="Kit Solicitado")
    #kit  = models.CharField(max_length=150, verbose_name="Nome do kit")
    #equipamento = models.CharField(max_length=150, verbose_name="Equipamentos que compoe o kit")
    data = models.DateField(auto_now=False, blank=True, null=True)
    hora = models.TimeField(auto_now=False, blank=True, null=True)
    matricula = models.IntegerField(verbose_name="Matricula do solicitante")   
    status = models.CharField(verbose_name="Solicitação", max_length=12, choices=STATUS_SOLICITACAO, default="SOLICITADO")
    hora_termino = models.TimeField(auto_now=False, blank=True, null=True)
    observacao = models.TextField(verbose_name="Observação", blank=True, null=True)

    def __str__(self):
        return f"{self.kit}"
