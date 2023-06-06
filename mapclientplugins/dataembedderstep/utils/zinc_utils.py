"""
Created on Oct 13, 2021

@author: Richard Christie
"""
from cmlibs.utils.zinc.general import ChangeManager, HierarchicalChangeManager
from cmlibs.zinc.node import Nodeset
from cmlibs.zinc.field import Field, FieldGroup
from cmlibs.zinc.scene import Scene


def get_scene_selection_group(scene: Scene, subelement_handling_mode=FieldGroup.SUBELEMENT_HANDLING_MODE_FULL):
    """
    Get existing scene selection group of standard name.
    :param scene: Zinc Scene to get selection group for.
    :param subelement_handling_mode: Mode controlling how faces, lines and nodes are
    automatically added or removed with higher dimensional elements.
    :return: Existing selection group, or None.
    """
    selection_group = scene.getSelectionField().castGroup()
    if selection_group.isValid():
        selection_group.setSubelementHandlingMode(subelement_handling_mode)
        return selection_group
    return None


selection_group_name = 'cmiss_selection'


def create_scene_selection_group(scene: Scene, subelement_handling_mode=FieldGroup.SUBELEMENT_HANDLING_MODE_FULL):
    """
    Create empty, unmanaged scene selection group of standard name.
    Should have already called get_selection_group with None returned.
    Can discover orphaned group of that name.
    :param scene: Zinc Scene to create selection for.
    :param subelement_handling_mode: Mode controlling how faces, lines and nodes are
    automatically added or removed with higher dimensional elements. Defaults to on/full.
    :return: Selection group for scene.
    """
    region = scene.getRegion()
    fieldmodule = region.getFieldmodule()
    with ChangeManager(fieldmodule):
        selection_group = fieldmodule.findFieldByName(selection_group_name)
        if selection_group.isValid():
            selection_group = selection_group.castGroup()
            if selection_group.isValid():
                selection_group.clear()
                selection_group.setManaged(False)
        if not selection_group.isValid():
            selection_group = fieldmodule.createFieldGroup()
            selection_group.setName(selection_group_name)
        selection_group.setSubelementHandlingMode(subelement_handling_mode)
    scene.setSelectionField(selection_group)
    return selection_group


def group_add_group_elements(group: FieldGroup, other_group: FieldGroup, highest_dimension_only=True):
    """
    Add to group elements from other_group.
    :param group:  Zinc FieldGroup to modify.
    :param other_group:  Zinc FieldGroup to add elements from.
    :param highest_dimension_only: If set (default), only add elements of
    highest dimension present in other_group, otherwise add all dimensions.
    """
    region = group.getFieldmodule().getRegion()
    with HierarchicalChangeManager(region):
        other_fieldmodule = other_group.getFieldmodule()
        for dimension in range(3, 0, -1):
            mesh = other_fieldmodule.findMeshByDimension(dimension)
            other_mesh_group = other_group.getMeshGroup(mesh)
            if other_mesh_group.isValid() and (other_mesh_group.getSize() > 0):
                mesh_group = group.getOrCreateMeshGroup(mesh)
                mesh_group.addElementsConditional(other_group)
                if highest_dimension_only:
                    break


def group_add_group_nodes(group: FieldGroup, other_group: FieldGroup, nodeset: Nodeset):
    """
    Add to group elements and/or nodes from other_group.
    :param group:  Zinc FieldGroup to modify.
    :param other_group:  Zinc FieldGroup to add nodes from.
    :param nodeset: Nodeset to add nodes from.
    """
    other_nodeset_group = other_group.getNodesetGroup(nodeset)
    if other_nodeset_group.isValid() and (other_nodeset_group.getSize() > 0):
        region = group.getFieldmodule().getRegion()
        with HierarchicalChangeManager(region):
            nodeset_group = group.getOrCreateNodesetGroup(nodeset)
            nodeset_group.addNodesConditional(other_group)


def field_is_managed_real_1_to_3_components(field_in: Field):
    """
    Conditional function returning True if the field is real-valued
    with up to 3 components, and is managed.
    """
    return (field_in.getValueType() == Field.VALUE_TYPE_REAL) and \
        (field_in.getNumberOfComponents() <= 3) and field_in.isManaged()
