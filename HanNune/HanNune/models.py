from unittest.util import _MAX_LENGTH
from django.db import models
from django.conf import settings

class live(models.Model):
    live_id = models.CharField(max_length=20, primary_key=True)
    live_name = models.CharField(max_length=100, null=True)
    live_start_dt = models.DateTimeField(null=True)
    live_end_dt = models.DateTimeField(null=True)
    live_stat = models.CharField(max_length=20, null=True)
    campaign_key = models.CharField(max_length=20, null=True)
    live_img_url = models.CharField(max_length=1000, null=True)

    class Meta:
        managed = False
        db_table = 'live'

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

class sentiword_info(models.Model):
    id = models.IntegerField(primary_key=True)
    word = models.CharField(max_length=100)
    word_root = models.CharField(max_length=100, null=True)
    polarity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sentiword_info'

class sentiword_live_score(models.Model):
    id = models.IntegerField(primary_key=True)
    power_negative = models.IntegerField()
    negative = models.IntegerField()
    neutrality = models.IntegerField()
    positive = models.IntegerField()
    power_positive = models.IntegerField()
    live_id = models.IntegerField()
    total = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sentiword_live_score'

class sentiword_goods_score(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    power_negative = models.IntegerField()
    negative = models.IntegerField()
    neutrality = models.IntegerField()
    positive = models.IntegerField()
    power_positive = models.IntegerField()
    god_no = models.CharField(max_length=20)
    total = models.IntegerField()
    evl5_cnt = models.IntegerField()
    evl4_cnt = models.IntegerField()
    evl3_cnt = models.IntegerField()
    evl2_cnt = models.IntegerField()
    evl1_cnt = models.IntegerField()
    god_nm = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'sentiword_goods_score'

class keyword_live_rank(models.Model):
    live_keyword_sn = models.AutoField(primary_key=True)
    live_id = models.CharField(max_length=20)
    keyword_rank = models.IntegerField(null=True)
    keyword = models.CharField(max_length=100, null=True)
    keyword_freq = models.IntegerField(null=True)

    class Meta:
        managed = False
        db_table = 'keyword_live_rank'

class god(models.Model):
    god_no = models.CharField(primary_key=True, max_length=20)
    erp_god_no = models.CharField(max_length=60, null=True)
    dsgn_grp_no = models.CharField(max_length=60, null=True)
    god_nm = models.CharField(max_length=500, null=True)
    prdlst_cd = models.CharField(max_length=60, null=True)
    prdlst_grp_cd = models.CharField(max_length=60, null=True)

    class Meta:
        managed = False
        db_table = 'god'

class god_god_evl(models.Model):
    # id = models.AutoField(primary_key=True)
    god_no = models.CharField(primary_key=True, max_length=20)
    god_evl_turn = models.IntegerField(unique=True)
    dsgn_grp_no = models.CharField(max_length=60, null=True)
    cstmr_nm = models.CharField(max_length=100, null=True)
    inflow_ord_sect_cd = models.CharField(max_length=60, null=True)
    god_evl_sj = models.CharField(max_length=200, null=True)
    god_evl_cont = models.CharField(max_length=4000, null=True)
    tot_evl_score = models.CharField(max_length=10, null=True)
    # god_god_evl_sn = models.IntegerField(null=True)
    BST_GOD_EVL_YN = models.CharField(max_length=10, null=True)
    DVC_CD = models.CharField(max_length=10, null=True)
    class Meta:
        managed = False
        db_table = 'god_god_evl'

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

class goods_emotion(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    power_negative = models.IntegerField()
    negative = models.IntegerField()
    neutrality = models.IntegerField()
    positive = models.IntegerField()
    power_positive = models.IntegerField()
    god_no = models.CharField(max_length=20)
    total = models.IntegerField()
    evl5_cnt = models.IntegerField()
    evl4_cnt = models.IntegerField()
    evl3_cnt = models.IntegerField()
    evl2_cnt = models.IntegerField()
    evl1_cnt = models.IntegerField()
    best_evl5_cnt = models.IntegerField()
    best_evl4_cnt = models.IntegerField()
    best_evl3_cnt = models.IntegerField()
    best_evl2_cnt = models.IntegerField()
    best_evl1_cnt = models.IntegerField()
    god_nm = models.CharField(max_length=500)
    god_img = models.CharField(max_length=45)

class keyword_goods_rank(models.Model):
    goods_keyword_sn = models.AutoField(primary_key=True)
    god_no = models.CharField(max_length=20)
    keyword_rank = models.IntegerField(null=True)
    keyword = models.CharField(max_length=100, null=True)
    keyword_freq = models.IntegerField(null=True)

    class Meta:
        managed = False
        db_table = 'keyword_goods_rank'

class god_img(models.Model):
    god_no = models.CharField(max_length=20)
    img_tp_cd = models.CharField(max_length=20)
    img_size_cd = models.CharField(max_length=20)
    img_turn = models.CharField(max_length=10)
    img_url = models.CharField(max_length=45)
    rprst_img_yn = models.CharField(max_length=1)
    model_img_yn = models.CharField(max_length=1)
    img_dscr = models.CharField(max_length=45)
    img_aprv_yn = models.CharField(max_length=1)
    img_use_yn = models.CharField(max_length=1)
    img_last_udt_dt = models.DateTimeField(null=True)
    regtr_id = models.CharField(max_length=45)
    reg_dt = models.DateTimeField(null=True)
    udter_id = models.CharField(max_length=45)
    udt_dt = models.DateTimeField(null=True)
    god_img_sn = models.CharField(primary_key=True, max_length=200)

    class Meta:
        managed = False
        db_table = 'god_img'