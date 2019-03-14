class FormFields:
    from wtforms import (
        Field as __Field,
        TimeField as __Time,
        FieldList as __List,
        FileField as __File,
        TextField as __Text,
        DateField as __Date,
        RadioField as __Radio,
        FloatField as __Float,
        SelectField as __Select,
        HiddenField as __Hidden,
        StringField as __String,
        DecimalField as __Decimal,
        IntegerField as __Integer,
        BooleanField as __Boolean,
        TextAreaField as __TextArea,
        DateTimeField as __DateTime,
        PasswordField as __Password,
        MultipleFileField as __MultipleFile,
        SelectMultipleField as __SelectMultiple,
    )

    time = __Time
    list = __List
    text = __Text
    file = __File
    date = __Date
    float = __Float
    field = __Field
    radio = __Radio
    select = __Select
    hidden = __Hidden
    string = __String
    boolean = __Boolean
    decimal = __Decimal
    integer = __Integer
    password = __Password
    date_time = __DateTime
    text_area = __TextArea
    multiple_file = __MultipleFile
    select_multiple = __SelectMultiple
