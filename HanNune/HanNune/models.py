from django.db import models
from django.conf import settings

class live(models.Model):
    live_id = models.CharField(max_length=20, null=True)
    live_name = models.CharField(max_length=100, null=True)
    live_start_dt = models.DateTimeField(null=True)
    live_end_dt = models.DateTimeField(null=True)
    live_stat = models.CharField(max_length=20, null=True)
    campaign_key = models.CharField(max_length=20, null=True)

class live_chat(models.Model):
    live_id = models.CharField(max_length=20, null=True)
    live_chat_dt = models.DateTimeField(null=True)
    user_uid = models.CharField(max_length=20, null=True)
    user_id = models.CharField(max_length=50, null=True)
    user_name = models.CharField(max_length=50, null=True)
    chat_cont = models.CharField(max_length=200, null=True)
    live_chat_id = models.CharField(max_length=20, primary_key=True)

    class Meta:
        managed = False
        db_table = 'live_chat'

class god(models.Model):
    god_no = models.CharField(max_length=20, null=True)
    erp_god_no = models.CharField(max_length=60, null=True)
    dsgn_grp_no = models.CharField(max_length=60, null=True)
    god_nm = models.CharField(max_length=500, null=True)
    prdlst_cd = models.CharField(max_length=60, null=True)
    prdlst_grp_cd = models.CharField(max_length=60, null=True)

class god_god_evl(models.Model):
    god_no = models.CharField(max_length=20, null=True)
    god_evl_turn = models.IntegerField(null=True)
    dsgn_grp_no = models.CharField(max_length=60, null=True)
    cstmr_nm = models.CharField(max_length=100, null=True)
    inflow_ord_sect_cd = models.CharField(max_length=60, null=True)
    god_evl_sj = models.CharField(max_length=200, null=True)
    god_evl_cont = models.CharField(max_length=4000, null=True)

class god_god_evl_atch_file(models.Model):
    god_no = models.CharField(max_length=20, null=True)
    god_evl_turn = models.IntegerField(null=True)
    atch_file_turn = models.IntegerField(null=True)
    atch_file_nm = models.CharField(max_length=300, null=True)
    atch_file_url = models.CharField(max_length=300, null=True)
    expect_img_badn_rt = models.IntegerField(null=True)
    img_rtat_num = models.IntegerField(null=True)

class god_god_evl_size(models.Model):
    god_no = models.CharField(max_length=20, null=True)
    god_evl_turn = models.IntegerField(null=True)
    mbr_size_cd = models.CharField(max_length=60, null=True)
    size_val = models.CharField(max_length=300, null=True)
    size_unit_cd = models.CharField(max_length=60, null=True)

class god_god_evl_wear_info(models.Model):
    god_no = models.CharField(max_length=20, null=True)
    god_evl_turn = models.IntegerField(null=True)
    wear_info_sect_cd = models.CharField(max_length=60, null=True)
    wear_info_sect_detail_cd = models.CharField(max_length=60, null=True)
    wear_info_sect_detail_val = models.IntegerField(null=True)