# abilium_taxonomy


## Usage

In order to add Tag fields to a view / model odoo studio needs to be installed.

### Add a Field

1. Open the view to which you want to add a Tag field.
1. Start the studio by clicking on the logo in the top right.
![logo](/doc/img/open_studio.png)
1. On the left, in the **+ Add** tab, select the **Many2many** field and place it in the view.
![logo](/doc/img/place_field.png)
1. Now a popup named **Field Properties** appears. Select **Taxonomy Tag** and click on **CONFIRM**.
![logo](/doc/img/field_properties.png)
1. In the **Properties** tab, rename the label to the name of the top level tag which you want to add.
1. For the widget select **Tags (many2many_tags)**.
1. Check the checkbox at **Disable creation**. This prevents users from creating new tags.
![logo](/doc/img/field_props.png)
1. Click on domain and in the popup click on **+ ADD FILTER**. Set the filter rule as shown in the screenshot (replace \<tag name> with the name of the top level tag) and save it.
![logo](/doc/img/field_domain.png)

If you close the studio, in that field you can now select all tags which are an anchestor of the tag specified in the domain.


### Add a Filter

1. In the studio, click on **Views > Search**
![logo](/doc/img/search_view.png)
1. On the left under the tab **+ Add** search for the field you just created and place it in the **Autocompletion Fields** list  
![logo](/doc/img/place_filter.png)
