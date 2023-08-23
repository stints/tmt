from django.test import TestCase
from django.utils import timezone
from rest_framework.test import APIClient

from interview.inventory.models import (
    Inventory,
    InventoryLanguage,
    InventoryTag,
    InventoryType,
)


class BaseInventoryTestCase(TestCase):
    def setUp(self) -> None:
        # Create inventory languages
        self.inventory_language_1 = InventoryLanguage.objects.create(name="English")
        self.inventory_language_2 = InventoryLanguage.objects.create(name="Spanish")

        # Create inventory tags
        self.inventory_tag_1 = InventoryTag.objects.create(name="Action")
        self.inventory_tag_2 = InventoryTag.objects.create(name="Sci-Fi")

        # Create inventory types
        self.inventory_type_1 = InventoryType.objects.create(name="Movie")
        self.inventory_type_2 = InventoryType.objects.create(name="TV Show")

        # Create inventories
        self.inventory_1 = Inventory.objects.create(
            name="Action Movie",
            type=self.inventory_type_1,
            language=self.inventory_language_1,
            metadata={"duration": "2h 16m"},
        )
        self.inventory_1.tags.add(self.inventory_tag_1)

        self.inventory_2 = Inventory.objects.create(
            name="Sci Fi Movie",
            type=self.inventory_type_2,
            language=self.inventory_language_2,
            metadata={"duration": "1h 30m"},
        )
        self.inventory_2.tags.add(self.inventory_tag_2)


class InventoryTestCase(BaseInventoryTestCase):
    def test_inventory_list_created_after(self) -> None:
        client = APIClient()
        base = client.get("http://testserver/inventory/")
        self.assertEqual(base.status_code, 200)
        self.assertEqual(len(base.json()), 2)

        # Modify the created_at date of inventory_1 to be 3 days ago
        three_days_ago = timezone.now() - timezone.timedelta(days=3)
        self.inventory_1.created_at = three_days_ago
        self.inventory_1.save(update_fields=["created_at"])

        yesterdays_date = timezone.now().date() - timezone.timedelta(days=1)
        created_after_today = client.get(
            f"http://testserver/inventory/?created_after={yesterdays_date}"
        )
        self.assertEqual(created_after_today.status_code, 200)
        self.assertEqual(len(created_after_today.json()), 1)
