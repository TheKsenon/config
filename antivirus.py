from .. import loader, utils
from telethon.tl.functions.account import DeleteAccountRequest

@loader.tds
class DeleteAccountModule(loader.Module):
    """🗑️ Модуль для удаления аккаунта."""

    strings = {"name": "DeleteAccountModule"}

    @loader.command()
    async def deleteacc(self, message):
        """🗑️ Удалить аккаунт с использованием -force."""
        args = utils.get_args(message)
        if "force" in args:
            await message.edit("🗑️ Удаление аккаунта с флагом -force...")
            try:
                await message.client(DeleteAccountRequest(reason="Удаление аккаунта по запросу пользователя."))
                await message.edit("✅ Аккаунт успешно удален.")
            except Exception as e:
                await message.edit(f"❌ Не удалось удалить аккаунт: {e}")
        else:
            await message.edit("⚠️ Для принудительного удаления используйте флаг -force.")
          
