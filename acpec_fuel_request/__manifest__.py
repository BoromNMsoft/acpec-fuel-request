{
    'name': 'ACPEC Fuel Request',
    'version': '17.0.1.0.0',
    'category': 'Operations',
    'summary': 'Gestion des demandes de carburant',
    'description': """
Module de gestion des demandes de carburant
=============================================
Permet la création, validation, suivi et notification des demandes
de carburant pour une société de distribution d'hydrocarbures.
""",
    'author': 'Amadou BA',
    'website': '',
    'license': 'LGPL-3',
    'depends': ['base', 'mail'],
    'data': [
        # 1. Sécurité d'abord : les groupes doivent exister avant les droits d'accès
        'security/security.xml',
        'security/ir.model.access.csv',
        # 2. Données de base : la séquence doit exister avant la création d'enregistrements
        'data/sequence.xml',
        # 3. Vues : elles peuvent référencer des groupes définis en sécurité
        'views/fuel_request_views.xml',
        # 4. Rapport : vient en dernier
        'report/fuel_report.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
