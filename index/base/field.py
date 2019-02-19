from django.db.models import (
    Field as Base,

    # Date fields
    DateTimeField as DateTime,
    DateField as Date,
    TimeField as Time,
    DurationField as Duration,

    # Number fields
    AutoField as Auto,
    BigAutoField as BigAuto,
    IntegerField as Integer,
    PositiveIntegerField as PositiveInteger,
    SmallIntegerField as SmallInteger,
    PositiveSmallIntegerField as PositiveSmallInteger,
    BigIntegerField as BigInteger,
    FloatField as Float,
    DecimalField as Decimal,
    CommaSeparatedIntegerField as CommaSeparatedInteger,

    NullBooleanField as NullBoolean,
    BooleanField as Boolean,

    # Relations fields
    ManyToManyField as ManyToMany,
    OneToOneField as OneToOne,
    ForeignKey as Foreign,

    # Others
    EmailField as Email,
    GenericIPAddressField as GenericIPAdress,
    IPAddressField as IPAdress,
    BinaryField as Binary,
    ImageField as Image,
    SlugField as Slug,
    FileField as File,
    CharField as Char,
    TextField as Text,
    FilePathField as FilePath,
    URLField as URL,
    UUIDField as UUID,
)

from index.fields.timezone import TimeZoneField as TimeZone
