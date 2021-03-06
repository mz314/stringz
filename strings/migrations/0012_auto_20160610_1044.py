# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-10 10:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strings', '0011_auto_20160610_1028'),
    ]

    operations = [
        migrations.AddField(
            model_name='stringset',
            name='reference_pith',
            field=models.DecimalField(decimal_places=2, default=440, max_digits=20),
        ),
        migrations.AlterField(
            model_name='stringstringset',
            name='note',
            field=models.CharField(choices=[('A0', 'A0'), ('A#0', 'A#0'), ('B0', 'B0'), ('C0', 'C0'), ('C#0', 'C#0'), ('D0', 'D0'), ('D#0', 'D#0'), ('E0', 'E0'), ('F0', 'F0'), ('F#0', 'F#0'), ('G0', 'G0'), ('G#0', 'G#0'), ('A1', 'A1'), ('A#1', 'A#1'), ('B1', 'B1'), ('C1', 'C1'), ('C#1', 'C#1'), ('D1', 'D1'), ('D#1', 'D#1'), ('E1', 'E1'), ('F1', 'F1'), ('F#1', 'F#1'), ('G1', 'G1'), ('G#1', 'G#1'), ('A2', 'A2'), ('A#2', 'A#2'), ('B2', 'B2'), ('C2', 'C2'), ('C#2', 'C#2'), ('D2', 'D2'), ('D#2', 'D#2'), ('E2', 'E2'), ('F2', 'F2'), ('F#2', 'F#2'), ('G2', 'G2'), ('G#2', 'G#2'), ('A3', 'A3'), ('A#3', 'A#3'), ('B3', 'B3'), ('C3', 'C3'), ('C#3', 'C#3'), ('D3', 'D3'), ('D#3', 'D#3'), ('E3', 'E3'), ('F3', 'F3'), ('F#3', 'F#3'), ('G3', 'G3'), ('G#3', 'G#3'), ('A4', 'A4'), ('A#4', 'A#4'), ('B4', 'B4'), ('C4', 'C4'), ('C#4', 'C#4'), ('D4', 'D4'), ('D#4', 'D#4'), ('E4', 'E4'), ('F4', 'F4'), ('F#4', 'F#4'), ('G4', 'G4'), ('G#4', 'G#4'), ('A5', 'A5'), ('A#5', 'A#5'), ('B5', 'B5'), ('C5', 'C5'), ('C#5', 'C#5'), ('D5', 'D5'), ('D#5', 'D#5'), ('E5', 'E5'), ('F5', 'F5'), ('F#5', 'F#5'), ('G5', 'G5'), ('G#5', 'G#5'), ('A6', 'A6'), ('A#6', 'A#6'), ('B6', 'B6'), ('C6', 'C6'), ('C#6', 'C#6'), ('D6', 'D6'), ('D#6', 'D#6'), ('E6', 'E6'), ('F6', 'F6'), ('F#6', 'F#6'), ('G6', 'G6'), ('G#6', 'G#6'), ('A7', 'A7'), ('A#7', 'A#7'), ('B7', 'B7'), ('C7', 'C7'), ('C#7', 'C#7'), ('D7', 'D7'), ('D#7', 'D#7'), ('E7', 'E7'), ('F7', 'F7'), ('F#7', 'F#7'), ('G7', 'G7'), ('G#7', 'G#7')], max_length=3),
        ),
    ]
