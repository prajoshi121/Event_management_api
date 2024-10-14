from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from events.models import UserProfile
from django.core.files import File
from django.core.exceptions import ValidationError

class Command(BaseCommand):
    help = 'Create multiple users and their profiles'

    def create_user_and_profile(self, username, password, email, full_name, bio, location, profile_picture_path):
        try:
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            self.stdout.write(self.style.SUCCESS(f'User "{user.username}" created successfully!'))

            user_profile = UserProfile(user=user, full_name=full_name, bio=bio, location=location)

            if profile_picture_path:
                with open(profile_picture_path, 'rb') as profile_picture_file:
                    user_profile.profile_picture.save(profile_picture_file.name, File(profile_picture_file), save=True)

            user_profile.save()
            self.stdout.write(self.style.SUCCESS(f'User profile for "{user.username}" created successfully!'))

        except ValidationError as e:
            self.stderr.write(self.style.ERROR(f'Error creating user or profile: {e}'))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'An unexpected error occurred: {e}'))

    def handle(self, *args, **kwargs):
        usernames = ["Kajol", "Jitesh"]
        passwords = ["mypassword1", "mypassword2"]
        emails = ["kajol1@email.com", "jitesh1@email.com"]
        full_names = ['Kajol Khanna', 'Jitesh Sharma']
        bios = ['Student', 'Student']
        locations = ['Goa', 'Goa']
        profile_picture_paths = [
            '/path/to/media/images/kajol.jpg',
            '/path/to/media/images/jitesh.jpg'
        ]

        for i in range(len(usernames)):
            self.create_user_and_profile(
                username=usernames[i],
                password=passwords[i],
                email=emails[i],
                full_name=full_names[i],
                bio=bios[i],
                location=locations[i],
                profile_picture_path=profile_picture_paths[i]
            )
