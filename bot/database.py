#    This file is part of the FileSharing distribution.
#    Copyright (c) 2022 kaif-00z
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in
# <https://github.com/kaif-00z/FileSharingBot/blob/main/License> .


from . import dB

# ----------------------BoardCast_db-----------------


def add_user(id):
    board = eval(dB.get("BOARDCAST_USERS") or "[]")
    if id not in board:
        board.append(id)
        dB.set("BOARDCAST_USERS", str(board).replace(" ", ""))


def rem_user(id):
    board = eval(dB.get("BOARDCAST_USERS") or "[]")
    if id in board:
        board.remove(id)
        dB.set("BOARDCAST_USERS", str(board).replace(" ", ""))


def get_users():
    return eval(dB.get("BOARDCAST_USERS") or "[]")


# ------------------------STORE_DB------------------


def info_own_iteam(unique_id, owner_id):
    _ = eval(dB.get("OWNERS_OF_ITEAMS") or "{}")
    _.update({unique_id: str(owner_id)})
    dB.set("OWNERS_OF_ITEAMS", str(_))


def get_info_own_iteam(unique_id):
    _ = eval(dB.get("OWNERS_OF_ITEAMS") or "{}")
    try:
        if _[unique_id]:
            return eval(_[unique_id])
    except BaseException:
        return None


def store_iteam(unique_id, id):
    _ = eval(dB.get("STORE") or "{}")
    _.update({unique_id: str(id)})
    dB.set("STORE", str(_))


def get_stored_iteam(unique_id):
    _ = eval(dB.get("STORE") or "{}")
    if _[unique_id]:
        try:
            return eval(_[unique_id])
        except BaseException:
            return None
    else:
        return None


def del_stored_iteam(unique_id):
    _ = eval(dB.get("STORE") or "{}")
    _x = eval(dB.get("OWNERS_OF_ITEAMS") or "{}")
    if unique_id in _:
        _.pop(unique_id)
        dB.set("STORE", str(_))
    if unique_id in _x:
        _x.pop(unique_id)
        dB.set("OWNERS_OF_ITEAMS", str(_x))
