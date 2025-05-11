from invoke import task


@task
def start(ctx):
    ctx.run("python3 src/main.py", pty=True)
    
@task
def test(ctx):
    ctx.run("poetry run python -m unittest discover -s src/tests")
    
@task
def coverage_report(ctx):
    ctx.run("poetry run coverage run -m unittest discover -s src/tests")
    ctx.run("poetry run coverage html")
    ctx.run("open htmlcov/index.html")

@task
def lint(ctx):
    ctx.run("pylint src", pty =True)