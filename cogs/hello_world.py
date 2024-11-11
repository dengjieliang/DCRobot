import discord
import random
from discord.ext import commands

# 定義名為 Main 的 Cog
class Hello_world(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # 前綴指令
    @commands.command()
    async def hello(self, ctx: commands.Context):
        await ctx.send("Hello, world!")

# Cog 載入 Bot 中
async def setup(bot: commands.Bot):
    await bot.add_cog(Hello_world(bot))