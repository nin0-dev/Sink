import hikari
import lightbulb
import util

plugin = lightbulb.Plugin("Owner")


@plugin.command
@lightbulb.add_checks(lightbulb.owner_only)
@lightbulb.option(name="guild_id", description="ID of the guild to leave", type=str)
@lightbulb.command("leave", "Leaves a guild.")
@lightbulb.implements(lightbulb.PrefixCommand)
async def leave(ctx: lightbulb.Context):
    # Fetch guild
    rest = ctx.bot.rest
    try:
        guild = await rest.fetch_guild(ctx.options.guild_id)
    except hikari.NotFoundError:
        await ctx.respond(util.error("The specified guild doesn't exist."))
        return
    except hikari.ForbiddenError:
        await ctx.respond(util.error("Sink isn't part of the specified guild."))
        return
    except hikari.InternalServerError:
        await ctx.respond(util.error("Discord decided to throw a server error. Try again later."))
        return
    # Leave guild
    await rest.leave_guild(guild.id)
    await ctx.respond(util.success(f"Successfully left {guild.name}."))


def load(bot):
    bot.add_plugin(plugin)


def unload(bot):
    bot.remove_plugin(plugin)
