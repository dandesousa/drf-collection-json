#!/usr/bin/env python
# encoding: utf-8


from collection_json import Collection, Data, Item, Link
from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework.relations import HyperlinkedIdentityField
from rest_framework.relations import HyperlinkedRelatedField
from rest_framework.renderers import JSONRenderer


class CollectionJSONRenderer(JSONRenderer):
    media_type = "application/vnd.collection+json"
    format = "collection+json"
    __link_cls__ = (HyperlinkedIdentityField, HyperlinkedRelatedField)

    def _is_field_hyperlink(self, field, value):
        for cls in self.__link_cls__:
            if isinstance(value, cls):
                return True
        return False

    def _infer_cj(self, data, serializer, **kwargs):
        """Renders a collection inferred from the data and serializer provided.

        :param data dict: Dictionary to render.
        :param serializer Serializer: Serializer use for the data provided.
        :param href str: URI to use for this resource.
        """
        href = kwargs.get("href", "")

        # is there an identity fields

        # which fields are related links
        link_fields = [field for field, obj in serializer.fields.items() if self._is_field_hyperlink(field, obj)]

        # generate the remaining fields
        if isinstance(data, dict):
            data = [data]

        def item_href(row):
            if isinstance(serializer, HyperlinkedModelSerializer):
                # TODO: should find the url field or IdentityField
                field = serializer.serializer_url_field
                return row["url"]
            else:
                return None

        def item_data(row):
            for field, value in row.items():
                yield Data(field, value)

        def item_links(row):
            for field in link_fields:
                yield Link(field, row[field])

        items = (Item(href=item_href(row),
                      data=item_data(row),
                      links=item_links(row)) for row in data)
        return Collection(href, items=items)

    def render(self, data, media_type=None, renderer_context=None):
        """Renders the data to collection+json hypermedia format.

        This renderer support multiple input types for data.

        If a Collection object is passed, will be renderer with
        collection_json module.

        TODO: If a dictionary is provided, and the view name is
        Api Root, renders everything as C+j links.

        If a dictionary/list is provided, along with an accessible
        serializer_class, it will infer the format and use the
        Hyperlinked fields to construct the hypermedia format.

        If a dictionary/list is provided, with no serializer_class, a
        TypeError is thrown.

        :param data object: the data to serialize to collection+json
        :raises TypeError: If the request had no serializer for the data.
        """
        if isinstance(data, Collection):
            data = data.to_dict()
        else:
            view = renderer_context["view"]
            serializer = getattr(view, "get_serializer", None)
            if not serializer:
                raise TypeError("Unable to generate a Collection+JSON object")
            request = renderer_context["request"]
            collection = self._infer_cj(data, serializer(),
                                        href=request.build_absolute_uri())
            data = collection.to_dict()

        return super(CollectionJSONRenderer, self).render(data, media_type,
                                                          renderer_context)
