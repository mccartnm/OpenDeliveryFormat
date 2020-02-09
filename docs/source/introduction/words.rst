Terminology
===========

Let's go through some of the terminology of ODF. From the onset, we try to set this as the standard for communicating between workflows. There are a number of words in the industry that typically mean multiple things. "Shot", "Take", "Sequence", "Asset", "Version", are a few examples.

ODF tries to lay out what each of the general elements is. Ideally, a pipeline user (artist, producer, etc.), doesn't have to know what these terms are. Only the technical users implementing their studios ODF protocols, should really have to know the intricate details.

.. glossary::

    Component
        .. image:: ../_static/components.svg

        A component is the lowest level we can get with packable content. These are any "things" that get shipped in an ODF manifest. Some examples might be:

        * Image Sequence (plate)
        * Quicktime
        * Note
        * Annotation
        * Cache
        * Model
        * ...

        There are an endless number of components but ODF tries to define the essentials.

    Specification (Spec)
        .. image:: ../_static/specs.svg

        A definition for work/deliverables. Each ``Container`` has a type which is linked to the name of a ``Spec``. That way, we know exactly what ``Components`` a ``Container`` requires for both ingest as well as delivery.

    Container
        .. image:: ../_static/containers.svg

        A virtual bucket for work to be done. For many pipelines, this usually takes the form of the Shot, Take, Asset, Sequence, etc. This holds onto
        metadata and a variable number of Components.

    Content
        .. image:: ../_static/content.svg

        The physical files. These gets attached to components that are not metadata. A ``plate`` or ``quicktime`` has content attached while a ``note`` would not.

    Metadata
        .. image:: ../_static/meta.svg

        Any information-only data. This is typically packed within the ODF manifest and requires no physical files to be present. A spec/manifest can be completely made of metadata components and no physical files.

    Manifest
        .. image:: ../_static/manifest.svg

        The culmination of all of the above, the ODF manifest describes a list of containers to be worked on or delivered for. The manifest can define abstract metadata as well.
