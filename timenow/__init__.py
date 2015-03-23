from vk_functions import vk_method
import time

def get(message):
    msk_time = vk_method('utils.getServerTime', {}) + 10800
    out_message = 'Московское время - {msk_time}, воткинское - {vtk_time}'.format(
        msk_time=time.strftime('%H:%M', time.gmtime(msk_time)),
        vtk_time=time.strftime('%H:%M')
    )
    return {"text": out_message, "attachments": []}
