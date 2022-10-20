from django.db.models import TextChoices
from django.utils.translation import ugettext_lazy as _

string_punctuation = '!#$%&()*+,-.:;<=>?@[]^_~'
DEFAULT_PASSWORD_LENGTH = 30
DEFAULT_PASSWORD_RULES = {
    'length': DEFAULT_PASSWORD_LENGTH,
    'symbol_set': string_punctuation
}


class AutomationTypes(TextChoices):
    ping = 'ping', _('Ping')
    gather_facts = 'gather_facts', _('Gather facts')
    push_account = 'push_account', _('Create account')
    change_secret = 'change_secret', _('Change secret')
    verify_account = 'verify_account', _('Verify account')
    gather_account = 'gather_account', _('Gather account')


class SecretStrategy(TextChoices):
    custom = 'specific', _('Specific')
    random_one = 'random_one', _('All assets use the same random password')
    random_all = 'random_all', _('All assets use different random password')


class SSHKeyStrategy(TextChoices):
    add = 'add', _('Append SSH KEY')
    set = 'set', _('Empty and append SSH KEY')
    set_jms = 'set_jms', _('Replace (The key generated by JumpServer) ')
