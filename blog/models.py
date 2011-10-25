from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()

    pub_datetime = models.DateTimeField(auto_now_add=True)
    mod_datetime = models.DateTimeField(auto_now=True, auto_now_add=True)

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

    def comments_count(self, filter=None):
        if(type(filter) == str):
            return len(self.comment_set.filter(filter))
        else:
            return self.comment_set.count()

    def tags_count(self):
        return len(self.tag_set.count())

    def __unicode__(self):
        return self.title

class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    text = models.TextField()
    parent = models.ForeignKey('self') 
    article = models.ForeignKey(Article, related_name="comment_set")

    pub_datetime = models.DateTimeField(auto_now_add=True)


    def __unicode__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self')
    article = models.ManyToManyField(Comment, related_name="tag_set")

    pub_datetime = models.DateTimeField(auto_now_add=True)
    mod_datetime = models.DateTimeField(auto_now=True, auto_now_add=True)

    def __unicode__(self):
        return self.name

class Widget(models.Model):
    name = models.CharField(max_length=100)
    template = models.FilePathField()
    css = models.FilePathField()

    pub_datetime = models.DateTimeField(auto_now_add=True)
    mod_datetime = models.DateTimeField(auto_now=True, auto_now_add=True)

    def __unicode__(self):
        return self.name

class Theme(models.Model):
    name = models.CharField(max_length=100)
    css = models.FilePathField()

    pub_datetime = models.DateTimeField(auto_now_add=True)
    mod_datetime = models.DateTimeField(auto_now=True, auto_now_add=True)

    def __unicode__(self):
        return self.name
