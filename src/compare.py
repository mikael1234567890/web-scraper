def find_new_books(old, new):
    old_ids = {b["id"] for b in old}
    return [b for b in new if b["id"] not in old_ids]