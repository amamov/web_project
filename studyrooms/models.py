
from django.db import models

class StudyroomStatus(models.Model):
    studyroom_number = models.AutoField(primary_key = True)
    studyroom_classification = models.CharField(max_length = 64)
    studyroom_name = models.CharField(max_length = 64)
    studyroom_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.studyroom_name

    class Meta:
        abstract = True

class StudyBook(models.Model):
    studybook_number = models.AutoField(primary_key = True)
    writter = models.ForeignKey("users.User", on_delete=models.CASCADE)
    contents = models.CharField(max_length = 300)

    class Meta:
        verbose_name_plural = "Study_book"

class NoticeBoard(models.Model):
    board_number = models.AutoField(primary_key = True)
    writter = models.ForeignKey("users.User", on_delete=models.CASCADE)
    contents = models.CharField(max_length = 300)
    type = models.CharField(max_length = 10) 
    date = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name_plural = "notice_board"

class ProgressRate(models.Model):
    rate_number = models.AutoField(primary_key = True)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="progress_rates")
	study_room = models.ForeignKey("StudyRoom", on_delete=models.CASCADE, related_name="progress_rates")
    progress_rate = models.FloatField()

    class Meta:
        verbose_name_plural = "progress_rate"

class StudyTime(models.Model):
    studytime_number = models.AutoField(primary_key = True)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="progress_rates")
	study_room = models.ForeignKey("StudyRoom", on_delete=models.CASCADE, related_name="progress_rates")
    study_time = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name_plural = "study_time"



# Create your models here.
class StudyRoom(Studyroom_status):
    leader_Id = models.ForeignKey(
               "users.user",
               on_delete = models.CASCADE,
               related_name = "study_rooms", 
    )

    study_book = models.ManyToManyField("Study_book",blank=True, related_name="study_rooms")
    notice_board = models.ManyToManyField("Notice_board",blank=True, related_name = "study_rooms")


    def __str__(self):
        return self.studyroom_name
        
    class Meta: 
        db_table = 'Studyroom'
        verbose_name = 'Studyroom'
        verbose_name_plural = 'Studyroom'
