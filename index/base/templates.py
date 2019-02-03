from index.settings import TEMPLATE_PREFIXES as __tp
from django.template.loader import get_template as __gt
from django.template import Template as __t


def get_template(name: str, type=None, extension='.html', using=None) -> __t:
    if type:
        return __gt(
            "%(type)s/%(name)s%(extension)s" % {
                'type': __tp.get(type, 'mail'),
                'name': name,
                'extension': extension,
            },
            using
        )
    else:
        return __gt("%s%s" % (name, extension), using)
