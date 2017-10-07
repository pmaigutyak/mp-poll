from django.db import models
from django.utils.translation import ugettext as _



class Poll(models.Model):
    question = models.TextField(_('Question'))
    is_multiple = models.BooleanField(_('Is multiple'), default=False)
    user = models.ForeignKey(_('User'))
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.question

    class Meta:
        ordering = ['-id']
        verbose_name = _('Poll')
        verbose_name_plural = _('Polls')


class PollChoice(models.Model):
    poll = models.ForeignKey(Poll)
    value = models.CharField(max_length=255)
    votes = models.IntegerField(default=0, editable=False)

    def __unicode__(self):
        return self.value

    class Meta:
        ordering = ['value']
        unique_together = ['poll', 'value']
        verbose_name = _('Poll choice')
        verbose_name_plural = _('Poll choices')



class Vote(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.ForeignKey(PollChoice)

    def __unicode__(self):
        return self.choice.value

    class Meta:
        verbose_name = _('Vote')
        verbose_name_plural = _('Votes')


