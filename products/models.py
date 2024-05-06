from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['name']

    def __str__(self):
        return self.name

class Product(models.Model):

    price_type_choices = (
        ('unitario', 'Precio Unitario'),
        ('media-doc', 'Media Docena'),
        ('docena', 'Docena'),
        ('por-kilo', 'kilo')
    )
    name = models.CharField(max_length=255, verbose_name='Nombre')
    image = models.ImageField(upload_to='products',default='imagen_default.jpg', verbose_name='Imagen')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='get_products',
                                 verbose_name='Categoria', null=True)
    description = models.TextField(verbose_name='Description')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Valor')
    price_type = models.CharField(max_length=20, choices=price_type_choices,default='unitario', verbose_name='Tipo')

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['name']

    def __str__(self):
        return self.name