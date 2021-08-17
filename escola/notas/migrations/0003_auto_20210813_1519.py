# Generated by Django 3.2.6 on 2021-08-13 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notas', '0002_segundobimestre_segunda_nota_geografia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='primeirobimestre',
            name='primeira_nota_Ciências',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='primeirobimestre',
            name='primeira_nota_Geografia',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='primeirobimestre',
            name='primeira_nota_História',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='primeirobimestre',
            name='primeira_nota_Matemática',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='primeirobimestre',
            name='primeira_nota_Português',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='quartobimestre',
            name='quarta_nota_Ciências',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='quartobimestre',
            name='quarta_nota_Geografia',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='quartobimestre',
            name='quarta_nota_História',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='quartobimestre',
            name='quarta_nota_Matemática',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='quartobimestre',
            name='quarta_nota_Português',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='segundobimestre',
            name='segunda_nota_Ciências',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='segundobimestre',
            name='segunda_nota_Geografia',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='segundobimestre',
            name='segunda_nota_História',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='segundobimestre',
            name='segunda_nota_Matemática',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='segundobimestre',
            name='segunda_nota_Português',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='terceirobimestre',
            name='terceira_nota_Ciências',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='terceirobimestre',
            name='terceira_nota_Geografia',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='terceirobimestre',
            name='terceira_nota_História',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='terceirobimestre',
            name='terceira_nota_Matemática',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='terceirobimestre',
            name='terceira_nota_Português',
            field=models.FloatField(),
        ),
    ]