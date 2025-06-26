from alembic import op
import sqlalchemy as sa

def upgrade():
    conn = op.get_bind()
    conn.execute(
        sa.text(
            "INSERT INTO dailytasks (day, task_no, task) VALUES (:day, :task_no, :task)"
        ),
        [{"day": 2, "task_no": 4, "task": "Python"},
         {"day": 3, "task_no": 5, "task": "Python python"}]
    )

def downgrade():
    conn = op.get_bind()
    conn.execute(
        sa.text("DELETE FROM dailytasks WHERE day = :day"),
        {"day": (1, 2)}
    )

accounts_table = table(
    "account",
    column("id", Integer),
    column("name", String),
    column("create_date", Date),
)

op.bulk_insert(
    accounts_table,
    [
        {
            "id": 1,
            "name": "John Smith",
            "create_date": date(2010, 10, 5),
        },
        {
            "id": 2,
            "name": "Ed Williams",
            "create_date": date(2007, 5, 27),
        },
        {
            "id": 3,
            "name": "Wendy Jones",
            "create_date": date(2008, 8, 15),
        },
    ],
)

with op.batch_alter_table('users') as batch_op:
    batch_op.add_column(sa.Column('age', sa.Integer))
    batch_op.drop_column('old_column')
    batch_op.alter_column('username', new_column_name='user_name')