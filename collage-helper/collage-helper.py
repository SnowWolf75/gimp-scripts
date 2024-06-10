from gimpfu import *
import sys

# sys.stderr = open('C:/Utils/Adb-shapez/python-fu-output.txt','a')
# sys.stdout = sys.stderr
# So that they both go to the same file
gimp_message("Hello world")


def layer_link_and_difference(image):
    print("## Start; Layer Link")
    active_layer = pdb.gimp_image_get_active_layer(image)
    pdb.gimp_layer_set_mode(active_layer, 32)
    pdb.gimp_item_set_linked(active_layer, 1)
    print("## End; Layer Link")


def layer_mode_set_normal(image):
    print("## End; Set Normal")
    active_layer = pdb.gimp_image_get_active_layer(image)
    pdb.gimp_layer_set_mode(active_layer, 28)
    print("## End; Set Normal")


print("## Start; Main body")
register(
    "layer_link_and_difference",
    "Set the layer's link status and change mode to Difference",
    "Set the layer's link status and change mode to Difference",
    "Author",
    "Author",
    "2024",
    "Layer Link and Difference",
    "RGB*",
    [  # List of input parameters (just one here)
        (PF_IMAGE, "image", "Input image", None)  # Just an image, since it's the first one, Gimp
        # Sets it implicitly without showing a dialog
    ],
    [],
    layer_link_and_difference,
    menu="<Image>/Layer/Collage"
)

register(
    "layer_mode_set_normal",
    "Set the layer mode back to Normal",
    "Set the layer mode back to Normal",
    "Author",
    "Author",
    "2024",
    "<Image>/Layer/Collage/Layer Mode to Normal",
    "RGB*",
    [  # List of input parameters (just one here)
        (PF_IMAGE, "image", "Input image", None)  # Just an image, since it's the first one, Gimp
        # Sets it implicitly without showing a dialog
    ],
    [],
    layer_mode_set_normal)

main()
print("## End; Main body")

