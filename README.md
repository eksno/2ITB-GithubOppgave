# 2ITB GithubOppgave
 Jonas, Steffen, Rasmus, Marius

## Setup
1. Clone Repository
2. Download Docker Desktop https://www.docker.com/get-started
3. Open Docker Desktop 
4. Run `docker-compose_up.bat`
5. Inside Docker Desktop expand `2itb-githuboppgave` and find `2itb-githuboppgave-app-1`, then click the `CLI` button
6. Enter the command `alembic revision --autogenerate -m "Initial Migration"`
7. Enter the command `alembic upgrade head`