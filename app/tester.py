import discord
from discord import app_commands
from settings import *
from utils import debug, flagger

class Test:
    """Test class for testing new commands"""
    def __init__(self, client) -> None:
        self.client = client
        
    async def get_attrs(self, obj):
        """Get all attributes from the client"""
        attrs = dir(obj)
        name = obj.__class__.__name__
        attrs = [attr for attr in attrs if not attr.startswith("_")]
        debug(f"{name} object attrs :{attrs}", function=f"Test.get_attrs.{name}")

    async def test(self, interaction):
        """Test command"""

        user = interaction.user
        roles = user.roles # cargos do user que chamou o comando
        flag = flagger(roles, PRESIDENT_ID, VICE_PRESIDENT_ID) # check if user is president

        if not flag:
            await interaction.response.send_message("Only the president or devs can use this command :(", ephemeral=True)
            return
        
        await self.get_attrs(self.client)
        await self.get_attrs(interaction)
        
        
        
        
        await interaction.response.send_message("Test command, logs avaible on command prompt", ephemeral=True)
        await interaction.edit_original_response(content="Test commands was edited")
        