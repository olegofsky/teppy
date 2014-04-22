import random
from django.contrib.auth.models import User

from source.tests.models import TestCase, TestSuit

desc = 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. Donec sodales sagittis magna. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc,'
user = User.objects.get(id=1)
suits = list(TestSuit.objects.all())
for i in range(20):
    TestCase.objects.create(
        author=user,
        developer=user,
        producer=user,
        priority=TestCase.PRIORITY_MID,
        status=TestCase.STATUS_ACTIVE,
        idea=desc[random.randint(1, 10): random.randint(10, len(desc))],
        procedure=desc[random.randint(1, 10): random.randint(10, len(desc))],
        setup=desc[random.randint(1, 10): random.randint(10, len(desc))],
        expected_result=desc[random.randint(1, 10): random.randint(10, len(desc))],
        suit=random.choice(suits),
    )
