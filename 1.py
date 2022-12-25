 class Meta:
        ordering = ("pk",)
        indexes = [
            GinIndex(
                name="address_search_gin",
                # `opclasses` and `fields` should be the same length
                fields=["first_name", "last_name", "city", "country"],
                opclasses=["gin_trgm_ops"] * 4,
            ),
            GinIndex(
                name="warehouse_address_search_gin",
                # `opclasses` and `fields` should be the same length
                fields=[
                    "company_name",
                    "street_address_1",
                    "street_address_2",
                    "city",
                    "postal_code",
                    "phone",
                ],
                opclasses=["gin_trgm_ops"] * 6,
            ),
        ]

    @property
    def full_name(self):
