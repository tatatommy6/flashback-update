from PIL import Image
# image_path = "C://Users//tatat//Downloads//openai_simple_outpainting-master (1)//openai_simple_outpainting-master//sample//sample_img.jpg"
def canvas_clear() :
    new_image = Image.open("flashback-main/static/original_image.png")

    # Create a new transparent canvas
    canvas_size = (4024, 2048)
    new_canvas = Image.new("RGBA", canvas_size, (255, 255, 255, 0))

    # Calculate position to center the new image on the canvas
    new_image_size = new_image.size
    position = ((canvas_size[0] - new_image_size[0]) // 2, (canvas_size[1] - new_image_size[1]) // 2)

# Paste the new image onto the transparent canvas
    new_canvas.paste(new_image, position, new_image.convert("RGBA"))

# Save the resulting image
    new_output_path1 = "flashback-main/src/src.png"
    new_output_path2 = "flashback-main/src/mask.png"
    new_output_path3 = "flashback-main/src/sample.png"
    new_canvas.save(new_output_path1)
    new_canvas.save(new_output_path2)
    new_canvas.save(new_output_path3)

    new_output_path1
    new_output_path2
    new_output_path3




def after_process_image(file_path: Image):
    new_image = Image.open(f"flashback-main/static/{file_path}.png")

    # Create a new transparent canvas
    canvas_size = (5300, 1800)
    new_canvas = Image.new("RGBA", canvas_size, (255, 255, 255))

    # Calculate position to center the new image on the canvas
    new_image_size = new_image.size
    position = ((canvas_size[0] - new_image_size[0]) // 2, (canvas_size[1] - new_image_size[1]) // 2)

# Paste the new image onto the transparent canvas
    new_canvas.paste(new_image, position, new_image.convert("RGBA"))
    

    new_outoutput_path=f"flashback-main/static/{file_path}.png"
    new_canvas.save(new_outoutput_path)