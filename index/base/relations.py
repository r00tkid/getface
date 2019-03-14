class Relations:
    from django.db.models import (
        CASCADE as __CASCADE,
        DO_NOTHING as __DO_NOTHING,
        PROTECT as __PROTECT,
        SET as __SET,
        SET_DEFAULT as __SET_DEFAULT,
        SET_NULL as __SET_NULL,
    )

    set = __SET
    protect = __PROTECT
    cascade = __CASCADE
    set_null = __SET_NULL
    do_nothing = __DO_NOTHING
    set_default = __SET_DEFAULT
