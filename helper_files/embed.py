# from discord.ext import commands
import discord
import asyncio # noqa, flake8 F401
# import json # noqa, flake8 F401


async def embed(ctx, title='', content='', description='', author='', colour=0xfaa51b, link='', thumbnail='',
                avatar='', footer=''):
    """
    title:<str> Title of the embed 99% of the time it'll be the command name, exceptions when it makes sense like
        with the sfu command.\n
    content:<array[tuples]> Array of tuples. Tuple per field of the embed. Field name at index 0 and value at index
        1. \n
    description:<str> Appears under the title. \n
    author:<str> Used to indicate user who involked the command or the bot itself when it makes sense like with the
        echo command.\n
    colour:<0x......> Used to set the coloured strip on the left side of the embed, by default set to a nice blue
        colour.\n
    link: <deprecated>\n
    thumbnail:<str> Url to image to be used in the embed. Thumbnail appears top right corner of the embed.\n
    avatar:<str> Used to set avatar next to author's name. Must be url. \n
    footer:<str> Used for whatever."""
    # these are put in place cause of the limits on embed described here
    # https://discordapp.com/developers/docs/resources/channel#embed-limits
    if len(title) > 256:
        title = str(title)
        length = str(len(title) - 256)
        await ctx.send("Embed Error: Title too big")
        return False

    if len(description) > 2048:
        await ctx.send("Embed Error: Description too big")
        return False

    if len(content) > 25:
        await ctx.send("Embed Error: Content too big")
        return False

    for record in content:
        if len(record[0]) > 256:
            await ctx.send("Embed Error: Content record too big")
            return False
        if len(record[1]) > 1024:
            await ctx.send("Embed Error: Content record too big")
            return False

    if len(footer) > 2048:
        await ctx.send("Embed Error: footer too big")
        return False

    embObj = discord.Embed(title=title, type='rich')
    embObj.description = description
    embObj.set_author(name=author, icon_url=avatar)
    embObj.colour = colour
    embObj.set_thumbnail(url=thumbnail)
    embObj.set_footer(text=footer)
    # embObj.url = link
    # parse content to add fields
    for x in content:
        embObj.add_field(name=x[0], value=x[1], inline=False)
    return embObj
