from enum import unique
from django.db import models

@unique
class QuarantineWardStatus(models.TextChoices):
    LOCKED = 'LOCKED',
    RUNNING = 'RUNNING'
    UNKNOWN = 'UNKNOWN'

class CustomUserStatus(models.TextChoices):
    LOCKED = 'LOCKED',
    AVAILABLE = 'AVAILABLE'

class QuarantineWardType(models.TextChoices):
    CONCENTRATE = 'CONCENTRATE'
    PRIVATE = 'PRIVATE'

class Gender(models.TextChoices):
    MALE = 'MALE'
    FEMALE = 'FEMALE'

class RoleName(models.TextChoices):
    ADMINISTRATOR = 'ADMINISTRATOR'
    SUPER_MANAGER = 'SUPER_MANAGER'
    MANAGER = 'MANAGER'
    STAFF = 'STAFF'
    MEMBER = 'MEMBER'

class MemberLabel(models.TextChoices):
    F0 = 'F0'
    F1 = 'F1'
    F2 = 'F2'
    F3 = 'F3'

class MemberQuarantinedStatus(models.TextChoices):
    COMPLETED = 'COMPLETED'
    QUARANTINING = 'QUARANTINING'
    REQUARANTINING = 'REQUARANTINING'
    MOVED = 'MOVED'

class HealthStatus(models.TextChoices):
    NORMAL = 'NORMAL'
    UNWELL = 'UNWELL'
    SERIOUS = 'SERIOUS'

class Disease(models.TextChoices):
    # now not use
    NONE = 'NONE'
    TIEU_DUONG = 'TIEU_DUONG'
    UNG_THU = 'UNG_THU'
    HEN_SUYEN = 'HEN_SUYEN'
    CAO_HUYET_AP = 'CAO_HUYET_AP'
    BENH_GAN = 'BENH_GAN'
    BENH_THAN_MAN_TINH = 'BENH_THAN_MAN_TINH'
    BENH_TIM_MACH = 'BENH_TIM_MACH'
    BENH_LY_MACH_MAU_NAO = 'BENH_LY_MACH_MAU_NAO'
    OTHER = 'OTHER'

class SymptomType(models.TextChoices):
    MAIN = 'MAIN'
    EXTRA = 'EXTRA'

class TestStatus(models.TextChoices):
    WAITING = 'WAITING'
    DONE = 'DONE'

class TestResult(models.TextChoices):
    NEGATIVE = 'NEGATIVE'
    POSITIVE = 'POSITIVE'

class TestType(models.TextChoices):
    QUICK = 'QUICK'
    RT_PCR = 'RT-PCR'