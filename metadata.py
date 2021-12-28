from sqlalchemy import MetaData, Table, Column, String, Integer, Boolean, ForeignKey


metadata = MetaData()


table_session = Table(
    'session', metadata,
    Column('id_session', Integer, primary_key=True, autoincrement=False),
    Column('id_discord', String, primary_key=True, autoincrement=False)
)

table_experience = Table(
    'experience', metadata,
    Column('id_session', Integer, primary_key=True, autoincrement=False),
    Column('id_discord', String, primary_key=True, autoincrement=False),
    Column('level', Integer),
    Column('experience', Integer),
    Column('experience_required', Integer)
)

table_items = Table(  # pas besoin d'id_session pcq les items lootables sont les mêmes quel que soit la session de jeu
    'items', metadata,
    Column('id_item', Integer, primary_key=True, autoincrement=True),
    Column('name', String),
    Column('type', String),
    Column('physical_defense', Integer),
    Column('magic_defense', Integer),
    Column('weight', Integer),
    Column('power', Integer)
)

table_inventory = Table(
    'inventory', metadata,
    Column('id_session', Integer, primary_key=True, autoincrement=False),
    Column('id_discord', String, primary_key=True, autoincrement=False),
    Column('id_item', Integer, ForeignKey('items.id_item')),
    Column('quantity', Integer)
)

table_equipment = Table(
    'equipment', metadata,
    Column('id_session', Integer, primary_key=True, autoincrement=False),
    Column('id_discord', String, primary_key=True, autoincrement=False),
    Column('id_item', Integer, ForeignKey('items.id_item'))
)

table_market = Table(
    'market', metadata,
    Column('id_session', Integer, primary_key=True, autoincrement=False),
    Column('id_discord', String, primary_key=True, autoincrement=False),
    Column('id_item', Integer, ForeignKey('items.id_item')),
    Column('type', String),  # selon si c'est une offre ou une demande
    Column('gold', Integer)
)

table_race = Table(
    'race', metadata,
    Column('id_session', Integer, primary_key=True, autoincrement=False),
    Column('id_discord', String, primary_key=True, autoincrement=False),
    Column('stamina', Integer),
    Column('gold', Integer),
    Column('weight', Integer),
    Column('health', Integer),
    Column('force', Integer),
    Column('defense', Integer),
    Column('magic_resist', Integer),
    Column('race', String),
    Column('intelligence', Integer),  # spécifique aux elfes
    Column('mana', Integer)  # spécifique aux elfes
)

