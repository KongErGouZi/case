from django.db import models
from utils.common_model import BaseModel
from typing import Tuple


class CourseCategory(BaseModel):
    """ 课程分类表 """
    # verbose_name 后台admin显示字段
    name = models.CharField(max_length=64, unique=True, verbose_name='课程分类')

    class Meta:
        # 数据库表名
        db_table: str = 'luffy_course_category'
        # admin后台单数显示
        verbose_name: str = '分类'
        # admin后台复数显示
        verbose_name_plural: str = verbose_name

    def __str__(self) -> str:
        return '%s' % self.name


class Course(BaseModel):
    """ 课程表 """
    course_type: Tuple[int, str] = (
        (0, '付费'),
        (1, 'VIP专享')
    )
    level_choices: Tuple[int, str] = (
        (0, '初级'),
        (1, '中级'),
        (2, '高级'),
    )
    status_choices: Tuple[int, str] = (
        (0, '上线'),
        (1, '下线'),
        (2, '预上线'),
    )

    name = models.CharField(max_length=128, verbose_name='课程名')
    # upload_to='courses' 上传的图片保存到 courses 目录下
    # blank=True Django 表单层面该字段可以不填
    course_img = models.ImageField(upload_to='courses',
                                   blank=True,
                                   null=True,
                                   max_length=255,
                                   verbose_name='封面图片')
    course_type = models.SmallIntegerField(choices=course_type,
                                           default=0,
                                           verbose_name='付费类型')
    brief = models.TextField(max_length=2048,
                             blank=True,
                             null=True,
                             verbose_name='课程介绍')
    level = models.SmallIntegerField(choices=level_choices,
                                     default=0,
                                     verbose_name='难度等级')
    # DateField 只存年月日
    # auto_now_add 新增对象时，自动以当前时间赋值
    pub_date = models.DateField(verbose_name='发布日期',
                                auto_now_add=True)
    period = models.IntegerField(verbose_name='建议学习周期',
                                 default=7)
    attachment_path = models.FileField(upload_to='attachment',
                                       verbose_name='课件路径',
                                       max_length=128,
                                       blank=True,
                                       null=True)
    status = models.SmallIntegerField(choices=status_choices,
                                      default=0,
                                      verbose_name='课程状态')
    students = models.IntegerField(verbose_name='学习人数',
                                   default=0)
    sections = models.IntegerField(verbose_name='总课时数量',
                                   default=0)
    pub_sections = models.IntegerField(verbose_name='课时更新数量',
                                       default=0)
    # DecimalField 浮点数，精度更高，存钱就用这个
    # max_digits=6 整数+小数最大6位
    # decimal_places=2 小数两位 9999.99
    price = models.DecimalField(max_digits=6,
                                decimal_places=2,
                                verbose_name="课程原价",
                                default=0)

    # 关联关系
    teacher = models.ForeignKey('Teacher',
                                on_delete=models.SET_NULL,
                                null=True,
                                blank=True,
                                verbose_name='授课老师')
    # db_constraint=False 数据库不建立强外键约束，数据存入时不作校验，会出现脏数据
    course_category = models.ForeignKey('CourseCategory',
                                        on_delete=models.SET_NULL,
                                        db_constraint=False,
                                        null=True,
                                        blank=True,
                                        verbose_name='课程分类')

    class Meta:
        db_table: str = 'luffy_course'
        verbose_name: str = '课程'
        verbose_name_plural: str = verbose_name

    def __str__(self) -> str:
        return '%s' % self.name


class Teacher(BaseModel):
    """ 教师表 """
    role_choices: Tuple[int, str] = (
        (0, '老师'),
        (1, '导师'),
        (2, '班主任'),
    )

    name = models.CharField(max_length=32,
                            verbose_name='名字')
    role = models.SmallIntegerField(choices=role_choices,
                                    default=0,
                                    verbose_name='角色')
    title = models.CharField(max_length=64,
                             verbose_name='职位')
    signature = models.CharField(max_length=255,
                                 null=True,
                                 blank=True,
                                 verbose_name='导师签名',
                                 help_text='导师签名')
    image = models.ImageField(upload_to='teacher',
                              null=True,
                              verbose_name='导师封面')
    brief = models.TextField(max_length=1024,
                             verbose_name='简介')

    class Meta:
        db_table: str = 'luffy_teacher'
        verbose_name: str = '教师'
        verbose_name_plural: str = verbose_name

    def __str__(self) -> str:
        return '%s' % self.name


class CourseChapter(BaseModel):
    """ 章节表 """
    chapter = models.SmallIntegerField(default=1,
                                       verbose_name='章节ID')
    name = models.CharField(max_length=32,
                            verbose_name='章节名')
    summary = models.TextField(max_length=1024,
                               verbose_name='章节介绍')
    pub_date = models.DateField(verbose_name='发布时间',
                                auto_now_add=True)

    course = models.ForeignKey('Course',
                               on_delete=models.CASCADE,
                               related_name='coursechapter',
                               verbose_name='课程名称')

    class Meta:
        db_table: str = 'luffy_course_chapter'
        verbose_name: str = '章节'
        verbose_name_plural: str = verbose_name

    def __str__(self) -> str:
        return '%s' % self.name


class CourseSection(BaseModel):
    """ 课时表 """
    section_type_choices: Tuple[int, str] = (
        (0, '文档'),
        (1, '练习'),
        (2, '视频'),
    )

    name = models.CharField(max_length=128, verbose_name='课时标题')
    # PositiveIntegerField 无符号整数
    order = models.PositiveIntegerField(verbose_name='课时排序')
    section_type = models.SmallIntegerField(choices=section_type_choices,
                                            default=2,
                                            verbose_name='课时种类')
    section_link = models.CharField(max_length=255,
                                    blank=True,
                                    null=True,
                                    help_text='若是video，填vid,若是文档，填link',
                                    verbose_name='课时链接')
    duration = models.CharField(max_length=32,
                                blank=True,
                                null=True,
                                verbose_name='课时时长')
    pub_date = models.DateField(verbose_name='更新时间',
                                auto_now_add=True)
    free_trail = models.BooleanField(verbose_name='是否可试看', default=False)

    chapter = models.ForeignKey('CourseChapter',
                                related_name='coursesections',
                                on_delete=models.CASCADE,
                                verbose_name='课程章节')

    class Meta:
        db_table: str = "luffy_course_section"
        verbose_name: str = "课时"
        verbose_name_plural: str = verbose_name

    def __str__(self) -> str:
        return '%s-%s' % (self.chapter, self.name)
