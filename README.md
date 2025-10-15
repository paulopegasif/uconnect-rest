# UCONNECT — REST
## Backend
1) `cd backend && python -m venv .venv && source .venv/bin/activate`
2) `pip install -r requirements.txt`
3) Crie `.env` a partir de `.env.example` (ajuste `DATABASE_URL` se necessário)
4) Exporte variáveis e crie as tabelas:
```bash
cd backend
export PYTHONPATH=$(pwd)
export DATABASE_URL=$(grep DATABASE_URL .env | cut -d'=' -f2-)
alembic -c alembic.ini upgrade head
uvicorn app.main:app --reload
```
- Healthcheck: `GET /api/v1/health/db`
- Auth: `POST /api/v1/auth/login` (necessário usuário seed no DB)
- Users: `GET/POST/PATCH/DELETE /api/v1/users` (Bearer)

## Dica (seed admin):
```sql
INSERT INTO users (matricula, name, email, password_hash, role, active)
VALUES ('admin','Admin','admin@uconnect.local',
'$2b$12$8x9b2u9b2u9b2u9b2u9b2uZyq8GQnYw6Vt7oYqsnT3qz6bA4iQny','admin',true);
-- senha: admin123
```
