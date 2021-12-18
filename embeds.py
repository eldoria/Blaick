import discord


def embeds_profile(ctx):
    invisible_char = "\u200b"
    embed = discord.Embed()
    embed.set_thumbnail(url=ctx.author.avatar_url)

    embed.add_field(name="Informations", value="Classe: Human\nNiveau: 1", inline=True)
    embed.add_field(name=invisible_char, value="Stamina: 100\nExpérience: 0/100", inline=True)
    embed.add_field(name=invisible_char, value=invisible_char, inline=False)

    embed.add_field(name="Stats", value=f"hp: \nDéfense physique: \nAgilité: ", inline=True)
    embed.add_field(name=invisible_char, value="Force: \nDéfense magique: ", inline=True)

    return embed
