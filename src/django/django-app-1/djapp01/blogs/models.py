from django.db import models
# Create your models here.

BLOG_ELEMENT_SEGEMENTS = (
    ('h1', 'Header'),
    ('h2', 'Header 2'),
    ('h3', 'Header 3'),
    ('h4', 'Header 4'),
    ('h5', 'Header 5'),
    ('h6', 'Header 6'),
    ('p', 'Paragraph'),
    ('ul', 'UnorderedLine'),
    ('ol', 'OrderedLine'),
    ('img', 'Images'),
    ('a', "Anchor"),
    ('br', "LineBreak"),
    ('code', "code"),
    ('content', "content"),


)


class Header(models.Model):
    author = models.ForeignKey(
        'authors.User', on_delete=models.CASCADE)
    topic = models.TextField("Topic", null=True, blank=True)
    CreatedDate = models.DateTimeField(
        "Blog_CreatedDate", auto_now_add=True)
    blog_created_by = models.CharField(max_length=100)

    def __str__(self):
        return "Blog Header"


class Details(models.Model):
    blog = models.ForeignKey(Header, on_delete=models.CASCADE)
    line_no = models.IntegerField(default=0)
    image_title = models.CharField(max_length=100, default='Image', null=True)
    images = models.ImageField(null=True, upload_to='images/', blank=True,)
    detail_element = models.CharField(
        max_length=100, choices=BLOG_ELEMENT_SEGEMENTS)
    element_text = models.TextField()
    detail_created_by = models.ForeignKey(
        'authors.User', on_delete=models.CASCADE)
    created_date = models.DateTimeField(
        "details_created_date", auto_now_add=True)
    created_by = models.CharField(max_length=100)

    # def save(self, *args, **kwargs):
    #     if self._state.adding:
    #         last_id = self.objects.all().aggregate(
    #             largest=models.Max('line_no'))['largest']

    #         if last_id is not None:
    #             self.blog_line_no = last_id + 1

    #     super(Details, self).save(*args, **kwargs)

    def __str__(self):
        return "Blog Details:  " + self.blog.topic + " Line#:" + str(self.line_no)
