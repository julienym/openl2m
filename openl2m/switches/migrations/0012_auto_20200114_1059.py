# Generated by Django 2.2.9 on 2020-01-14 18:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('switches', '0011_auto_20200110_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='action',
            field=models.PositiveSmallIntegerField(
                choices=[
                    [0, 'View Switch Groups'],
                    [1, 'View Switch'],
                    [2, 'View Interface'],
                    [3, 'View PoE'],
                    [4, 'View Vlans'],
                    [5, 'View LLDP'],
                    [6, 'Viewing All Logs'],
                    [7, 'Viewing Site Statistics'],
                    [8, 'Viewing Tasks'],
                    [9, 'Viewing Task Details'],
                    [100, 'Reloading Switch Data'],
                    [101, 'New System ObjectID Found'],
                    [102, 'New System Name Found'],
                    [90, 'Login'],
                    [91, 'Logout'],
                    [92, 'Inactivity Logout'],
                    [93, 'Login Failed'],
                    [103, 'Interface Disable'],
                    [104, 'Interface Enable'],
                    [105, 'Interface Toggle'],
                    [106, 'Interface PoE Disable'],
                    [107, 'Interface PoE Enable'],
                    [108, 'Interface PoE Toggle'],
                    [109, 'Interface PVID Vlan Change'],
                    [110, 'Interface Description Change'],
                    [111, 'Saving Configuration'],
                    [112, 'Execute Command'],
                    [113, 'Port PoE Fault'],
                    [114, 'LDAP New SwitchGroup'],
                    [115, 'Bulk Edit'],
                    [116, 'Bulk Edit Task Submit'],
                    [117, 'Bulk Edit Task Started'],
                    [118, 'Bulk Edit Task Ended OK'],
                    [119, 'Bulk Edit Task Ended With Errors'],
                    [120, 'Task Deleted'],
                    [121, 'Task Terminated'],
                    [122, 'Email Sent'],
                    [256, 'Undefined Vlan'],
                    [257, 'Vlan Name Mismatch'],
                    [258, 'SNMP Error'],
                    [259, 'LDAP User->SwitchGroup Error'],
                    [260, 'LDAP SwitchGroup Error'],
                    [261, 'Bulk Edit Job Start Error'],
                    [262, 'Email Error'],
                ],
                default=1,
                verbose_name='Activity or Action to log',
            ),
        ),
        migrations.AlterField(
            model_name='task',
            name='results',
            field=models.TextField(blank=True, help_text='Task results, in JSON format', null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='reverse_arguments',
            field=models.TextField(
                blank=True, help_text='Arguments to undo the changes of this task, in JSON format', null=True
            ),
        ),
    ]
