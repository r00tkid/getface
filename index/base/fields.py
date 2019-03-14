class Fields:
    from django.db.models import (
        Field as __Field,

        # Date fields
        DateTimeField as __DateTime,
        DateField as __Date,
        TimeField as __Time,
        DurationField as __Duration,

        # Number fields
        AutoField as __Auto,
        BigAutoField as __BigAuto,
        IntegerField as __Integer,
        PositiveIntegerField as __PositiveInteger,
        SmallIntegerField as __SmallInteger,
        PositiveSmallIntegerField as __PositiveSmallInteger,
        BigIntegerField as __BigInteger,
        FloatField as __Float,
        DecimalField as __Decimal,
        CommaSeparatedIntegerField as __CommaSeparatedInteger,

        NullBooleanField as __NullBoolean,
        BooleanField as __Boolean,

        # Relations fields
        ManyToManyField as __ManyToMany,
        OneToOneField as __OneToOne,
        ForeignKey as __Foreign,

        # Others
        EmailField as __Email,
        GenericIPAddressField as __GenericIPAddress,
        IPAddressField as __IPAddress,
        BinaryField as __Binary,
        ImageField as __Image,
        SlugField as __Slug,
        FileField as __File,
        CharField as __Char,
        TextField as __Text,
        FilePathField as __FilePath,
        URLField as __URL,
        UUIDField as __UUID,
    )

    # Custom fields goes here
    from index.fields.timezone import TimeZoneField as __TimeZone

    base = __Field
    date_time = __DateTime
    date = __Date
    time = __Time
    duration = __Duration

    auto = __Auto
    big_auto = __BigAuto
    integer = __Integer
    positive_integer = __PositiveInteger
    small_integer = __SmallInteger
    positive_small_integer = __PositiveSmallInteger
    big_integer = __BigInteger
    float = __Float
    decimal = __Decimal
    comma_separated_integer = __CommaSeparatedInteger

    null_boolean = __NullBoolean
    boolean = __Boolean

    many_to_many = __ManyToMany
    one_to_one = __OneToOne
    foreign = __Foreign

    email = __Email
    generic_ip_address = __GenericIPAddress
    ip_address = __IPAddress
    binary = __Binary
    image = __Image
    slug = __Slug
    file = __File
    char = __Char
    text = __Text
    file_path = __FilePath
    url = __URL
    uuid = __UUID

    time_zone = __TimeZone
