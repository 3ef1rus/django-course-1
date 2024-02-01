from tastypie.resources import ModelResource
from shop.models import Category, Course
from tastypie.authorization import Authorization
from .auth import CustomAuthetication

# Create your models here.


class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'categories'
        allowed_methods = ['get']


class CourseResource(ModelResource):
    class Meta:
        queryset = Course.objects.all()
        resource_name = 'courses'
        allowed_methods = ['get', 'post', 'delete']
        # в нижнем атрибуте можно убрать значения которые вы не хотите выводить пользователю в запросе get
        excludes = ['created_at']
        authetication = CustomAuthetication()
        authorization = Authorization()

    def hydrate(self, bundle):
        bundle.obj.category_id = bundle.data['category_id']
        return bundle

    def dehydrate(self, bundle):
        bundle.data['category_id'] = bundle.obj.category_id
        return bundle

    # def dehydrate_titel(self, bundle):  # пример изменения вывода данных при запросе get
    #     return bundle.data['titel'].upper()
