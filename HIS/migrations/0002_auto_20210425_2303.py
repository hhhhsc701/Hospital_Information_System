# Generated by Django 3.2 on 2021-04-25 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HIS', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bed',
            fields=[
                ('id', models.CharField(max_length=11, primary_key=True, serialize=False, verbose_name='床位')),
                ('status', models.SmallIntegerField(choices=[(0, '空'), (1, '满')], default=0, verbose_name='床位状态')),
            ],
            options={
                'verbose_name': '床位',
                'db_table': 'bed',
            },
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.CharField(max_length=11, primary_key=True, serialize=False, verbose_name='物品编号')),
                ('number', models.IntegerField(verbose_name='存货数目')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='成本')),
            ],
            options={
                'verbose_name': '库存',
                'db_table': 'inventory',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.CharField(max_length=11, primary_key=True, serialize=False, verbose_name='项目编号')),
                ('name', models.CharField(max_length=20, verbose_name='项目名称')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='项目单价')),
            ],
            options={
                'verbose_name': '收费项目',
                'db_table': 'project',
            },
        ),
        migrations.RenameField(
            model_name='doctor',
            old_name='id_num',
            new_name='id_number',
        ),
        migrations.RenameField(
            model_name='nurse',
            old_name='id_num',
            new_name='id_number',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='id_num',
            new_name='id_number',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='d_id',
            new_name='doctor_id',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='p_id',
            new_name='patient_id',
        ),
        migrations.AlterField(
            model_name='doctor',
            name='gender',
            field=models.SmallIntegerField(choices=[(0, '男'), (1, '女')], default=0, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='nurse',
            name='gender',
            field=models.SmallIntegerField(choices=[(0, '男'), (1, '女')], default=0, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.SmallIntegerField(choices=[(0, '男'), (1, '女')], default=0, verbose_name='性别'),
        ),
        migrations.CreateModel(
            name='Rounds',
            fields=[
                ('id', models.CharField(max_length=11, primary_key=True, serialize=False, verbose_name='查房信息')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='查房时间')),
                ('information', models.CharField(max_length=256, verbose_name='查房信息')),
                ('nurse_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='HIS.nurse', verbose_name='护士编号')),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='HIS.patient', verbose_name='病人编号')),
            ],
            options={
                'verbose_name': '查房表',
                'db_table': 'rounds',
            },
        ),
        migrations.CreateModel(
            name='Replenishment',
            fields=[
                ('id', models.CharField(max_length=11, primary_key=True, serialize=False, verbose_name='补货单编号')),
                ('number', models.IntegerField(verbose_name='补货数目')),
                ('time', models.DateTimeField(auto_now=True, verbose_name='补货日期')),
                ('inventory_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='HIS.inventory', verbose_name='物品编号')),
            ],
            options={
                'verbose_name': '补货单',
                'db_table': 'replenishment',
            },
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.CharField(max_length=11, primary_key=True, serialize=False, verbose_name='处方单编号')),
                ('content', models.TextField(verbose_name='处方内容')),
                ('annotation', models.CharField(max_length=256, verbose_name='批注')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='处方时间')),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='HIS.doctor', verbose_name='医生编号')),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='HIS.patient', verbose_name='病人编号')),
            ],
            options={
                'verbose_name': '处方单',
                'db_table': 'prescription',
            },
        ),
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.CharField(max_length=11, primary_key=True, serialize=False, verbose_name='手术单编号')),
                ('name', models.CharField(max_length=20, verbose_name='手术名称')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='手术时间')),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='HIS.patient', verbose_name='病人编号')),
                ('prescription_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='HIS.prescription', verbose_name='处方单编号')),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='HIS.project', verbose_name='项目编号')),
            ],
            options={
                'verbose_name': '手术',
                'db_table': 'Operation',
            },
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.CharField(max_length=11, primary_key=True, serialize=False, verbose_name='收费单编号')),
                ('name', models.CharField(max_length=20, verbose_name='药物名称')),
                ('number', models.IntegerField(verbose_name='药物数目')),
                ('text', models.TextField(verbose_name='注意事项')),
                ('prescription_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='HIS.prescription', verbose_name='处方单编号')),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='HIS.project', verbose_name='项目编号')),
            ],
            options={
                'verbose_name': '取药单',
                'db_table': 'Medicine',
            },
        ),
        migrations.CreateModel(
            name='Inspection',
            fields=[
                ('id', models.CharField(max_length=11, primary_key=True, serialize=False, verbose_name='检验单编号')),
                ('name', models.CharField(max_length=20, verbose_name='检验名称')),
                ('report', models.TextField(verbose_name='检验报告')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='检验时间')),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='HIS.doctor', verbose_name='医生编号')),
                ('prescription_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='HIS.prescription', verbose_name='处方单编号')),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='HIS.project', verbose_name='项目编号')),
            ],
            options={
                'verbose_name': '检验单',
                'db_table': 'inspection',
            },
        ),
        migrations.CreateModel(
            name='Hospitalized',
            fields=[
                ('id', models.CharField(max_length=11, primary_key=True, serialize=False, verbose_name='住院表编号')),
                ('admission_time', models.DateTimeField(auto_now_add=True, verbose_name='入院时间')),
                ('discharge_time', models.DateTimeField(verbose_name='出院时间')),
                ('will', models.SmallIntegerField(choices=[(0, '允许出院'), (1, '自主出院')], default=0, verbose_name='自主出院')),
                ('order', models.CharField(max_length=256, verbose_name='医嘱')),
                ('bed_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='HIS.bed', verbose_name='床位号')),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='HIS.doctor', verbose_name='医生编号')),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='HIS.patient', verbose_name='病人编号')),
            ],
            options={
                'verbose_name': '住院表',
                'db_table': 'hospitalized',
            },
        ),
        migrations.CreateModel(
            name='Charge',
            fields=[
                ('id', models.CharField(max_length=11, primary_key=True, serialize=False, verbose_name='收费单编号')),
                ('number', models.IntegerField(verbose_name='项目次数')),
                ('time', models.DateTimeField(auto_now=True, verbose_name='收费日期')),
                ('status', models.SmallIntegerField(choices=[(0, '未支付'), (1, '已支付')], default=0, verbose_name='缴费状态')),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='HIS.patient', verbose_name='病人编号')),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='HIS.project', verbose_name='项目编号')),
            ],
            options={
                'verbose_name': '收费单',
                'db_table': 'charge',
            },
        ),
        migrations.AddField(
            model_name='register',
            name='project',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='HIS.project', verbose_name='项目编号'),
        ),
        migrations.CreateModel(
            name='DoctorOperation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='HIS.doctor', verbose_name='医生编号')),
                ('operation_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='HIS.operation', verbose_name='手术单编号')),
            ],
            options={
                'unique_together': {('doctor_id', 'operation_id')},
            },
        ),
    ]