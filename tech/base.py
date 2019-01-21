def fields_dictionary(name):
    return {
        'StringField': 'text',
        'PasswordField': 'password',
        'BooleanField': 'radio',
        'FileField': 'file',
        'DecimalField': 'number',
        'IntegerField': 'number',
        'FloatField': 'number',
        'DateField': 'date',
        'TimeField': 'time',
        'DateTimeField': 'datetime-local',
    }.get(name, 'text')


def get_form_fields(form):
    try:
        name = form.name
    except:
        name = type(form).__name__

    return {
        'form': name,
        'fields': [{
            'name': field.name,
            'label': field.label.text,
            'description': field.description,
            'type': fields_dictionary(field.type),
            'original_type': field.type,
            'default': field.default,
            'required': field.flags.required,
        } for field in form]
    }
