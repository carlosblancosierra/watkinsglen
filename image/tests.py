from django.test import TestCase
from .models import Gallery, Image, GalleryImage, ImageTag

class GalleryTestCase(TestCase):
    def setUp(self):
        self.gallery = Gallery.objects.create(name='Test Gallery')

    def test_gallery_creation(self):
        self.assertEqual(self.gallery.name, 'Test Gallery')

    def test_gallery_str(self):
        self.assertEqual(str(self.gallery), 'Test Gallery')


class ImageTestCase(TestCase):
    def setUp(self):
        self.image = Image.objects.create(image='test_image.jpg')

    def test_image_creation(self):
        self.assertEqual(self.image.image, 'test_image.jpg')

    def test_image_str(self):
        self.assertEqual(str(self.image), self.image.image.url)


class GalleryImageTestCase(TestCase):
    def setUp(self):
        self.gallery = Gallery.objects.create(name='Test Gallery')
        self.image = Image.objects.create(image='test_image.jpg')
        self.gallery_image = GalleryImage.objects.create(gallery=self.gallery, image=self.image, order=1)

    def test_gallery_image_creation(self):
        self.assertEqual(self.gallery_image.gallery, self.gallery)
        self.assertEqual(self.gallery_image.image, self.image)
        self.assertEqual(self.gallery_image.order, 1)

    def test_gallery_image_order_increment(self):
        new_gallery_image = GalleryImage.objects.create(gallery=self.gallery, image=self.image, order=2)
        self.assertEqual(new_gallery_image.order, 2)
        self.assertEqual(self.gallery_image.order, 1)

    def test_gallery_image_order_update(self):
        self.gallery_image.order = 3
        self.gallery_image.save()
        updated_gallery_image = GalleryImage.objects.get(pk=self.gallery_image.pk)
        self.assertEqual(updated_gallery_image.order, 3)

    def test_gallery_image_order_max_order_none(self):
        GalleryImage.objects.all().delete()
        new_gallery_image = GalleryImage.objects.create(gallery=self.gallery, image=self.image)
        self.assertEqual(new_gallery_image.order, 1)

    def test_gallery_image_order_max_order_exists(self):
        GalleryImage.objects.create(gallery=self.gallery, image=self.image, order=3)
        new_gallery_image = GalleryImage.objects.create(gallery=self.gallery, image=self.image)
        self.assertEqual(new_gallery_image.order, 4)

    def test_gallery_image_ordering(self):
        GalleryImage.objects.create(gallery=self.gallery, image=self.image, order=3)
        GalleryImage.objects.create(gallery=self.gallery, image=self.image, order=2)
        GalleryImage.objects.create(gallery=self.gallery, image=self.image, order=4)
        gallery_images = GalleryImage.objects.filter(gallery=self.gallery)
        expected_order = [1, 2, 3, 4]
        self.assertEqual([gi.order for gi in gallery_images], expected_order)


class ImageTagTestCase(TestCase):
    def setUp(self):
        self.image_tag = ImageTag.objects.create(tag='Test Tag')

    def test_image_tag_creation(self):
        self.assertEqual(self.image_tag.tag, 'Test Tag')

    def test_image_tag_str(self):
        self.assertEqual(str(self.image_tag), 'Test Tag')from django.test import TestCase
from .models import Gallery, Image, GalleryImage

class GalleryImageTestCase(TestCase):
    def setUp(self):
        self.gallery = Gallery.objects.create(name='Test Gallery')
        self.image = Image.objects.create(image='test_image.jpg')
        self.gallery_image = GalleryImage.objects.create(gallery=self.gallery, image=self.image, order=1)

    def test_gallery_image_create(self):
        gallery_image_count = GalleryImage.objects.count()
        new_gallery_image = GalleryImage.objects.create(gallery=self.gallery, image=self.image, order=2)
        self.assertEqual(GalleryImage.objects.count(), gallery_image_count + 1)
        self.assertEqual(new_gallery_image.order, 2)

    def test_gallery_image_read(self):
        retrieved_gallery_image = GalleryImage.objects.get(pk=self.gallery_image.pk)
        self.assertEqual(retrieved_gallery_image.gallery, self.gallery)
        self.assertEqual(retrieved_gallery_image.image, self.image)
        self.assertEqual(retrieved_gallery_image.order, 1)

    def test_gallery_image_update(self):
        self.gallery_image.order = 3
        self.gallery_image.save()
        updated_gallery_image = GalleryImage.objects.get(pk=self.gallery_image.pk)
        self.assertEqual(updated_gallery_image.order, 3)

    def test_gallery_image_delete(self):
        gallery_image_count = GalleryImage.objects.count()
        self.gallery_image.delete()
        self.assertEqual(GalleryImage.objects.count(), gallery_image_count - 1)
