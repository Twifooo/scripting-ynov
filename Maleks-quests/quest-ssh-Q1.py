import spur
import spur.ssh
import click

@click.command()
@click.option('--host', prompt='SSH Host', help='The SSH server hostname or IP address.')
@click.option('--port', default=22, type=int, help='The SSH server port.')
@click.option('--username', prompt='Username', help='The SSH username.')
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=False, help='The SSH password.')
def connect_ssh(host, port, username, password):
    """Connects to an SSH server and runs a simple command."""
    try:
        shell = spur.SshShell(
            hostname=host,
            port=port,
            username=username,
            password=password,
            missing_host_key=spur.ssh.MissingHostKey.accept
        )

        with shell:
            result = shell.run(["echo", "Hello, SSH!"])
            click.echo("Command output: {}".format(result.output.decode().strip()))
    except Exception as e:
        click.echo("An error occurred: {}".format(e))

if __name__ == '__main__':
    connect_ssh()