from stark.service.sites import site,ModelStark
from app01 import models

site.register(models.Author)
# site.register(models.Book)
site.register(models.Publish)

class BookConfig(ModelStark):

    # def display_authors(self,obj=None,is_header=False):
    #
    #     if is_header:
    #         return '作者'
    #     s=[]
    #     for author in obj.authors.all():
    #         s.append(author.name)
    #
    #     return ' '.join(s)

    list_display = ['nid','title','price','authors','publish']
    search_fields = ['title', 'price']

    def patch_init(self,selected_pk):
        ret=self.model.objects.filter(pk__in=selected_pk).update(price=100)
    patch_init.desc='批量初始化'

    def patch_delete(self,selected_pk):
        ret=self.model.objects.filter(pk__in=selected_pk).delete()
    patch_delete.desc='批量删除'


    actions=[patch_init,patch_delete]

site.register(models.Book,BookConfig)


