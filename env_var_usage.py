from config import DB_USER, DB_PASSWORD

DSN = f'postgres://{DB_USER}:{DB_PASSWORD}@postgres_db:5432/db_name'


def connect_db():
    print(f'connecting db: {DSN=}')


if __name__ == '__main__':
    connect_db()
