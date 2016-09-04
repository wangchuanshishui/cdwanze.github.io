#!/usr/bin/env python
# -*-coding:utf-8-*-




import click

@click.command()
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def main(name):
    click.echo('Hello %s!' % name)


if __name__ == '__main__':
    main()
