import psycopg2

class PostgresDBConnection:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.conn = None

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            print("Conexión a la base de datos PostgreSQL exitosa.")
        except psycopg2.Error as e:
            print(f"Error al conectar a la base de datos: {e}")

    def execute_query(self, query):
        if not self.conn:
            print("No se pudo ejecutar la consulta. La conexión no está establecida.")
            return

        try:
            with self.conn.cursor() as cur:
                cur.execute(query)
                result = cur.fetchall()
                return result
        except psycopg2.Error as e:
            print(f"Error al ejecutar la consulta: {e}")

    def close(self):
        if self.conn:
            self.conn.close()
            print("Conexión cerrada.")
