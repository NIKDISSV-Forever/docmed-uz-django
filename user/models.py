def image_dir_path(instance, filename):
    extension = filename.split('.')[-1]
    new_filename = "profile_images/candidate_%s.%s" % (instance.name, extension)
    return new_filename


# class User(AbstractUser):
#     profile_image = models.ImageField(upload_to=image_dir_path, blank=True, null=True)
