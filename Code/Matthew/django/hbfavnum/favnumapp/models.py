from django.db import models
from django.contrib.auth.models import User


class FavNumReason(models.Model):
    text = models.CharField(max_length=150)

    def __str__(self):
        return self.text


class FavNum(models.Model):
    number = models.CharField(max_length=20)
    reason = models.ForeignKey(FavNumReason, related_name='fav_nums', on_delete=models.PROTECT)
    other_reason = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fav_nums')

    def __str__(self):
        return self.number + ' because ' + self.reason.text


# fav_num = FavNum.objects.get(id=1)
# fav_num.reasons.all()
# print(fav_num) # invoke the __str__

# reason = FavNumReason.objects.get(text='it\'s pretty')
# reason.fav_nums.all()
