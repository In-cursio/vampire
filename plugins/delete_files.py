#https://github.com/Joelkb/DQ-the-file-donor

import re
import logging
from pyrogram import Client, filters
from info import DELETE_CHANNELS
from database.ia_filterdb import Media1, Media2, Media3, Media4, Media5, Media6, unpack_new_file_id

logger = logging.getLogger(__name__)

media_filter = filters.document | filters.video | filters.audio



@Client.on_message(filters.chat(DELETE_CHANNELS) & media_filter)
async def deletemultiplemedia(bot, message):
    """Delete Multiple files from the database"""
    for file_type in ("document", "video", "audio"):
        media = getattr(message, file_type, None)
        if media is not None:
            break
    else:
        return

    file_id, file_ref = unpack_new_file_id(media.file_id)

    result_media1 = await Media1.collection.find_one({'_id': file_id})
    result_media2 = await Media2.collection.find_one({'_id': file_id})
    result_media3 = await Media3.collection.find_one({'_id': file_id})
    result_media4 = await Media4.collection.find_one({'_id': file_id})
    result_media5 = await Media5.collection.find_one({'_id': file_id})
    result_media6 = await Media6.collection.find_one({'_id': file_id})
    
    if result_media1:
        await Media1.collection.delete_one({'_id': file_id})
    elif result_media2:
        await Media2.collection.delete_one({'_id': file_id})
    elif result_media3:
        await Media3.collection.delete_one({'_id': file_id})
    elif result_media4:
        await Media4.collection.delete_one({'_id': file_id})
    elif result_media5:
        await Media5.collection.delete_one({'_id': file_id})
    elif result_media6:
        await Media6.collection.delete_one({'_id': file_id})
    else:
        logger.info('File not found in the database.')
