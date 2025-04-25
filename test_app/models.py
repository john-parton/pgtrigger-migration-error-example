from django.db import models
import pgtrigger

class Product(models.Model):
    pass

class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
    )

class ProductVariant(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
    )

    class Meta:
        triggers = [
            pgtrigger.Trigger(
                name="product_variant_consistency",
                operation=pgtrigger.UpdateOf("product_id"),
                when=pgtrigger.After,
                condition=pgtrigger.AnyChange("product_id"),
                func="""
                    -- Ensure that the related ProductVariant.product_id matches
                    -- all related VariantImage.variant.product_id
                    IF EXISTS (SELECT
                        1
                    FROM
                        catalog_variantimage
                    WHERE
                        variant_id = OLD.id
                    ) THEN
                        RAISE EXCEPTION 'ProductImage and ProductVariant must have the same product_id';
                    END IF;
                """,
            ),
        ]

class VariantImage(models.Model):
    # This is a through model for the ProductVariant.images field
    variant = models.ForeignKey(
        ProductVariant,
        on_delete=models.CASCADE,
    )
    image = models.ForeignKey(
        ProductImage,
        on_delete=models.CASCADE,
    )

    class Meta:
        unique_together = (("variant", "image"),)
