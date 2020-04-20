import click

@click.command()
@click.option('--num', default=1, help='number of greetings')
@click.option('--string', default='me:)', help='this is what\'s printed')
@click.argument('out', type=click.File('w'),default='-', required=False)
def cli(num, string, out):
    """this functions just says hello repeatedly for sometime."""
    for i in range(num):
        click.echo(f'Hello {string} !!!')


# if __name__ == '__main__':
#     sayHello()