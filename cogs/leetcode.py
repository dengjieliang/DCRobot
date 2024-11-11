import discord
import random
from discord.ext import commands

# 定義名為 Main 的 Cog
class Leetcode(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # 前綴指令
    @commands.command()
    async def leetcode_random(self, ctx: commands.Context):
        eg_number = int
        eg_number = random.randint(1, 500)
        url = str
        url = "http://lcid.cc/"+str(eg_number)
        await ctx.send(url)

# Cog 載入 Bot 中
async def setup(bot: commands.Bot):
    await bot.add_cog(Leetcode(bot))  # 這裡也要改