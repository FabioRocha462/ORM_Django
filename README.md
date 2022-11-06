# ORM_Django

Aprendendo a fazer filtros com o ORM do Django
# Filter e Order_by
`Product.objects.filter(name__contains="geladeira").order_by('unitary_value') `

# Join

`Request.objects.filter(delivery__address__state="RN")`

# Exclude

`Product.objects.filter(name__contains="geladeira").exclude(name="geladeira") `
