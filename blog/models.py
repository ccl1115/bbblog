from django.db import models

class Article(models.Model):
    title = CharField(max_length=100, required=True)
    text = TextField(required=True)

    pub_datetime = DatetimeField(auto_now_add=True)
    mod_datetime = DatetimeField(auto_now=True, auto_now_add=True)

    def tags_as_ul(self, filter=None):
        if(type(filter) == str):
            tags = self.tag_set.filter(filter)
        else:
            tags = self.tag_set.all()
        ret = '<ul id="article_tags_%d">' % self.id
        for tag in tags:
            ret += '<li id="article_%d_tag_%d">%s</li>' % (self.id, tag.id)
        ret += '</ul>'
        return ret

    def comment_as_ul(self, page=1, size=10, filter=None):
        if(type(filter) == str):
            tags = self.comment_set.filter(filter)
        else:
            tags = self.tag_set.all()
        from django.core.paginator import Paginator
        comments = Paginator(tags, 

    def __unicode__(self):
        return self.title

class Comment(models.Model):
    name = CharField(max_length=100, required=True)
    email = EmailField(max_length=100, required=True)
    text = TextField(required=True)
    parent = ForeignKey('self') 
    article = ForeignKey(Article, related_name="comment_set")

    pub_datetime = DatetimeField(auto_now_add=True)


    def __unicode__(self):
        return self.name

class Tag(models.Model):
    name = CharField(max_length=100, required=True)
    parent = ForeignKey('self')
    article = ManyToManyField(Comment, related_name="tag_set")

    pub_datetime = DatetimeField(auto_now_add=True)
    mod_datetime = DatetimeField(auto_now=True, auto_now_add=True)

    def __unicode__(self):
        return self.name

class Widget(models.Model):
    name = CharField(max_length=100, required=True)
    template = FilePathField(required=True)
    css = FilePathField()

    pub_datetime = DatetimeField(auto_now_add=True)
    mod_datetime = DatetimeField(auto_now=True, auto_now_add=True)

    def __unicode__(self):
        return self.name

class Theme(models.Model):
    name = CharField(max_length=100, required=True)
    css = FilePathField(required=True)

    pub_datetime = DatetimeField(auto_now_add=True)
    mod_datetime = DatetimeField(auto_now=True, auto_now_add=True)

    def __unicode__(self):
        return self.name
